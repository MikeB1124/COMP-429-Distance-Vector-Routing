import threading
import time
from src.utils import *
from src.clientMessages import *
import config

def runIntervalUpdates():
    while config.var["primary"]["primaryNode"]["enabled"]:
        interval = config.var["settings"]["interval"]
        time.sleep(interval)
        readyToReceiveMessage()
        print("\nPeriodic updates sent")
        