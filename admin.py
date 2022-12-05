from socket import*

# defines basic tcp
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

# reads the file and converts it into binary
file = open('img.jpg', 'rb')
image_data = file.read(2048)

#  prints the menu
def menu():
    print("[1] Send Image")
    print("[2] Send JSON")
    print("[3] Send CSV")
    print("[0] Exit Program")


menu()
option = int(input("Enter your Option: ")) # to decide what to send

while option != 0:
    if option == 1:
        clientSocket.connect((serverName, serverPort)) # connects to the server
        while image_data: # while the image is being sent
            clientSocket.send(image_data) # sends the image data
            image_data = file.read(2048)
        file.close() # stops reading the original image
        clientSocket.close() # closes the connection to the receiving client
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


print("Exiting Program")