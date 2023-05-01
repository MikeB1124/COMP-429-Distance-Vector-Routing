import json

def parseStartUpCommand(command):
    filename = ""
    interval = ""
    args = command.split(" ")
    
    for i, arg in enumerate(args):
        if arg == "-t":
            filename = args[i + 1]
        elif arg == "-i":
            interval = args[i + 1]
    
    return {"filename": filename, "interval": int(interval)}

def checkServerPort(port):
    if int(port) > 1024:
        return True
    return False
            