from OrdersAddonSyncro import OrdersAddonSyncro
from ClassQuery import Query
from ClassUtility import Utility
from ClassFtp import Ftp
from ClassMail import Mail
from datetime import datetime

import os
import json

configPath = OrdersAddonSyncro.get_configuration().get("general", "app_path")

class SyncroSubCategories:

    def syncro():

        #vars
        config = OrdersAddonSyncro.get_configuration()
        fileController = 'wsSubCategories.php'
        controller = "SubCategories"
        nameFileJson = 'Syncro.SubCategories.json'
        table = "TBLME"
        fieldOrder = {'TBLME_DESCRIZIONE1':'ASC'}
        fields = [
            'TBLME_CODICE2', 
            'TBLME_DESCRIZIONE1',
            'TBLME_DESCRIZIONE2',
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
                'TBLME_CODICE2': '',
                'TBLME_DESCRIZIONE1': '',
                'TBLME_DESCRIZIONE2': ''
            }

            data4json['TBLME_CODICE2'] = d[0]
            data4json['TBLME_DESCRIZIONE1'] = d[1]
            data4json['TBLME_DESCRIZIONE2'] = d[2]

            dataJson.append(data4json)

        #create json
        print("Creazione JSON...")
        fileJson = json.dumps(dataJson, indent=2)
        with open(configPath+'/temp/'+nameFileJson, "w") as outfile:
            outfile.write(fileJson)

        #upload fila FTP
        print("Upload file FTP...")
        Ftp.upload(configPath+'/temp/'+nameFileJson,'import/'+nameFileJson,config.get("ftp", "ftp_server"),config.get("ftp", "ftp_user"),config.get("ftp", "ftp_pass"))
        
        #call api url 
        #apiKey = config.get("api", "api_key")
        #urlApi = config.get("api", "api_url")+fileController+"?apiKey="+apiKey+"&controller="+controller+""
        #print("Chiamata API: " + urlApi + '...')
        #callApi = Utility.callApi(urlApi)
        #print(callApi)
        #fileJsonLog = callApi
        #now = str(datetime.now().year)+'_'+str(datetime.now().month)+'_'+str(datetime.now().day)+'_'+str(datetime.now().hour)+'_'+str(datetime.now().minute)+'_'+str(datetime.now().second)
        #with open(configPath+'/logs/'+nameFileJson, "w") as f:
        #    f.write(fileJsonLog)

        #delete tmp file
        print("Pulizia e rimozione file...")
        os.remove(configPath+'/temp/'+nameFileJson)

        print("Procedura di sicronizzazione completata!")
        print(datetime.now())
        print("------------------------------------------------")

