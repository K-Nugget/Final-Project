import time
from socket import*
from http import server
from datetime import datetime

serverName = 'localhost'
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

print("Server is ready")

connectionSocket, addr = serverSocket.accept()

file = open("recivedImage.jpg", "wb")
image_chunk = connectionSocket.recv(2048)

 

while image_chunk:
    file.write(image_chunk)
    image_chunk = connectionSocket.recv(2048)
    print(datetime.now())
file.close()