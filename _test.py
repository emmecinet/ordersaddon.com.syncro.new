
from OrdersAddonSyncro import OrdersAddonSyncro
from ClassFtp import Ftp

config = OrdersAddonSyncro.get_configuration()
configPath = "D:/Sviluppo/i-quadra.syncro.new/dist/"
nameFileJson = "test.txt"

Ftp.upload(configPath+'/temp/'+nameFileJson,'import/'+nameFileJson,config.get("ftp", "ftp_server"),config.get("ftp", "ftp_user"),config.get("ftp", "ftp_pass"))


input("Press enter to exit;")