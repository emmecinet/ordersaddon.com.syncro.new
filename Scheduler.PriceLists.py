from classes.ClassOrdersAddonSyncro import OrdersAddonSyncro
from classes.ClassMail import Mail
from datetime import datetime
from classes.ClassSyncroPriceLists import SyncroPriceLists

import schedule
import time

#C:/Zucchetti.Ordersaddon.UDDistribuzione.2.0/'
configPath = OrdersAddonSyncro.get_configuration_path()

def SyncPriceLists():
    
    SyncroPriceLists.syncro()

    controller = 'PriceLists'
    with open(configPath+'logs/Syncro.'+controller+'.json') as f:
        lines = f.readlines()
    messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
    messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
    Mail.send(messageObject,messageBody)

SyncPriceLists()

#input("Press enter to exit;")
time.sleep(5)