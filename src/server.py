#!env python3



import socket,signal,sys

def handler(signum,frame):
    signal.signal(signum,signal.SIG_IGN)
    print("ctrl + c Pressed")
    raise KeyboardInterrupt
    sys.exit(0)
#signal.signal(signal.SIGINT,handler) kinda sus, bit skeptical
class server:
    def __init__(self,port,ipaddr,username):
        self.port = port
        self.ipaddr = ipaddr
        self.username = username
    def xstart(self):
        #hst = a.get()
        x = socket.socket()

        x.bind(('',self.port))
        x.listen(10)
        print("Server started, listening for any connection")
        z, addr = x.accept()

        print("Server Connected with client")
        self.sendInfo(z)
    def receive(self,k,p):
        while 1:
            rData = k.recv(1024).decode()
            print(p + " => " + rData)
            if rData == "end" or rData == "END":
                break;
                k.close()
            self.kirim(k,p)
    def kirim(self,i,sender):
        while 1:
            sData = input("You => ")

            if sData == "end" or sData == "END":
                i.close()
                break;
                print("Connection Ended With : ",sender)
            i.send(sData.encode())
            self.receive(i,sender)
    def sendInfo(self,connection):
        connection.send(self.username.encode())
        self.receiveInfo(connection)
    def receiveInfo(self,connection):
        global infoData
        infoData = connection.recv(1024).decode()
        print("Connected with : " + infoData)
        self.receive(connection,infoData)


try:
    port = int(input("Port (Default 5555) => "))
except ValueError:
    port = 5555

main = server(int(port),'0.0.0.0',"server1")
main.xstart()
