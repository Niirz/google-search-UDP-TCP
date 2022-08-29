from socket import *
from googlesearch import search


serverPort = 12000

#Se crea el socket
serverSocket = socket(AF_INET,SOCK_DGRAM, 0)

#Se le asigna el puerto al socket
serverSocket.bind(('',serverPort))

print("El Servidor esta listo para recibir")

#Queda en un bucle esperando consultas
while True:
    #Se recibe la busqueda porporcionada por el cliente
    message, clientAddress = serverSocket.recvfrom(2048)

    #Se realiza la busqueda en google
    for i in search(message.decode(), start=0, stop=1):
        busqueda = i
    #Se envia el resultado de la busqueda al cliente
    serverSocket.sendto(busqueda.encode(),clientAddress)


