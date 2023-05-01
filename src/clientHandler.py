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
        elif (clientInput == "display"):
            displayTable()
        elif (clientInput == "packets"):
            packets()
        else:
            if(clientInput != ""):
                print("Invalid option")
        # except Exception as e:
        #     print(e)
        #     print("Invalid input format please look at instructions on README file")