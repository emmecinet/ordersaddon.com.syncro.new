from ClassOrdersAddonSyncro import OrdersAddonSyncro
from ClassQuery import Query
from ClassUtility import Utility
from ClassFtp import Ftp
from datetime import datetime

import os
import json

class SyncroPriceList:

    def syncro():

        #vars
        config = OrdersAddonSyncro.get_configuration()
        fileController = 'wsPriceLists.php'
        controller = "PriceLists"
        nameFileJson = 'Syncro.PriceLists.json'
        table = "LIS"
        fieldOrder = {'LIS_CODICE_ART':'ASC'}
        fields = [
            'LIS_CODICE_ART', 
            'LIS_CODICE_LI',
            'LIS_PREZZO_01',
            'LIS_AA',
            'LIS_MM',
            'LIS_GG',
            'LIS_DATA_FINE_VLD',
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
                'LIS_CODICE_ART': '',
                'LIS_CODICE_LI': '',
                'LIS_PREZZO_01': '',
                'LIS_AA': '',
                'LIS_MM': '',
                'LIS_GG': '',
                'LIS_DATA_FINE_VLD': '',
            }

            data4json['LIS_CODICE_ART'] = d[0]
            data4json['LIS_CODICE_LI'] = d[1]
            data4json['LIS_PREZZO_01'] = d[2]
            data4json['LIS_AA'] = d[3]
            data4json['LIS_MM'] = d[4]
            data4json['LIS_GG'] = d[5]
            data4json['LIS_DATA_FINE_VLD'] = ''

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
        #print(callApi)
        fileJsonLog = callApi
        #now = str(datetime.now().year)+'_'+str(datetime.now().month)+'_'+str(datetime.now().day)+'_'+str(datetime.now().hour)+'_'+str(datetime.now().minute)+'_'+str(datetime.now().second)
        with open('logs/'+nameFileJson, "w") as f:
            f.write(fileJsonLog)

        #delete tmp file
        print("Pulizia e rimozione file...")
        os.remove('temp/'+nameFileJson)

        print("Procedura di sicronizzazione completata!")
        print(datetime.now())
        print("------------------------------------------------")

SyncroPriceList.syncro()