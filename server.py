import socket;

HOST = "192.168.99.62"
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
        print(result)
        try:
            client.send("okay".encode())
        except:
            print("client closed software")
            break
    command = input("Do you exit [Y/n]>")
    if(command.lower() == "y"):
        server.close()
        break
