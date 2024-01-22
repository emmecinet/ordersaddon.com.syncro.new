from ClassOrdersAddonSyncro import OrdersAddonSyncro
from ClassQuery import Query
from ClassUtility import Utility
from ClassFtp import Ftp
from datetime import datetime

import os
import json

class SyncroSuppliers:

    def syncro():

        #vars
        config = OrdersAddonSyncro.get_configuration()
        fileController = 'wsSuppliers.php'
        controller = "Suppliers"
        nameFileJson = 'Syncro.Suppliers.json'
        table = "FRN"
        fieldOrder = {'FRN_CODICE':'ASC'}
        fields = [
            'FRN_CODICE', 
            'FRN_DESCRIZIONE1',
            'FRN_DESCRIZIONE2',
            'FRN_VIA',
            'FRN_CAP',
            'FRN_CITTA',
            'FRN_PROVINCIA',
            'FRN_TELEFONO',
            'FRN_FAX',
            'FRN_E_MAIL',
            'FRN_PARTITA_IVA',
            'FRN_CODICE_FISCALE',
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
                'FRN_CODICE':'', 
                'FRN_DESCRIZIONE1':'',
                'FRN_DESCRIZIONE2':'',
                'FRN_VIA':'',
                'FRN_CAP':'',
                'FRN_CITTA':'',
                'FRN_PROVINCIA':'',
                'FRN_TELEFONO':'',
                'FRN_FAX':'',
                'FRN_E_MAIL':'',
                'FRN_PARTITA_IVA':'',
                'FRN_CODICE_FISCALE':'',
            }
            
            data4json['FRN_CODICE'] = d[0]
            data4json['FRN_DESCRIZIONE1'] = d[1]
            data4json['FRN_DESCRIZIONE2'] = d[2]
            data4json['FRN_VIA'] = d[3]
            data4json['FRN_CAP'] = d[4]
            data4json['FRN_CITTA'] = d[5]
            data4json['FRN_PROVINCIA'] = d[6]
            data4json['FRN_TELEFONO'] = d[7]
            data4json['FRN_FAX'] = d[8]
            data4json['FRN_E_MAIL'] = d[9]
            data4json['FRN_PARTITA_IVA'] = d[10]
            data4json['FRN_CODICE_FISCALE'] = d[11]

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

SyncroSuppliers.syncro()