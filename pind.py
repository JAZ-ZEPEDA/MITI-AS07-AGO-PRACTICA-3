import socket
import sys
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 8182)
print('starting up on {} port {}'.format(*server_address))
try:
  sock.bind(server_address)
except (socket.error , msg):
  print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
  sys.exit()

print('Socket bind complete')


# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(60)
            # print('received {!r}'.format(data))
            if data:
                stud_obj = json.loads(data)
                print('Mensaje recibido ' + stud_obj["saludo"] + " " +str(stud_obj["secuencia"]))
                stud_obj["tipo"] = 1
                json_string = json.dumps(stud_obj)
                connection.sendall(str.encode(json_string))
            else:
                print('no data from', client_address)
                break
    except (socket.error , msg):
        print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])

    finally:
        # Clean up the connection
        connection.close()