import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=12346
s.connect((host,port))
print(s.recv(7).decode("utf-8"))
#print(s.recv(1024))