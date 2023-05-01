from src.utils import *
from src.readFiles import *
from src.updateTimer import *
from src.clientHandler import *
from src.serverHandler import *
import os
import signal
import threading
import config

def main():
    #Get user input for topology file and update interval
    print("ENTER THE FOLLOWING COMMAND TO START\n(server -t topology_file -i seconds)")
    commandInput = input(">")
    parsedInput = parseStartUpCommand(commandInput)
    filename = parsedInput["filename"]
    interval = parsedInput["interval"]
    
    
    #Check if user inputed file exists
    if not os.path.isfile(filename):
        print(f'Topology File Does Not Exits: {filename}')
        exit()
    
    #Get number of servers in this topology and number of edges for a particular server
    topologyInfo = readNumServersAndEdges(filename)
    numServers = topologyInfo["servers"]
    numEdges = topologyInfo["edges"]
    
    #Get primary node ID
    primaryID = readPrimaryNodeID(filename, numServers)
                     
    #Get all server information and store it locally   
    nodeInfo = readAllServersInTopology(filename, numServers, primaryID)
    nodeList = nodeInfo["nodeList"]
    primaryNode = nodeInfo["primary"]
    
    #Initialize primary node costs to other servers
    primaryNode["cost"] = readInitialCosts(filename, numServers, numEdges, primaryNode)
    
    #Set global application configuration
    config.var["settings"]["filename"] = filename
    config.var["settings"]["interval"] = interval
    config.var["settings"]["numServers"] = numServers
    config.var["settings"]["numEdges"] = numEdges
    config.var["servers"]["nodeList"] = nodeList
    config.var["primary"]["primaryNode"] = primaryNode
    
    #Start periodic updates based off user interval input
    threading.Thread(target=runServer, daemon=True).start()
    threading.Thread(target=runIntervalUpdates, daemon=True).start()
    runClient()
    

main()