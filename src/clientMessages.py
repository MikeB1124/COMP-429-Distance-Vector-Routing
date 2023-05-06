from src.utils import *
import socket
import config

def readyToReceiveMessage():
    primaryNode = config.var["primary"]["primaryNode"]
    nodeList = config.var["servers"]["nodeList"]
    for node in nodeList:
        if node["enabled"] == True or node["enabled"] == 0:
            try:
                id = str(node["id"])
                if primaryNode["cost"][id]["pathCost"] != "inf":
                    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    clientSocket.connect((node["ip"], int(node["port"])))
                    message = f'Ready:{primaryNode["id"]}:{primaryNode["ip"]}:{primaryNode["port"]}:Ready for packets'
                    clientSocket.send(message.encode())
                    
                    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    clientSocket.connect((node["ip"], int(node["port"])))
                    message = f'RoutingTable|{primaryNode["id"]}|{primaryNode["ip"]}|{primaryNode["port"]}|{primaryNode["cost"]}'
                    clientSocket.send(message.encode())
            except:
                continue
        

def disableConnection(id):
    primaryNode = config.var["primary"]["primaryNode"]
    nodeList = config.var["servers"]["nodeList"]
    ip = ""
    port = 0
    for node in nodeList:
        if node["id"] == int(id):
            ip = node["ip"]
            port = node["port"]
            node["enabled"] = False
            
    primaryNode["cost"][id]["pathCost"] = "inf"
    primaryNode["cost"][id]["nextHop"] = "-"
    config.var["primary"]["primaryNode"] = primaryNode
    config.var["servers"]["nodeList"] = nodeList
    if ip != "":
        try:
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect((ip, int(port)))
            message = f'Disable:{primaryNode["id"]}:{primaryNode["ip"]}:{primaryNode["port"]}:Disable connection'
            clientSocket.send(message.encode())
        except:
            print(f'Server {id} not connected.')