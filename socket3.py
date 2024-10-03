import socket
k=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
k.connect(("Ashfak",80))
while True:
    mm=input("CLIENT :")
    k.send(mm.encode())
    mm2=k.recv(1024)
    print("SERVER :",mm2.decode())
    im mm==None or len(mm)==0:
        break
k.close()
    
