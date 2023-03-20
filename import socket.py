import socket
import bluetooth
HOST = 'localhost'
PORT = 5000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f'Server listening on {HOST}:{PORT}')
client_socket, addr = server_socket.accept()
print(f'Connected by {addr}')
data = client_socket.recv(1024)
print(f'Received: {data.decode()}')
response = 'Hello from Python'
client_socket.sendall(response.encode())
target_name=response.encode()
target_address = None
nearby_devices = bluetooth.discover_devices()
for bdaddr in nearby_devices:
        if target_name == bluetooth.lookup_name( bdaddr ):
         target_address = bdaddr
         break

if target_address is not None:
       print("found target bluetooth device with address ", target_address)
else:
       print ("could not find target bluetooth device nearby")

client_socket.close()
