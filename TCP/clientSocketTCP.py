from socket import *
import webbrowser

serverName = 'localhost'
serverPort = 12001

#Se crea el socket de cliente
clientSocket = socket(AF_INET, SOCK_STREAM)

#Se inicia la conexion en tres fases con el servidor
clientSocket.connect((serverName, serverPort))
message = input('Ingrese su busqueda de google: ')

#Se envia la busqueda al socket de servidor
clientSocket.send(message.encode())

#Se recibe el resultado de la busqueda desde el socket del servidor
modifiedMessage = clientSocket.recv(1024)

#Se decodifica el mensaje y se ejecuta la respuesta obtenida
webbrowser.open(modifiedMessage.decode(), new=0, autoraise=True)

#Se cierra el socket de cliente
clientSocket.close()