import socket
import time
Buttons = 0
UDP_IP = "10,1,15,243"
UDP_PORT = 5000
Address = (UDP_IP, UDP_PORT)

Client_Socket = socket.socket(socket.AF_INET,
                              socket.SOCK_DGRAM)
Client_Socket.settimeout(1)
Client_Socket.sendto(1, Address)
