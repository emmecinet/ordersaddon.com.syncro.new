from ClassOrdersAddonSyncro import OrdersAddonSyncro
from ClassQuery import Query
from ClassUtility import Utility
from ClassFtp import Ftp
from ClassMail import Mail
from datetime import datetime

import os
import json

class SyncroItems:

    def syncro():
        
        #vars
        config = OrdersAddonSyncro.get_configuration()
        fileController = 'wsItems.php'
        controller = "Items"
        nameFileJson = 'Syncro.Items.json'
        table = "ART"
        fieldOrder = {'ART_CODICE':'ASC'}
        fields = [
            'ART_CODICE', 
            'ART_CODICE_ALTERNATIVO', 
            'ART_DESCRIZIONE1', 
            'ART_DESCRIZIONE2', 
            'ART_CODICE_UM', 
            'ART_CODICE_UM1', 
            'ART_CONVERSIONE', 
            'ART_VOLUME', 
            'ART_CODICE_IV_VEN', 
            'ART_CODICE_CM', 
            'ART_CODICE_ME', 
            'ART_CODICE_IN', 
            'ART_CODICE_FRN', 
            'ART_LOTTO_VENDITA', 
            'ART_TBLSE_CODICE',
            'ART_IMPEGNATO',
            'ART_ORDINATO',
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
                'ART_CODICE': '',
                'ART_CODICE_ALTERNATIVO': '',
                'ART_DESCRIZIONE1': '',
                'ART_DESCRIZIONE2': '',
                'ART_CODICE_UM': '',
                'ART_CODICE_UM1': '',
                'ART_CONVERSIONE': '',
                'ART_VOLUME': '',
                'ART_CODICE_IV_VEN': '',
                'ART_CODICE_CM': '',
                'ART_CODICE_ME': '',
                'ART_CODICE_IN': '',
                'ART_CODICE_FRN': '',
                'ART_LOTTO_VENDITA': '',
                'ART_TBLSE_CODICE': '',
                'ART_IMPEGNATO': '',
                'ART_ORDINATO': ''
            }

            data4json['ART_CODICE'] = d[0]
            data4json['ART_CODICE_ALTERNATIVO'] = d[1]
            data4json['ART_DESCRIZIONE1'] = d[2]
            data4json['ART_DESCRIZIONE2'] = d[3]
            data4json['ART_CODICE_UM'] = d[4]
            data4json['ART_CODICE_UM1'] = d[5]
            data4json['ART_CONVERSIONE'] = d[6]
            data4json['ART_VOLUME'] = d[7]
            data4json['ART_CODICE_IV_VEN'] = d[8]
            data4json['ART_CODICE_CM'] = d[9]
            data4json['ART_CODICE_ME'] = d[10]
            data4json['ART_CODICE_IN'] = d[11]
            data4json['ART_CODICE_FRN'] = d[12]
            data4json['ART_LOTTO_VENDITA'] = d[13]
            data4json['ART_TBLSE_CODICE'] = d[14]
            data4json['ART_IMPEGNATO'] = d[15]
            data4json['ART_ORDINATO'] = d[16]

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

SyncroItems.syncro()

controller = 'Items'
with open('logs/Syncro.Items.json') as f:
    lines = f.readlines()
messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
Mail.send(messageObject,messageBody)