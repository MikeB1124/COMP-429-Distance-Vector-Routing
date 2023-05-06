from src.utils import *
from src.commands import *
import socket
import config
import json
from src.distanceVectorAlgo import *

def runServer():
    primaryNode = config.var["primary"]["primaryNode"]
    nodeList = config.var["servers"]["nodeList"]
    # try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', int(primaryNode["port"])))
    serverSocket.listen(1)
    while True:
        connectionSocket, addr = serverSocket.accept()
        message = connectionSocket.recv(1024).decode()
        if not "RoutingTable" in message:
            action = message.split(":")[0]
            id = message.split(":")[1]
            ip = message.split(":")[2]
            port = message.split(":")[3]
            messageBody = message.split(":")[4]
        else:
            action = message.split("|")[0]
            id = message.split("|")[1]
            ip = message.split("|")[2]
            port = message.split("|")[3]
            messageBody = message.split("|")[4]
            
        if action == "Ready":
            for node in nodeList:
                if node["id"] == int(id):
                    node["enabled"] = True
            config.var["servers"]["nodeList"] = nodeList
        if action == "RoutingTable":
            jsonFormatMessageBody = messageBody.replace("'", '"')
            routingTable = json.loads(jsonFormatMessageBody)
            checkForRoutingTableUpdates(id, routingTable)
            print(f'Received a message from server {id}')
            config.var["primary"]["packets"] = config.var["primary"]["packets"] + 1
        if action == "Disable":
            primaryNode["cost"][id]["pathCost"] = "inf"
            primaryNode["cost"][id]["nextHop"] = "-"
            nodeList = config.var["servers"]["nodeList"]
            
            for node in nodeList:
                if node["id"] == int(id):
                    node["enabled"] = False
            
            config.var["primary"]["primaryNode"] = primaryNode
            config.var["servers"]["nodeList"] = nodeList
        connectionSocket.close()
    # except:
    #     print("\n\nServer unable to receive messages")
