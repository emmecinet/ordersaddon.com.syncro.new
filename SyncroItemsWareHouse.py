from ClassOrdersAddonSyncro import OrdersAddonSyncro
from ClassQuery import Query
from ClassUtility import Utility
from ClassFtp import Ftp
from datetime import datetime

import os
import json

class SyncroItemsWareHouse:

    def syncro():

        #vars
        config = OrdersAddonSyncro.get_configuration()
        fileController = 'wsItemsWareHouse.php'
        controller = "ItemsWareHouse"
        nameFileJson = 'Syncro.ItemsWareHouse.json'
        table = "ARZ"
        fields = [
            'ARZ_CODICE_ART', 
        ]
        curDateTime = datetime.now()
        curDateTime = str(curDateTime.year) + "_" + str(curDateTime.month) + "_" + str(curDateTime.day)

        print("------------------------------------------------")
        print(datetime.now())
        print("Inizializzazione Sincronizzazione: " + controller.upper())

        #read and create data output
        sql = Query.builderQuery("SELECT",table,fields,[],[],{'ARZ_CODICE_ART':'ASC'})
        print("Esecuzione QUERY: " + sql)
        print("Lettura DATI...")

        data = Query.exQueryData(sql)
        dataJson = []

        for d in data:
            
            data4json = {
                'ARZ_CODICE_ART': '',
            }

            data4json['ARZ_CODICE_ART'] = d[0]

            dataJson.append(data4json)

        #create json
        print("Creazione JSON...")
        fileJson = json.dumps(dataJson, indent=2)
        with open('temp/'+nameFileJson, "w") as outfile:
            outfile.write(fileJson)

        #upload fila FTP
        print("Upload file FTP...")
        Ftp.upload('temp/'+nameFileJson,'import/'+nameFileJson)
        Ftp.upload('temp/'+nameFileJson,'log/'+curDateTime+"_"+nameFileJson)

        #call api url 
        apiKey = config.get("api", "api_key")
        urlApi = config.get("api", "api_url")+fileController+"?apiKey="+apiKey+"&controller="+controller+""
        print("Chiamata API: " + urlApi + '...')
        callApi = Utility.callApi(urlApi)
        print(callApi)

        #delete tmp file
        print("Pulizia e rimozione file...")
        os.remove('temp/'+nameFileJson)

        print("Procedura di sicronizzazione completata!")
        print(datetime.now())
        print("------------------------------------------------")

SyncroItemsWareHouse.syncro()