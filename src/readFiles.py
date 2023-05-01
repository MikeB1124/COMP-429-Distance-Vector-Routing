from src.utils import *

def readNumServersAndEdges(filename):
    servers = 0
    edges = 0
    with open(filename) as file:
        for i, line in enumerate(file):
            if i == 0:
                servers = int(line)
            elif i == 1:
                edges = int(line)
    return {"servers": servers, "edges": edges}

def readPrimaryNodeID(filename, servers):
    primaryID = 0
    with open(filename) as file:
        for i, line in enumerate(file):
            if i >= 2 + servers:
                line = line[:len(line) - 1]
                splitString = line.split(" ")
                primaryID = int(splitString[0])
    return primaryID

def readAllServersInTopology(filename, servers, primaryID):
    primary = {}
    nodeList = []
    with open(filename) as file:    
        for i, line in enumerate(file):
            if i >= 2 and i < 2 + servers:
                line = line[:len(line) - 1]
                splitString = line.split(" ")
                
                if int(splitString[0]) == primaryID:
                    primary = {
                        "id": int(splitString[0]), 
                        "ip": splitString[1], 
                        "port": int(splitString[2]),
                        "enabled": True,
                        "cost": {}
                    }
                else:
                    nodeList.append({
                        "id": int(splitString[0]), 
                        "ip": splitString[1], 
                        "port": int(splitString[2]),
                        "enabled": False,
                    })
    return {"nodeList": nodeList, "primary": primary}

def readInitialCosts(filename, servers, edges, primaryNode):
    costMap = {str(primaryNode["id"]): {"pathCost": 0, "nextHop": str(primaryNode["id"])}}
    
    for i in range(1, servers + 1):
        if str(primaryNode["id"]) != str(i):
            costMap[str(i)] = {"pathCost": "inf", "nextHop": "-"}
    
    with open(filename) as file:
        for i, line in enumerate(file):
            if i >= 2 + servers and i < 2 + servers + edges:
                line = line[:len(line) - 1]
                splitString = line.split(" ")
                id = splitString[1]
                costMap[str(splitString[1])] = {"pathCost": int(splitString[2]), "nextHop": str(splitString[1])}
    return costMap