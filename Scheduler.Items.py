from OrdersAddonSyncro import OrdersAddonSyncro
from ClassMail import Mail
from datetime import datetime
from SyncroItems import SyncroItems

import schedule
import time

configPath = OrdersAddonSyncro.get_configuration().get("general", "app_path")

def SyncItems():
    
    SyncroItems.syncro()

    controller = 'Items'
    with open(configPath+'logs/Syncro.'+controller+'.json') as f:
        lines = f.readlines()
    messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
    messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
    Mail.send(messageObject,messageBody)

SyncItems()

#input("Press enter to exit;")
time.sleep(5)