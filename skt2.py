import socket
k=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
k.connect(("Ashfak",80))
while True:
    msg1=input("CLIENT :")
    k.send(msg1.encode())
    msg2=k.recv(1024)
    print("SERVER :",msg2.decode())
    if msg1==None or len(msg1)==0:
        break
k.close()
