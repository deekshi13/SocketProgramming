import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=12346
s.connect((host,port))
complete_info=''
while True:
    msg=s.recv(7)
    if len(msg)<=0:
        break
    complete_info=complete_info+msg.decode("utf-8")
print(complete_info)
s.close()