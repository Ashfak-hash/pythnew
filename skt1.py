import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostname=socket.gethostname()
print(hostname)
try:
    s.bind((hostname,80))
except:
    print("FAILED TO BIND")
else:
    print(hostname,"BINDED SUCCESSFULLY")
    s.listen(10)
    c,ad=s.accept()
    while True:
        msg1=c.recv(1024)
        print("CLIENT : ",msg1.decode())
        msg2=input("SERVER : ")
        if msg2==None or len(msg2)==0:
            break
        c.send(msg2.encode())
s.close()
