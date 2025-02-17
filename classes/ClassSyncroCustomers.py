from ClassOrdersAddonSyncro import OrdersAddonSyncro
from ClassQuery import Query
from ClassUtility import Utility
from ClassFtp import Ftp
from ClassMail import Mail
from datetime import datetime

import os
import json

configPath = OrdersAddonSyncro.get_configuration_path()

class SyncroCustomers:

    def syncro():

        #vars
        config = OrdersAddonSyncro.get_configuration()
        fileController = 'wsCustomers.php'
        controller = "Customers"
        nameFileJson = 'Syncro.Customers.json'
        table = "CLI"
        fieldOrder = {'CLI_CODICE':'ASC'}
        fields = [
            'CLI_CODICE_AG', 
            'CLI_CODICE', 
            'CLI_DESCRIZIONE1',
            'CLI_DESCRIZIONE2',
            'CLI_VIA',
            'CLI_CAP',
            'CLI_CITTA',
            'CLI_PROVINCIA',
            'CLI_TELEFONO',
            'CLI_FAX',
            'CLI_E_MAIL',
            'CLI_CODICE_LI',
            'CLI_PARTITA_IVA',
            'CLI_CODICE_FISCALE',
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
                'CLI_CODICE_AG':'', 
                'CLI_CODICE':'', 
                'CLI_DESCRIZIONE1':'',
                'CLI_DESCRIZIONE2':'',
                'CLI_VIA':'',
                'CLI_CAP':'',
                'CLI_CITTA':'',
                'CLI_PROVINCIA':'',
                'CLI_TELEFONO':'',
                'CLI_FAX':'',
                'CLI_E_MAIL':'',
                'CLI_CODICE_LI':'',
                'CLI_PARTITA_IVA':'',
                'CLI_CODICE_FISCALE':'',
            }
            
            data4json['CLI_CODICE_AG'] = d[0]
            data4json['CLI_CODICE'] = d[1]
            data4json['CLI_DESCRIZIONE1'] = d[2]
            data4json['CLI_DESCRIZIONE2'] = d[3]
            data4json['CLI_VIA'] = d[4]
            data4json['CLI_CAP'] = d[5]
            data4json['CLI_CITTA'] = d[6]
            data4json['CLI_PROVINCIA'] = d[7]
            data4json['CLI_TELEFONO'] = d[8]
            data4json['CLI_FAX'] = d[9]
            data4json['CLI_E_MAIL'] = d[10]
            data4json['CLI_CODICE_LI'] = d[11]
            data4json['CLI_PARTITA_IVA'] = d[12]
            data4json['CLI_CODICE_FISCALE'] = d[13]

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
