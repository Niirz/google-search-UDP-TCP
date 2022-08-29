from socket import *
from googlesearch import search

serverPort = 12001
#Se crea el socket
serverSocket = socket(AF_INET, SOCK_STREAM)

#Se le asigna el puerto
serverSocket.bind(('',serverPort))

#Deja el servidor a la escucha de solicitudes
serverSocket.listen(1)

print("El servidor esta listo para recibir")

while True:
    #Se acepta la conexion con el cliente y se crea un nuevo socket 
    connectionSocket, addr = serverSocket.accept()

    #Se recibe la busqueda del cliente
    message = connectionSocket.recv(1024)

    #Se realiza la busqueda proporcionada por el cliente
    for i in search(message.decode(), start=0, stop=1):
        busqueda = i

    #Se envia la busqueda codificada al cliente
    connectionSocket.send(busqueda.encode())

    #Se cierra el socket de conexion
    connectionSocket.close()

