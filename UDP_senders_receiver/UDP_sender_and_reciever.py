import socket
import threading
import time

dest_UDP_IP = "192.168.1.112" # IP of destination device
UDP_IP_from_sender = ""       # IP of UDP sender device (optional)
UDP_PORT = 5001
MESSAGE = b"Hello, World!!!"

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP_from_sender, UDP_PORT))
def receive():
    while True:
        sock.sendto(MESSAGE, (dest_UDP_IP, UDP_PORT))
        time.sleep(3)
        

        

def send():
    while True:
        data, addr = sock.recvfrom(128) # buffer size is 1024 bytes
        text = "received message: {} from: {}" .format(data.decode("ascii"), addr)
        print(text)


thread_1 = threading.Thread(target= send)
thread_1.start()
thread_2 = threading.Thread(target= receive)
thread_2.start()

