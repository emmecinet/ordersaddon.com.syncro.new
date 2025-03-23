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

pyinstaller Scheduler.Categories.py -F --onefile
pyinstaller Scheduler.Customers.py -F --onefile
pyinstaller Scheduler.Items.py -F --onefile
pyinstaller Scheduler.ItemsWareHouse.py -F --onefile
pyinstaller Scheduler.PriceLists.py -F --onefile
pyinstaller Scheduler.Suppliers.py -F --onefile

