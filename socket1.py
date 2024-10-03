import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostname = socket.gethostname()
print(hostname)
try:
    s.bind((hostname,80))
except:
    print("Unable to Connect")
else:
    print(hostname,"NETWORK IS BINDED")
    s.listen(10)
    c,add = s.accept()
    while True:
        msg1=c.recv(1024)
        print("CLIENT: ",msg1.decode())
        m=input("SERVER: ")
        if m==None or len(m)==0:
            break
        c.send(m.encode())
    s.close()
