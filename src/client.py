#!env python3


#: PYChat Software, Client Script
#: Copyright Maulana B. (C) 2020-2021
#:
#: This Program is free software: you can redistribute it and/or modify
#: it under terms of the GNU General Public License as published by
#: Free Software Foundation , either version 3 of the License, or
#: (at your option) any later version
#:
#:
#: This program is distributed in the hope that it will be useful,
#: but WITHOUT ANY WARRANTY; without even the implied warranty of
#: MERCHANTIBILTY or FITNESS FOR A PARTICULAR PURPOSE.   See the
#: GNU General Public License for more details
#:
#: You should have received a copy of the GNU General Public License
#: along with this program. If not, see <https://www.gnu.org/licenses/>
#:
#:
#:          <Maintained Under>
#:   Maulana B. <https://github.com/DogeX86-64>

import socket

# Before oop
"""v = socket.socket()

ip = input("IP : ")
try:
    port = int(input("Empty, default : 5555 => "))
except ValueError:
    port = 5555
v.connect((ip,port))
while 1:
    xData = input("=> ")

    v.send(xData.encode())

    if xData == "end" or xData == "END":
        break
        v.close()
    print("+: => ",v.recv(1023).decode())"""
class client:
    def __init__(self,username,port,ip):
        self.username = username
        self.port = port
        self.ip = ip
    def online(self):
        x = socket.socket()
        x.connect((ip,port))

        print("Connected to {} , port : {} ".format(ip,port))
        self.receiveInfo(x)
    def receiveInfo(self,connection):
        global infodata
        infoData = connection.recv(1024).decode()
        print("Connected to : {} ".format(infoData))
        self.sendInfo(connection,infoData)
    def sendInfo(self,connection,sender):
        connection.send(self.username.encode())
        self.kirim(connection,sender)
        #infoData VARIABLE CANNOT GLOBALIZED
        #so, just pipe it on dirty way
        #receiveInfo() -> sendInfo() -> kirim() -> receive()
        # anjir lah
    def receive(self,a,o):
        while 1:
            receivedData = a.recv(2048).decode()
            print("{} => {}".format(o,receivedData))
            if receivedData == "end" or receivedData == "END":
                b.close()
                print("Connection with {} Ended".format(infoData))
                break
            self.kirim(a,o)
    def kirim(self,b,c):
        while 1:
            dataToSend = input("You => ")
            b.send(dataToSend.encode())
            self.receive(b,c)
def usernim():
    global usr
    try:
        usr = str(input("Username => "))
    except ValueError:
        print("Username must be not empty !")
        usernim()
try:
    port = int(input("Port (Default 5555)=> "))
except ValueError:
    port = 5555
def ip():
    try:
        global ip
        ip = input("IP Address => ")
    except ValueError:
        print("IP must be not empty !")
        ip()
usernim()
ip()
main = client(usr,port,ip)
main.online()
