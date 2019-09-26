from socket import *
serverName="127.0.0.1"
serverPort=12000
clientsocket=socket(AF_INET,SOCK_DGRAM)
sentence=input("enter the file name")
clientsocket.sendto(bytes(sentence,"utf-8"),(serverName,serverPort))
filecontents,serverAddress=clientsocket.recvfrom(2048)
print("from server",filecontents)
clientsocket.close()
