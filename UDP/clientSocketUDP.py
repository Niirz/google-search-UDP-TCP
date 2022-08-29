from socket import *
import webbrowser

serverName = 'localhost' #localhost
serverPort = 12000

#Se crea el socket
clientSocket = socket(AF_INET,SOCK_DGRAM)

#Crea y envia la busqueda
message = input('Ingrese su busqueda de google: ')
clientSocket.sendto(message.encode(),(serverName, serverPort))

#Recibe respuesta del servidor
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

#Ejecuta la respuesta del servidor
webbrowser.open(modifiedMessage.decode(), new=0, autoraise=True)

clientSocket.close()
