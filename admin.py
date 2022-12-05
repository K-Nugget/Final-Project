from socket import*
import sys
import time
import os
import numpy
from http import server

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)


file = open('img.jpg', 'rb')
image_data = file.read(2048)

def menu():
    print("[1] Send Image")
    print("[2] Send JSON")
    print("[3] Send CSV")
    print("[0] Exit Program")


menu()
option = int(input("Enter your Option: "))

while option != 0:
    if option == 1:
        clientSocket.connect((serverName, serverPort))
        while image_data:
            clientSocket.send(image_data)
            image_data = file.read(2048)
        file.close()
        clientSocket.close()
        print("Image Sent")
    elif option == 2:
        #send JSON
        print("Sending JSON")
    elif option == 3:
        #send CSV
        print("Sending CSV")
    else:
        print("Invalid Option")
   

    print()
    menu()
    option = int(input("Enter your Option: "))


clientSocket.close()
print("Exiting Program")