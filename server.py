import socket;

HOST = "[Your IP Address]"
PORT = 4444 # Your PORT

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((HOST,PORT))
server.listen(1)
client,addr = server.accept()
print("[+] Connected")
while True:
    result = client.recv(1024).decode()
    print(result)
    client.send("okay".encode())
