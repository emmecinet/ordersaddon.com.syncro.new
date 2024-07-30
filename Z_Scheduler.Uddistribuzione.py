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

#C:/Zucchetti.Ordersaddon.UDDistribuzione.2.0/'
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


schedule.every().day.at("08:00").do(SyncCategories)
schedule.every().day.at("08:00").do(SyncSubCategories)
schedule.every().day.at("08:00").do(SyncCustomers)
schedule.every().day.at("08:00").do(SyncCustomersDestinations)
schedule.every().day.at("08:00").do(SyncSuppliers)

schedule.every().day.at("14:00").do(SyncCategories)
schedule.every().day.at("14:00").do(SyncSubCategories)
schedule.every().day.at("14:00").do(SyncCustomers)
schedule.every().day.at("14:00").do(SyncCustomersDestinations)
schedule.every().day.at("14:00").do(SyncSuppliers)

schedule.every().day.at("08:05").do(SyncItems)
schedule.every().day.at("08:05").do(SyncItemsWarehouse)
schedule.every().day.at("08:05").do(SyncPriceLists)
schedule.every().day.at("08:35").do(SyncItems)
schedule.every().day.at("08:35").do(SyncItemsWarehouse)
schedule.every().day.at("08:35").do(SyncPriceLists)

schedule.every().day.at("09:05").do(SyncItems)
schedule.every().day.at("09:05").do(SyncItemsWarehouse)
schedule.every().day.at("09:05").do(SyncPriceLists)
schedule.every().day.at("09:35").do(SyncItems)
schedule.every().day.at("09:35").do(SyncItemsWarehouse)
schedule.every().day.at("09:35").do(SyncPriceLists)

schedule.every().day.at("10:05").do(SyncItems)
schedule.every().day.at("10:05").do(SyncItemsWarehouse)
schedule.every().day.at("10:05").do(SyncPriceLists)
schedule.every().day.at("10:35").do(SyncItems)
schedule.every().day.at("10:35").do(SyncItemsWarehouse)
schedule.every().day.at("10:35").do(SyncPriceLists)

schedule.every().day.at("11:05").do(SyncItems)
schedule.every().day.at("11:05").do(SyncItemsWarehouse)
schedule.every().day.at("11:05").do(SyncPriceLists)
schedule.every().day.at("11:35").do(SyncItems)
schedule.every().day.at("11:35").do(SyncItemsWarehouse)
schedule.every().day.at("11:35").do(SyncPriceLists)

schedule.every().day.at("12:05").do(SyncItems)
schedule.every().day.at("12:05").do(SyncItemsWarehouse)
schedule.every().day.at("12:05").do(SyncPriceLists)
schedule.every().day.at("12:35").do(SyncItems)
schedule.every().day.at("12:35").do(SyncItemsWarehouse)
schedule.every().day.at("12:35").do(SyncPriceLists)

schedule.every().day.at("13:05").do(SyncItems)
schedule.every().day.at("13:05").do(SyncItemsWarehouse)
schedule.every().day.at("13:05").do(SyncPriceLists)
schedule.every().day.at("13:35").do(SyncItems)
schedule.every().day.at("13:35").do(SyncItemsWarehouse)
schedule.every().day.at("13:35").do(SyncPriceLists)

schedule.every().day.at("14:05").do(SyncItems)
schedule.every().day.at("14:05").do(SyncItemsWarehouse)
schedule.every().day.at("14:05").do(SyncPriceLists)
schedule.every().day.at("14:35").do(SyncItems)
schedule.every().day.at("14:35").do(SyncItemsWarehouse)
schedule.every().day.at("14:35").do(SyncPriceLists)

schedule.every().day.at("15:05").do(SyncItems)
schedule.every().day.at("15:05").do(SyncItemsWarehouse)
schedule.every().day.at("15:05").do(SyncPriceLists)
schedule.every().day.at("15:35").do(SyncItems)
schedule.every().day.at("15:35").do(SyncItemsWarehouse)
schedule.every().day.at("15:35").do(SyncPriceLists)

schedule.every().day.at("16:05").do(SyncItems)
schedule.every().day.at("16:05").do(SyncItemsWarehouse)
schedule.every().day.at("16:05").do(SyncPriceLists)
schedule.every().day.at("16:35").do(SyncItems)
schedule.every().day.at("16:35").do(SyncItemsWarehouse)
schedule.every().day.at("16:35").do(SyncPriceLists)

schedule.every().day.at("17:05").do(SyncItems)
schedule.every().day.at("17:05").do(SyncItemsWarehouse)
schedule.every().day.at("17:05").do(SyncPriceLists)
schedule.every().day.at("17:35").do(SyncItems)
schedule.every().day.at("17:35").do(SyncItemsWarehouse)
schedule.every().day.at("17:35").do(SyncPriceLists)

schedule.every().day.at("18:05").do(SyncItems)
schedule.every().day.at("18:05").do(SyncItemsWarehouse)
schedule.every().day.at("18:05").do(SyncPriceLists)
schedule.every().day.at("18:35").do(SyncItems)
schedule.every().day.at("18:35").do(SyncItemsWarehouse)
schedule.every().day.at("18:35").do(SyncPriceLists)

schedule.every().day.at("19:05").do(SyncItems)
schedule.every().day.at("19:05").do(SyncItemsWarehouse)
schedule.every().day.at("19:05").do(SyncPriceLists)
schedule.every().day.at("19:35").do(SyncItems)
schedule.every().day.at("19:35").do(SyncItemsWarehouse)
schedule.every().day.at("19:35").do(SyncPriceLists)

schedule.every().day.at("20:30").do(SyncItems)
schedule.every().day.at("20:35").do(SyncItemsWarehouse)


while True:
    schedule.run_pending()
    time.sleep(1)
    