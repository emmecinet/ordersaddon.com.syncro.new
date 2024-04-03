from ClassOrdersAddonSyncro import OrdersAddonSyncro
from ClassQuery import Query
from ClassUtility import Utility
from ClassFtp import Ftp
from ClassMail import Mail
from datetime import datetime

import os
import json

configPath = OrdersAddonSyncro.get_configuration_path()

class SyncroCustomersDestinations:

    def syncro():

        #vars
        config = OrdersAddonSyncro.get_configuration()
        fileController = 'wsCustomersDestinations.php'
        controller = "CustomersDestinations"
        nameFileJson = 'Syncro.CustomersDestinations.json'
        table = "DES"
        fieldOrder = {'DES_CONTO':'ASC'}
        fields = [
            'DES_TIPO', 
            'DES_CONTO', 
            'DES_FILIALE',
            'DES_DESCRIZIONE1',
            'DES_DESCRIZIONE2',
            'DES_VIA',
            'DES_CAP',
            'DES_CITTA',
            'DES_PROVINCIA',
        ]
        curDateTime = datetime.now()
        curDateTime = str(curDateTime.year) + "_" + str(curDateTime.month) + "_" + str(curDateTime.day)

        print("------------------------------------------------")
        print(datetime.now())
        print("Inizializzazione Sincronizzazione: " + controller.upper())

        #read and create data output
        sql = Query.builderQuery("SELECT",table,fields,[],[],fieldOrder)
        print("Esecuzione QUERY: " + sql)
        print("Lettura DATI...")

        data = Query.exQueryData(sql)
        dataJson = []

        for d in data:
            
            data4json = {
                'DES_TIPO':'',  
                'DES_CONTO':'', 
                'DES_FILIALE':'', 
                'DES_DESCRIZIONE1':'', 
                'DES_DESCRIZIONE2':'', 
                'DES_VIA':'', 
                'DES_CAP':'', 
                'DES_CITTA':'', 
                'DES_PROVINCIA':'', 
            }
            
            data4json['DES_TIPO'] = d[0]
            data4json['DES_CONTO'] = d[1]
            data4json['DES_FILIALE'] = d[2]
            data4json['DES_DESCRIZIONE1'] = d[3]
            data4json['DES_DESCRIZIONE2'] = d[4]
            data4json['DES_VIA'] = d[5]
            data4json['DES_CAP'] = d[6]
            data4json['DES_CITTA'] = d[7]
            data4json['DES_PROVINCIA'] = d[8]

            dataJson.append(data4json)

        #create json
        print("Creazione JSON...")
        fileJson = json.dumps(dataJson, indent=2)
        with open(configPath+'/temp/'+nameFileJson, "w") as outfile:
            outfile.write(fileJson)

        #upload fila FTP
        print("Upload file FTP...")
        Ftp.upload(configPath+'/temp/'+nameFileJson,'import/'+nameFileJson)
        Ftp.upload(configPath+'/temp/'+nameFileJson,'log/'+curDateTime+"_"+nameFileJson)

        #call api url 
        apiKey = config.get("api", "api_key")
        urlApi = config.get("api", "api_url")+fileController+"?apiKey="+apiKey+"&controller="+controller+""
        print("Chiamata API: " + urlApi + '...')
        callApi = Utility.callApi(urlApi)
        #print(callApi)
        fileJsonLog = callApi
        #now = str(datetime.now().year)+'_'+str(datetime.now().month)+'_'+str(datetime.now().day)+'_'+str(datetime.now().hour)+'_'+str(datetime.now().minute)+'_'+str(datetime.now().second)
        with open(configPath+'/logs/'+nameFileJson, "w") as f:
            f.write(fileJsonLog)

        #delete tmp file
        print("Pulizia e rimozione file...")
        os.remove(configPath+'/temp/'+nameFileJson)

        print("Procedura di sicronizzazione completata!")
        print(datetime.now())
        print("------------------------------------------------")
