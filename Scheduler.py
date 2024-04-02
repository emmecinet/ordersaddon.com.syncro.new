from ClassOrdersAddonSyncro import OrdersAddonSyncro
from ClassMail import Mail
from datetime import datetime
from SyncroItems import SyncroItems
from SyncroItemsWareHouse import SyncroItemsWareHouse
from SyncroPriceLists import SyncroPriceList

import schedule
import time

def SyncItems():
    
    SyncroItems.syncro()

    controller = 'Items'
    with open('logs/Syncro.Items.json') as f:
        lines = f.readlines()
    messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
    messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
    Mail.send(messageObject,messageBody)

    print("Syncro Items")

def SyncItemsWareHouse():

    SyncroItemsWareHouse.syncro()

    controller = 'ItemsWareHouse'
    with open('logs/Syncro.ItemsWareHouse.json') as f:
        lines = f.readlines()
    messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
    messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
    Mail.send(messageObject,messageBody)

def SyncPriceList():

    SyncroPriceList.syncro()

    controller = 'PriceLists'
    with open('logs/Syncro.PriceLists.json') as f:
        lines = f.readlines()
    messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
    messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
    Mail.send(messageObject,messageBody)

schedule.every().hour.at(":00").do(SyncItems)
#schedule.every().hour.at(":10").do(SyncItemsWareHouse)
schedule.every().hour.at(":20").do(SyncPriceList)

while True:
    schedule.run_pending()
    time.sleep(1)
    