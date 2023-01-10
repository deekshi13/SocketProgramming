import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=12346
s.bind((host,port))
s.listen()
while True:
    client, address=s.accept()
    print(f"Got connection with {client}")
    client.send(bytes("thank you visiting MyHCL portal","utf-8"))
    client.close()