from src.utils import *
from src.commands import *
import config


def runClient():
    primaryPort = config.var["primary"]["primaryNode"]["port"]
    while True and checkServerPort(primaryPort):
        clientInput = input("Type command option or enter help to see options: ")
        # try:
        if(clientInput == "help"):
            help()
        elif (clientInput.split(" ")[0] == "update"):
            s1 = clientInput.split(" ")[1]
            s2 = clientInput.split(" ")[2]
            cost = clientInput.split(" ")[3]
            update(s1, s2, cost)
        elif (clientInput == "packets"):
            packets()
            print(f"{clientInput} SUCCESS")
        elif(clientInput == "step"):
            step()
            print(f"{clientInput} SUCCESS")
        elif (clientInput == "display"):
            display()
            print(f"{clientInput} SUCCESS")
        elif (clientInput.split(" ")[0] == "disable"):
            id = clientInput.split(" ")[1]
            disableConnection(id)
            print(f"{clientInput} SUCCESS")
        elif (clientInput == "crash"):
            crash()
            print(f"{clientInput} SUCCESS")
            exit()
        else:
            if(clientInput != ""):
                print(f"{clientInput}: not a valid command")
        # except Exception as e:
        #     print(e)
        #     print("Invalid input format please look at instructions on README file")