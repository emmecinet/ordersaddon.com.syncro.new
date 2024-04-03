from ClassOrdersAddonSyncro import OrdersAddonSyncro
from ClassMail import Mail
from datetime import datetime
from SyncroCategories import SyncroCategories
from SyncroSubCategories import SyncroSubCategories
from SyncroItems import SyncroItems
from SyncroItemsWareHouse import SyncroItemsWareHouse
from SyncroPriceLists import SyncroPriceLists
from SyncroCustomers import SyncroCustomers
from SyncroCustomersDestinations import SyncroCustomersDestinations
from SyncroSuppliers import SyncroSuppliers

import schedule
import time

#C:/Zucchetti.Ordersaddon.Curafarma.2.0/'
configPath = OrdersAddonSyncro.get_configuration_path()

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

def SyncItems():
    
    SyncroItems.syncro()

    controller = 'Items'
    with open(configPath+'logs/Syncro.'+controller+'.json') as f:
        lines = f.readlines()
    messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
    messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
    Mail.send(messageObject,messageBody)

def SyncItemsWarehouse():
    
    SyncroItemsWareHouse.syncro()

    controller = 'ItemsWareHouse'
    with open(configPath+'logs/Syncro.'+controller+'.json') as f:
        lines = f.readlines()
    messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
    messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
    Mail.send(messageObject,messageBody)

def SyncPriceLists():
    
    SyncroPriceLists.syncro()

    controller = 'PriceLists'
    with open(configPath+'logs/Syncro.'+controller+'.json') as f:
        lines = f.readlines()
    messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
    messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
    Mail.send(messageObject,messageBody)

def SyncCustomers():
    
    SyncroCustomers.syncro()

    controller = 'Customers'
    with open(configPath+'logs/Syncro.'+controller+'.json') as f:
        lines = f.readlines()
    messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
    messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
    Mail.send(messageObject,messageBody)

def SyncCustomersDestinations():
    
    SyncroCustomersDestinations.syncro()

    controller = 'CustomersDestinations'
    with open(configPath+'logs/Syncro.'+controller+'.json') as f:
        lines = f.readlines()
    messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
    messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
    Mail.send(messageObject,messageBody)

def SyncSuppliers():
    
    SyncroSuppliers.syncro()

    controller = 'Suppliers'
    with open(configPath+'logs/Syncro.'+controller+'.json') as f:
        lines = f.readlines()
    messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
    messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
    Mail.send(messageObject,messageBody)

schedule.every().day.at("19:00").do(SyncCategories)
schedule.every().day.at("19:00").do(SyncSubCategories)
schedule.every().day.at("19:05").do(SyncCustomers)
schedule.every().day.at("19:10").do(SyncCustomersDestinations)
schedule.every().day.at("19:15").do(SyncSuppliers)
schedule.every().day.at("19:20").do(SyncItems)
schedule.every().day.at("19:25").do(SyncItemsWarehouse)
schedule.every().day.at("19:30").do(SyncPriceLists)

while True:
    schedule.run_pending()
    time.sleep(1)
    