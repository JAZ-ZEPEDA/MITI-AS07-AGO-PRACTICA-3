import socket
import sys
import json


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


stud_obj = json.loads('{ "saludo": "' + "Hola" + '","tipo":0,"secuencia": ' + str(0) + '}')
# Connect the socket to the port where the server is listening
print('¿Cual es la ip?')
ip = str(input())
print('¿Cual es el puerto?')
puerto = int(input())
server_address = (ip, puerto)

print('¿Cual es el mensaje?')
message = str(input())

print('¿Cantidad de mensajes?')
cantidad = int(input())

print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    for num in range(0, cantidad, 1):
        m = str.encode('{ "saludo": "' + message + '","tipo":0,"secuencia": ' + str(num) + '}')
        print('sending {!r}'.format(m))
        sock.send(m)
        data = sock.recv(60)
        stud_obj = json.loads(data)
        print("tipo: " + str(stud_obj["tipo"]) + " secuencia " + str(stud_obj["secuencia"]))

        


finally:
    print('closing socket')
    sock.close()