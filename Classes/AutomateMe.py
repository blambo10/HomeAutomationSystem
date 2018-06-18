#!/usr/bin/env python
import configparser
import platform
import os
from Classes.Network import Network

class AutomateMe:

    def __init__(self):
        #Defining "Constants" if you can call a mutable variable that ... sigh.
        CONST_CONFIG = "hasagent.configa"
        CONST_OS = platform.system()

        #Defining control commands
        if CONST_OS == "Windows":
            self.CONST_REBOOTCOMMAND = "shutdown -r -f"
            self.CONST_SHUTDOWNCOMMAND = "shutdown -s -f"
        elif CONST_OS == "Linux":
            self.CONST_REBOOTCOMMAND = "sync;shutdown -r now"
            self.CONST_SHUTDOWNCOMMAND = "sync;shutdown -h now"
        else:
            print("Operating Not Supported!")
            exit(2)

        #Loading Config Parameters from external config file.
        self.config = configparser.ConfigParser()
        networkparameters = self.loadconfig(CONST_CONFIG)

        #Create the network object with appropriate network
        #Data in the construct
        self.Listener = Network(*networkparameters)

    def loadconfig(self, configfile):
        try:
            #Parsing in config file
            if self.config.read(configfile):

                #for key in self.config["NETWORK"]:
                    #print(key + " : " + self.config["NETWORK"][key])

                if self.config["NETWORK"]["SocketIP"]:
                    ip = self.config["NETWORK"]["SocketIP"]

                if self.config["NETWORK"]["SocketPort"]:
                    port = self.config["NETWORK"]["SocketPort"]

                #Returning IP and Port extracted from config file
                #in tuple
                return ip, port
            else:
                ip = False
                port = 6060
                return ip, port
        except:
            return "",""

    def startagent(self):
        #print(self.Listener.listeningip + " : " + self.Listener.listeningport)
        self.Listener.startsocketlistener(self)

    def powercontroler(self, command):
        if str(command) == "reboot":
            os.system(self.CONST_REBOOTCOMMAND)
        elif str(command) == "shutdown":
            os.system(self.CONST_SHUTDOWNCOMMAND)

