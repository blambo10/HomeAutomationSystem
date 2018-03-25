import platform
import socket
import ipaddress
from socket import error as socket_error

# Network Class
#
# Author: Bryce Lamborne
# Purpose is to provide an Network Object that
# Contains all appropriate Network Functions
# As Methods.
#
# Including but not limited to a listener.
class Network:

    def __init__(self, IP, Port):
        self.__listeningIP = None
        self.__listeningPort = None
        self.listeningip = IP
        self.listeningport = Port

    # Validation Methods
    def validateIPv4(self, IPAddress):
        try:
            socket.inet_aton(IPAddress)
            return True
        except:
            return False

    #Defining Properties
    @property
    def listeningip(self):
        return self.__listeningIP

    @listeningip.setter
    def listeningip(self, value):
        if self.validateIPv4(value):
            self.__listeningIP = value
            return True
        else:
            return False

    @property
    def listeningport(self):
        return self.__listeningPort

    @listeningport.setter
    def listeningport(self, value):
        self.__listeningPort = value

    #Lets Get this party started
    def startsocketlistener(self, feedhandler):
        try:
            print("Listening on: " + self.listeningip + ":" + self.listeningport)
            print("OS: " + platform.system())

            #Creating Socket for Windows
            #binding to socket
            #listening on socket
            HomeAutomationSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            HomeAutomationSocket.bind((self.listeningip, int(self.listeningport)))
            HomeAutomationSocket.listen(5)

            #Recieving Data Stream From Socket
            while 1:
                c, address = HomeAutomationSocket.accept()
                data = c.recv(2048)

                #send data back to feed handler
                #to operate appropriate logic dependant pon payload
                feedhandler.powercontroler(data.decode('utf-8'))

            return True
        except:
            raise socket_error
            print("Error with socket")
            return False