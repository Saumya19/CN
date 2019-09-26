from socket import *
serverName="127.0.0.1"
serverPort=12000
serversocket=socket(AF_INET,SOCK_DGRAM)
serversocket.bind(("127.0.0.1",serverPort))
print("the server is ready to recieve")
while 1:
    sentence,clientAddress=serversocket.recvfrom(2048)
    file=open(sentence,"r")
    l=file.read(2048)
    serversocket.sendto(bytes(l,"utf-8"),clientAddress)
    print("send to client");
file.close()
