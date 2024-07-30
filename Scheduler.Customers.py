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

SyncCustomers()
SyncCustomersDestinations()