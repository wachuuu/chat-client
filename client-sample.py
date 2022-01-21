import socket

HOST="127.0.0.1"
PORT=1100

# niech klient działa w pętli
# na początku przeczytać dane z konsoli
# wysłać je i odebrać
# jeżeli input z konsoli =="exit" wyjść z pętli i zakończyć połączenie

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        opt=input(
        "1: LOGIN \n"
        +"2: REGISTER \n"
        +"3: LIST \n"
        +"4: MESSAGE \n"
        +"5: REFRESH \n"
        +"6: LOGOUT \n")

        if opt=="1":
          username=input("username: ")
          password=input("password: ")
          s.send(bytes("#LOGIN#"+username+"#"+password+"#","utf-8"))
          data=s.recv(1024)
          print("\n>>>",data.decode(),"\n")
          
        elif opt=="2":
          username=input("username: ")
          password=input("password: ")
          s.send(bytes("#REGISTER#"+username+"#"+password+"#","utf-8"))
          data=s.recv(1024)
          print("\n>>>",data.decode(),"\n")

        elif opt=="3":
          s.send(bytes("#LIST#","utf-8"))
          data=s.recv(1024)
          print("\n>>>",data.decode(),"\n")

        elif opt=="4":
          reciever=input("reciever: ")
          message=input("message: ")
          s.send(bytes("#MSG#"+reciever+"#"+message+"#","utf-8"))

        elif opt=="5":
          data=s.recv(1024)
          print("\n>>>",data.decode(),"\n")

        elif opt=="6":
          s.send(bytes("#LOGOUT#","utf-8"))
          data=s.recv(1024)
          print("\n>>>",data.decode(),"\n")

        elif opt =="exit":
          break

    s.close()
