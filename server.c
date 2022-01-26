#include <stdio.h>
#include <string.h> //strlen
#include <stdlib.h>
#include <errno.h>
#include <sys/ioctl.h>
#include <unistd.h>		 //close
#include <arpa/inet.h> //close
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/time.h> //FD_SET, FD_ISSET, FD_ZERO macros
#include <netdb.h>

#define _GNU_SOURCE
#define TRUE 1
#define FALSE 0
#define PORT 1100

// Message headers
#define LOGIN "LOGIN"
#define LOGOUT "LOGOUT"
#define REGISTER "REGISTER"
#define LIST "LIST"
#define ERR "ERR"
#define MSG "MSG"

int main(int argc, char *argv[])
{
	int opt = TRUE;		 // opt for reusing addresses
	int master_socket; // master server socket
	int new_socket;		 // new socet for incoming connections
	int sd;						 // auxiliary socket descriptor
	int max_sd;				 // maximum socket number

	int client_socket[30];	// list of client socket descriptors
	int max_clients = 30;		// maximum of clients
	char user_list[30][50]; // usernames of active clients
	int read_bytes_value;		// number of bytes in read message

	char buffer[1025];
	char err_msg[256];
	fd_set readfds;	 // set of socket descriptors
	FILE *users_fd;	 // file descriptor for users.txt
	FILE *outbox_fd; // file descriptor for outbox.txt

	struct sockaddr_in address;
	int addrlen;
	address.sin_family = AF_INET;
	address.sin_addr.s_addr = INADDR_ANY;
	address.sin_port = htons(PORT);
	addrlen = sizeof(address);

	// clear list of active users
	memset(user_list, 0, sizeof user_list);

	// initialise all client_socket[] to 0 so not checked
	for (int i = 0; i < max_clients; i++)
	{
		client_socket[i] = 0;
	}

	// create a master socket
	if ((master_socket = socket(AF_INET, SOCK_STREAM, 0)) == 0)
	{
		perror("socket failed");
		exit(EXIT_FAILURE);
	}

	// set master socket to allow multiple connections,
	// this is just a good habit, it will work without this
	if (setsockopt(master_socket, SOL_SOCKET, SO_REUSEADDR, (char *)&opt, sizeof(opt)) < 0)
	{
		perror("setsockopt failed");
		exit(EXIT_FAILURE);
	}

	// set socket to be non-blocking
	if (ioctl(master_socket, FIONBIO, (char *)&opt) < 0)
	{
		perror("ioctl failed");
		close(master_socket);
		exit(EXIT_FAILURE);
	}

	// bind the socket to localhost port 1100
	if (bind(master_socket, (struct sockaddr *)&address, addrlen) < 0)
	{
		perror("binding to socket failed");
		exit(EXIT_FAILURE);
	}

	// listen with maximum of 3 pending connections for the master socket
	if (listen(master_socket, 3) < 0)
	{
		perror("listen");
		exit(EXIT_FAILURE);
	}

	printf("Listener on port %d \n", PORT);
	puts("Waiting for connections ...");

	// -------------------SERVER MAIN LOOP-------------------
	while (TRUE)
	{
		// clear the socket set
		FD_ZERO(&readfds);

		// clear buffer
		memset(buffer, 0, sizeof buffer);

		// clear error message and add ERR header
		memset(err_msg, 0, sizeof err_msg);
		strcat(err_msg, "#");
		strcat(err_msg, ERR);
		strcat(err_msg, "#");

		// add master socket to set
		FD_SET(master_socket, &readfds);
		max_sd = master_socket;

		// add child sockets to set
		for (int i = 0; i < max_clients; i++)
		{
			// assign socket descriptor for convenience
			sd = client_socket[i];

			// if valid socket descriptor then add to read list
			if (sd > 0)
				FD_SET(sd, &readfds);

			// highest file descriptor number, useful for the select function
			if (sd > max_sd)
				max_sd = sd;
		}

		// wait for an activity on one of the sockets, timeout is NULL, so wait indefinitely
		if ((select(max_sd + 1, &readfds, NULL, NULL, NULL) < 0) && (errno != EINTR))
		{
			printf("select error");
		}

		// if something happened on the master socket then its an incoming connection
		if (FD_ISSET(master_socket, &readfds))
		{
			if ((new_socket = accept(master_socket, (struct sockaddr *)&address, (socklen_t *)&addrlen)) < 0)
			{
				perror("accept");
				exit(EXIT_FAILURE);
			}

			printf("New connection, socket fd is %d, ip is : %s, port : %d \n", new_socket,
						 inet_ntoa(address.sin_addr), ntohs(address.sin_port));

			// add new socket to array of sockets
			for (int i = 0; i < max_clients; i++)
			{
				// if position is empty
				if (client_socket[i] == 0)
				{
					client_socket[i] = new_socket;
					printf("Adding to list of sockets as %d\n", i);
					break;
				}
			}
		}

		// else it's some IO operation on some other socket
		for (int i = 0; i < max_clients; i++)
		{
			sd = client_socket[i];

			if (FD_ISSET(sd, &readfds))
			{
				// check if it was for closing, and also read the incoming message
				if ((read_bytes_value = read(sd, buffer, 1024)) == 0)
				{
					// somebody disconnected , get his details and print
					getpeername(sd, (struct sockaddr *)&address, (socklen_t *)&addrlen);
					printf("Host disconnected, ip %s, port %d \n", inet_ntoa(address.sin_addr), ntohs(address.sin_port));

					// close the socket and mark as 0 in list for reuse
					memset(user_list[i], 0, sizeof user_list[i]);
					close(sd);
					client_socket[i] = 0;
				}
				// process incoming message
				else
				{
					// assigning useful variables
					char *token;						// for tokens from strtok() function
					char delimiter[] = "#"; // delimiter for extracting parts of message
					char *outbox_token;			// for reading outbix messages
					char outbox_delimiter[] = "$";

					// get first token - type of message (LOGIN, REGISTER, LIST, MSG)
					token = strtok(buffer, delimiter);

					// LOGIN-----------------------------------------------------------------------------------
					// this will accept messages with #LOGIN# prefix and return list of logged users
					if (strcmp(token, LOGIN) == 0)
					{
						char *username, *password;

						// get USERNAME token
						token = strtok(NULL, delimiter);
						if (token != NULL)
						{
							username = token;
						}
						else
						{
							strcat(err_msg, "Username or password not provided#");
							send(sd, err_msg, strlen(err_msg), 0);
							continue;
						}

						// get PASSWORD token
						token = strtok(NULL, delimiter);
						if (token != NULL)
						{
							password = token;
						}
						else
						{
							strcat(err_msg, "Username or password not provided#");
							send(sd, err_msg, strlen(err_msg), 0);
							continue;
						}

						// open file with registered users
						users_fd = fopen("./data/users.txt", "r");
						char line[256]; // to store line read from file

						// copy username to list of active users on the same index as socket
						strcpy(user_list[i], username);

						// concatenate user data to format: "user password"
						char userdata[256];
						strcpy(userdata, username);
						strcat(userdata, " ");
						strcat(userdata, password);
						strcat(userdata, "\n");

						int found = FALSE;
						while (fgets(line, sizeof(line), users_fd))
						{
							if (strcmp(line, userdata) == 0)
							{
								printf("Successfully logged in user %s\n", username);
								found = TRUE;
								break;
							}
						}
						fclose(users_fd);

						// if user is registered then return list of active users, if not - return an error
						if (found)
						{
							// return list of active users
							// concatenated string of all active users names (30x50 bytes + delimiters)
							char list[2000];
							strcpy(list, "#");
							strcat(list, LIST);
							strcat(list, "#");

							// add to list all active users
							for (int j = 0; j < max_clients; j++)
							{
								if ((strcmp(user_list[j], "") != 0) && j != i)
								{
									strcat(list, "T#");
									strcat(list, user_list[j]);
									strcat(list, "#");
								}
							}

							// open file with registered users
							users_fd = fopen("./data/users.txt", "r");
							char username[50];

							while (!feof(users_fd))
							{
								// get only first word of the line which is username
								fscanf(users_fd, "%s%*[^\n]", username);
								// registered user is not yet on the list - that means he is offline
								// also dont return current user in the list
								if (!strcasestr(list, username) && (strcmp(username, user_list[i]) != 0))
								{
									strcat(list, "F#");
									strcat(list, username);
									strcat(list, "#");
								}
							}
							fclose(users_fd);

							list[strlen(list)] = '\0';
							send(sd, list, strlen(list), 0);
						}
						else
						{
							strcat(err_msg, "Invalid login or password#");
							send(sd, err_msg, strlen(err_msg), 0);
							continue;
						}

						// check if there are messages in outbox for this user
						outbox_fd = fopen("./data/outbox.txt", "r");
						char outbox_line[256]; // to store line read from file
						char msg_for_user[256];

						FILE *temp_fd = fopen("./data/temp.txt", "w"); // create temporary file
						char temp_line[256];

						while (fgets(outbox_line, sizeof(outbox_line), outbox_fd))
						{
							outbox_token = strtok(outbox_line, outbox_delimiter);
							// found message for user
							if (strcmp(outbox_token, username) == 0)
							{
								// get message to send
								outbox_token = strtok(NULL, outbox_delimiter);
								strcpy(msg_for_user, outbox_token);
								send(sd, msg_for_user, strlen(msg_for_user), 0);
							}
							// copy all lines that are not sent to temporary file
							else
							{
								// merge line back to its original form
								strcpy(temp_line, "$");
								strcat(temp_line, outbox_token);
								strcat(temp_line, "$");
								outbox_token = strtok(NULL, outbox_delimiter);
								strcat(temp_line, outbox_token);
								
								// write line in the temp file
								fputs(temp_line, temp_fd);
							}
						}
						fclose(outbox_fd);
						fclose(temp_fd);
						// remove existing outbox.txt file and replace it with temp.txt file
						remove("./data/outbox.txt");
						rename("./data/temp.txt", "./data/outbox.txt");
					}

					// LOGOUT-----------------------------------------------------------------------------------
					else if (strcmp(token, LOGOUT) == 0)
					{
						memset(user_list[i], 0, sizeof user_list[i]);
						send(sd, "#LOGOUT#Logged out#", strlen("#LOGOUT#Logged out#"), 0);
					}

					// REGISTER-----------------------------------------------------------------------------------
					else if (strcmp(token, REGISTER) == 0)
					{
						char *username, *password;

						// get USERNAME token
						token = strtok(NULL, delimiter);
						if (token != NULL)
						{
							username = token;
						}
						else
						{
							strcat(err_msg, "Username or password not provided#");
							send(sd, err_msg, strlen(err_msg), 0);
							continue;
						}

						// get PASSWORD token
						token = strtok(NULL, delimiter);
						if (token != NULL)
						{
							password = token;
						}
						else
						{
							strcat(err_msg, "Username or password not provided#");
							send(sd, err_msg, strlen(err_msg), 0);
							continue;
						}

						printf("Successfully registered user: username=%s, password=%s\n", username, password);

						// open file with registered users with append option
						users_fd = fopen("./data/users.txt", "a");

						// concatenate user data to format: "user password"
						char userdata[256];
						strcpy(userdata, username);
						strcat(userdata, " ");
						strcat(userdata, password);
						strcat(userdata, "\n");

						// append user data to file and close file
						fputs(userdata, users_fd);
						fclose(users_fd);

						send(sd, "#REGISTER#Succesfully registered#", strlen("#REGISTER#Succesfully registered#"), 0);
					}

					// LIST-----------------------------------------------------------------------------------
					// this will return list of all users and info if they are active or not
					// #T# prefix before the username means that he is active; #F# - unactive
					if (strcmp(token, LIST) == 0)
					{
						// check if client is logged in, if not return an error
						if (strcmp(user_list[i], "") == 0)
						{
							strcat(err_msg, "You must log in#");
							send(sd, err_msg, strlen(err_msg), 0);
							continue;
						}

						char list[2000];
						strcpy(list, "#");
						strcat(list, LIST);
						strcat(list, "#");

						// add to list all active users
						for (int j = 0; j < max_clients; j++)
						{
							if ((strcmp(user_list[j], "") != 0) && j != i)
							{
								strcat(list, "T#");
								strcat(list, user_list[j]);
								strcat(list, "#");
							}
						}

						// open file with registered users
						users_fd = fopen("./data/users.txt", "r");
						char username[50];

						while (!feof(users_fd))
						{
							// get only first word of the line which is username
							fscanf(users_fd, "%s%*[^\n]", username);
							// registered user is not yet on the list - that means he is offline
							// also dont return current user in the list
							if (!strcasestr(list, username) && (strcmp(username, user_list[i]) != 0))
							{
								strcat(list, "F#");
								strcat(list, username);
								strcat(list, "#");
							}
						}
						fclose(users_fd);

						list[strlen(list)] = '\0';
						send(sd, list, strlen(list), 0);
					}

					// MSG-----------------------------------------------------------------------------------
					// send message from one client to another
					if (strcmp(token, MSG) == 0)
					{
						// check if client is logged in, if not return an error
						if (strcmp(user_list[i], "") == 0)
						{
							strcat(err_msg, "You must log in#");
							send(sd, err_msg, strlen(err_msg), 0);
							continue;
						}

						char *reciever, *message;
						int reciever_sd = -1;
						char msg_to_send[256];

						// get RECIEVER token
						token = strtok(NULL, delimiter);
						if (token != NULL)
						{
							reciever = token;
						}
						else
						{
							strcat(err_msg, "Reciever or message not provided#");
							send(sd, err_msg, strlen(err_msg), 0);
							continue;
						}

						// get MESSAGE token
						token = strtok(NULL, delimiter);
						if (token != NULL)
						{
							message = token;
						}
						else
						{
							strcat(err_msg, "Reciever or message not provided#");
							send(sd, err_msg, strlen(err_msg), 0);
							continue;
						}

						// find reciever in active users list
						for (int j = 0; j < max_clients; j++)
						{
							if (strcmp(user_list[j], reciever) == 0)
							{
								reciever_sd = client_socket[j];
								break;
							}
						}

						// if no active user found
						if (reciever_sd == -1)
						{
							// chceck if reciever exists in registered users

							int found = FALSE;
							users_fd = fopen("./data/users.txt", "r");
							char username[50];

							while (!feof(users_fd))
							{
								// get only first word of the line which is username
								fscanf(users_fd, "%s%*[^\n]", username);
								if (strcmp(reciever, username) == 0)
								{
									found = TRUE;
									break;
								}
							}
							fclose(users_fd);

							if (found)
							{
								// add message to outbox file and send it whet user will log in
								// structure of message to send later is: $TO_WHO$#MSG#FROM_WHO#MESSAGE#
								strcpy(msg_to_send, "$");
								strcat(msg_to_send, reciever);
								strcat(msg_to_send, "$");
								strcat(msg_to_send, "#");
								strcat(msg_to_send, MSG);
								strcat(msg_to_send, "#");
								strcat(msg_to_send, user_list[i]); // sender
								strcat(msg_to_send, "#");
								strcat(msg_to_send, message);
								strcat(msg_to_send, "#\n");

								// open file with messages to send later
								outbox_fd = fopen("./data/outbox.txt", "a");
								fputs(msg_to_send, outbox_fd);
								fclose(users_fd);
							}
							else
							{
								strcat(err_msg, "Reciever of the message was not found#");
								send(sd, err_msg, strlen(err_msg), 0);
								continue;
							}
						}
						else
						{
							// send message to reciever
							strcpy(msg_to_send, "#");
							strcat(msg_to_send, MSG);
							strcat(msg_to_send, "#");
							strcat(msg_to_send, user_list[i]); // sender
							strcat(msg_to_send, "#");
							strcat(msg_to_send, message);
							strcat(msg_to_send, "#");

							send(reciever_sd, msg_to_send, strlen(msg_to_send), 0);
						}
					}
				}
			}
		}
	}

	return EXIT_SUCCESS;
}
