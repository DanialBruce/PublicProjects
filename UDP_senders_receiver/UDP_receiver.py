import socket

UDP_IP = ""
UDP_PORT = 5001

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(128) # buffer size is 1024 bytes
    info_text = "received message: {} from: {}" .format(data.decode("ascii"), addr)
    print(info_text)