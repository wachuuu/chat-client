import select
import socket
import sys

HOST = "127.0.0.1"
PORT = 1100

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	
	# show start menu
	print("1: LOGIN \n"
				+ "2: REGISTER \n"
				+ "3: LIST \n"
				+ "4: MESSAGE \n"
				+ "5: REFRESH \n"
				+ "6: LOGOUT \n")

	while True:
		# listen to events from stdin or socket
		r, w, x = select.select([sys.stdin, s], [], [])

		# we are interested only in reading
		if not r:
			continue

		# if something appears on input console
		if r[0] is sys.stdin:
			opt = input(
				"1: LOGIN \n"
				+ "2: REGISTER \n"
				+ "3: LIST \n"
				+ "4: MESSAGE \n"
				+ "5: LOGOUT \n"
				+ "6: EXIT \n")

			if opt == "1":
				username = input("username: ")
				password = input("password: ")
				s.send(bytes("#LOGIN#"+username+"#"+password+"#", "utf-8"))

			elif opt == "2":
				username = input("username: ")
				password = input("password: ")
				s.send(bytes("#REGISTER#"+username+"#"+password+"#", "utf-8"))

			elif opt == "3":
				s.send(bytes("#LIST#", "utf-8"))

			elif opt == "4":
				reciever = input("reciever: ")
				message = input("message: ")
				s.send(bytes("#MSG#"+reciever+"#"+message+"#", "utf-8"))

			elif opt == "5":
				s.send(bytes("#LOGOUT#", "utf-8"))

			elif opt == "6":
				break

		# if there is incomming message from the server, recieve it and print
		else:
				data = s.recv(1024)
				print("\n>>>", data.decode(), "\n")

s.close()
