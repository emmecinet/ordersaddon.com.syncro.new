from classes.ClassOrdersAddonSyncro import OrdersAddonSyncro
from classes.ClassMail import Mail
from datetime import datetime
from classes.ClassSyncroSuppliers import SyncroSuppliers

import schedule
import time

configPath = OrdersAddonSyncro.get_configuration_path()

def SyncSuppliers():
    
    SyncroSuppliers.syncro()

    controller = 'Suppliers'
    with open(configPath+'logs/Syncro.'+controller+'.json') as f:
        lines = f.readlines()
    messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
    messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
    Mail.send(messageObject,messageBody)

SyncSuppliers()

#input("Press enter to exit;")
time.sleep(5)