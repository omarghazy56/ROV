import socket

# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Binding server port(1234) with host(pass host name or ip incase of external server)
s.bind((socket.gethostname(), 1234))
s.listen(5)
while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Hello, I'am Ghazy <3","utf-8"))
    clientsocket.close()
