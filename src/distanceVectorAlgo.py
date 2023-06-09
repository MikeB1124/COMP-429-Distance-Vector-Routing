import config

def checkForRoutingTableUpdates(serverID, routingTable):
    primaryNode = config.var["primary"]["primaryNode"]
    for i in range(1, config.var["settings"]["numServers"] + 1):
        if primaryNode["cost"][serverID]["pathCost"] != "inf":
            destination = str(i)
            toNeighbor = int(primaryNode["cost"][serverID]["pathCost"])
            if destination != str(primaryNode["id"]) and destination != serverID and primaryNode["cost"][destination]["pathCost"] == "inf" and routingTable[destination]["pathCost"] != "inf":
                primaryNode["cost"][destination]["pathCost"] = toNeighbor + int(routingTable[destination]["pathCost"])
                primaryNode["cost"][destination]["nextHop"] = serverID
            elif destination != str(primaryNode["id"]) and destination != serverID and routingTable[destination]["pathCost"] != "inf": 
                if(int(primaryNode["cost"][destination]["pathCost"]) > toNeighbor + int(routingTable[destination]["pathCost"])):
                    primaryNode["cost"][destination]["pathCost"] = toNeighbor + int(routingTable[destination]["pathCost"])
                    primaryNode["cost"][destination]["nextHop"] = serverID
            
            config.var["primary"]["primaryNode"] = primaryNode  