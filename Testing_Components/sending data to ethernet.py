import socket

HOST = '192.168.1.177' # change the IP address to match your Arduino's IP address
PORT = 8888

data = "Hello, Arduino!"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(data.encode(), (HOST, PORT))
