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
print("Inizializzazione Sincronizzazione: " + controller.upper())

#read and create data output
sql = Query.builderQuery("SELECT","TBLCM",fields,[],[],{'TBLCM_DESCRIZIONE1':'ASC'})
print("Esecuzione QUERY: " + sql)
print("Lettura DATI...")

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

#create json
print("Creazione JSON...")
fileJson = json.dumps(dataJson, indent=2)
with open('temp/'+nameFileJson, "w") as outfile:
    outfile.write(fileJson)

#upload fila FTP
print("Upload file FTP...")
Ftp.upload('temp/'+nameFileJson,'import/'+nameFileJson)

#call api url 
apiKey = config.get("api", "api_key")
urlApi = config.get("api", "api_url")+fileController+"?apiKey="+apiKey+"&controller="+controller+""
print("Chiamata API: " + urlApi + '...')
Utility.callApi(urlApi)

#delete tmp file
print("Pulizia e rimozione file...")
os.remove('temp/'+nameFileJson)

print("Procedura di sicronizzazione completata!")
print("------------------------------------------------")

