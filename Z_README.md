# ordersaddon.com.syncro.new

#install reference

pip install --upgrade pip
python.exe -m pip install --upgrade pip

pip install wheel
pip install pyodbc
pip install requests
pip install schedule
pip install pyinstaller

pyinstaller Scheduler.py --onefile

pyinstaller SyncroCategories.py --onefile
pyinstaller SyncroSubCategories.py --onefile
pyinstaller SyncroCustomers.py --onefile
pyinstaller SyncroCustomersDestinations.py --onefile
pyinstaller SyncroItems.py --onefile
pyinstaller SyncroItemsWareHouse.py --onefile
pyinstaller SyncroPriceLists.py --onefile
pyinstaller SyncroSuppliers.py --onefile

#Note

