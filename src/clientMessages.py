from src.utils import *
import socket
import config

def readyToReceiveMessage():
    primaryNode = config.var["primary"]["primaryNode"]
    nodeList = config.var["servers"]["nodeList"]
    
    for node in nodeList:
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