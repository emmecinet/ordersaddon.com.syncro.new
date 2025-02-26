from OrdersAddonSyncro import OrdersAddonSyncro
from ClassMail import Mail
from datetime import datetime
from SyncroCategories import SyncroCategories
from SyncroSubCategories import SyncroSubCategories

import schedule
import time

configPath = OrdersAddonSyncro.get_configuration().get("general", "app_path")

def SyncCategories():
    
    SyncroCategories.syncro()

    controller = 'Categories'
    with open(configPath+'logs/Syncro.'+controller+'.json') as f:
        lines = f.readlines()
    messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
    messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
    Mail.send(messageObject,messageBody)

def SyncSubCategories():
    
    SyncroSubCategories.syncro()

    controller = 'SubCategories'
    with open(configPath+'logs/Syncro.'+controller+'.json') as f:
        lines = f.readlines()
    messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
    messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
    Mail.send(messageObject,messageBody)

SyncCategories()
SyncSubCategories()

#input("Press enter to exit;")
time.sleep(5)