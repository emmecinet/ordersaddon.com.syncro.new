from ClassOrdersAddonSyncro import OrdersAddonSyncro
from ClassQuery import Query
from ClassUtility import Utility
from ClassFtp import Ftp
from ClassMail import Mail
from datetime import datetime

import os
import json

urlApi = 'https://ps-uddistribuzione.ordersaddon.com/api/categories/?ws_key=3JK89WNB8LY82HZNX74S6CCA1C9NAVKG'
callApi = Utility.callApi(urlApi)

print(callApi)

fileXmlLog = callApi

with open('logs/categories.xml',"w") as f:
    f.write(fileXmlLog)



exit()

class SyncroCategories:

    def syncro():

        #vars
        log = ""
        config = OrdersAddonSyncro.get_configuration()
        fileController = 'wsCategories.php'
        controller = "Categories"
        nameFileJson = 'Syncro.Categories.json'
        table = "TBLCM"
        fieldOrder = {'TBLCM_DESCRIZIONE1':'ASC'}
        fields = [
            'TBLCM_CODICE2', 
            'TBLCM_DESCRIZIONE1',
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

SyncroCategories.syncro()

controller = 'Categories'
with open('logs/Syncro.Categories.json') as f:
    lines = f.readlines()
messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
Mail.send(messageObject,messageBody)