
import socket

TARGET_IP = "192.168.122.77"
TARGET_PORT = 5006

nama='informatika'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(nama.encode()),(TARGET_IP,TARGET_PORT))