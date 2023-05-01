from src.utils import *
import config

def help():
    print(
        "Command List:" 
        + "\n-update <server id 1> <server"
        + "\n-step"
        + "\n-packets"
        + "\n-display"
        + "\n-disable <server id>"
        + "\n-crash"  
    )
    print(config.var["primary"]["primaryNode"])
    print(config.var["servers"]["nodeList"])
    
def packets():
    packets = config.var["primary"]["packets"]
    print("------------------------------")
    print(f"Packets Recieved: {packets}")
    print("------------------------------")
    
    
def displayTable():
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