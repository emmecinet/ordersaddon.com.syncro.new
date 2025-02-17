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

pyinstaller Scheduler.Categories.py --onefile
pyinstaller Scheduler.Customers.py --onefile
pyinstaller Scheduler.Items.py --onefile
pyinstaller Scheduler.ItemsWareHouse.py --onefile
pyinstaller Scheduler.PriceLists.py --onefile
pyinstaller Scheduler.Suppliers.py --onefile

