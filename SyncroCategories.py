from ClassOrdersAddonSyncro import OrdersAddonSyncro
from ClassQuery import Query
from ClassUtility import Utility
from ClassFtp import Ftp

import os
import json

#vars
config = OrdersAddonSyncro.get_configuration()
fileController = 'wsCategories.php'
controller = "Categories"
nameFileJson = 'Syncro.Categories.json'
fields = [
    'TBLCM_CODICE2', 
    'TBLCM_DESCRIZIONE1',
]

print("------------------------------------------------")
print("Inizializzazione sincronizzazione: " + controller)

#read and create data output
sql = Query.builderQuery("SELECT","TBLCM",fields,[],[],{'TBLCM_DESCRIZIONE1':'ASC'})
data = Query.exQueryData(sql)
dataJson = []

for d in data:
    
    data4json = {
        'TBLCM_CODICE2': '',
        'TBLCM_DESCRIZIONE1': ''
    }

    data4json['TBLCM_CODICE2'] = d[0]
    data4json['TBLCM_DESCRIZIONE1'] = d[1]

    dataJson.append(data4json)

print("Esecuzione Query: " + sql)
print("Lettura dati...")

#create json
fileJson = json.dumps(dataJson, indent=2)
with open('temp/'+nameFileJson, "w") as outfile:
    outfile.write(fileJson)

print("Creazione Json...")

#upload fila FTP
Ftp.upload('temp/'+nameFileJson,'import/'+nameFileJson)

print("Upload fie su FTP...")

#call api url 
apiKey = config.get("api", "api_key")
urlApi = config.get("api", "api_url")+fileController+"?apiKey="+apiKey+"&controller="+controller+""

Utility.callApi(urlApi)

print("Chiamata API... " + urlApi)

#delete tmp file
os.remove('temp/'+nameFileJson)

print("Pulizia e rimozione file...")

print("Procedura di sicronizzazione completata!")
print("------------------------------------------------")

