from src.utils import *
from src.clientMessages import *
from src.readFiles import *
import config

def help():
    print(
        "Command List:" 
        + "\n-update <server id 1> <server id 2>"
        + "\n-step"
        + "\n-packets"
        + "\n-display"
        + "\n-disable <server id>"
        + "\n-crash"  
    )

def update(s1, s2, cost):
    primaryNode = config.var["primary"]["primaryNode"]
    if(str(primaryNode["id"]) == s1):
        if cost == "inf":
            primaryNode["cost"][s2]["pathCost"] = "inf"
            primaryNode["cost"][s2]["nextHop"] = "-"
        else:  
            primaryNode["cost"][s2]["pathCost"] = int(cost)
            primaryNode["cost"][s2]["nextHop"] = s2
        config.var["primary"]["primaryNode"] = primaryNode
        print(f"update SUCCESS")
    else:
        print("update: server id 1 must be the server you input this command on")

def step():
    readyToReceiveMessage()


def packets():
    packets = config.var["primary"]["packets"]
    print("------------------------------")
    print(f"Packets Recieved: {packets}")
    print("------------------------------")
    
    
def display():
    primaryNode = config.var["primary"]["primaryNode"]
    nodeList = config.var["servers"]["nodeList"]
    table = []
    table.append("Server ID    Next ID   Cost\n")
    primaryID = str(primaryNode["id"])
    table.append(f'   {primaryID}\t\t{primaryNode["cost"][primaryID]["nextHop"]}\t{primaryNode["cost"][primaryID]["pathCost"]}\n')
    for node in nodeList:
        id = str(node["id"])
        table.append(f'   {id}\t\t{primaryNode["cost"][id]["nextHop"]}\t{primaryNode["cost"][id]["pathCost"]}\n')
    print("".join(table))
    
def disable(id):
    primaryNode = config.var["primary"]["primaryNode"]
    neighbors = readInitialCosts(config.var["settings"]["filename"], config.var["settings"]["numServers"], config.var["settings"]["numEdges"], primaryNode)
    if neighbors[id] != "inf":
        primaryNode["cost"][id]["pathCost"] = "inf"
        primaryNode["cost"][id]["nextHop"] = "-"
        disableConnection(id)
    config.var["primary"]["primaryNode"] = primaryNode
    
        
def crash():
    primaryNode = config.var["primary"]["primaryNode"]
    neighbors = readInitialCosts(config.var["settings"]["filename"], config.var["settings"]["numServers"], config.var["settings"]["numEdges"], primaryNode)
    nodeList = config.var["servers"]["nodeList"]
    
    
    for node in nodeList:
        id = str(node["id"])
        if neighbors[id] != "inf":
            primaryNode["cost"][id]["pathCost"] = "inf"
            primaryNode["cost"][id]["nextHop"] = "-"
            disableConnection(id)    
        config.var["primary"]["primaryNode"] = primaryNode