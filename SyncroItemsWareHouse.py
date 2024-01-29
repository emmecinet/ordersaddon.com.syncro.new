from ClassOrdersAddonSyncro import OrdersAddonSyncro
from ClassQuery import Query
from ClassUtility import Utility
from ClassFtp import Ftp
from ClassMail import Mail
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
        fieldOrder = {'ARZ_CODICE':'ASC'}
        fields = [
            'ARZ_CODICE', 
            'ARZ_ESISTENZA',
            'ARZ_ESISTENZA_UM',
            'ARZ_QTA_APERTURA',
            'ARZ_VAL_APERTURA',
            'ARZ_QTA_CHIUSURA',
            'ARZ_VAL_CHIUSURA',
            'ARZ_QTA_ENTRATE_VAL',
            'ARZ_VAL_ENTRATE_VAL',
            'ARZ_QTA_INIZIALE',
            'ARZ_QTA_ACQUISTI',
            'ARZ_QTA_RESI_CLIENTI',
            'ARZ_QTA_CARICHI_PROD',
            'ARZ_ENTRATE_VARIE',
            'ARZ_QTA_VENDITE',
            'ARZ_QTA_RESI_FORNITORI',
            'ARZ_QTA_SCARICHI_PROD',
            'ARZ_QTA_USCITE_VARIE',
            'ARZ_PRECEDENTE',
            'ARZ_PRECEDENTE_UM',
            'ARZ_FILLER',
            'ARZ_FILLER_RIS',
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
                'ARZ_CODICE': '',
                'ARZ_ESISTENZA': '',
                'ARZ_ESISTENZA_UM': '',
                'ARZ_QTA_APERTURA': '',
                'ARZ_VAL_APERTURA': '',
                'ARZ_QTA_CHIUSURA': '',
                'ARZ_VAL_CHIUSURA': '',
                'ARZ_QTA_ENTRATE_VAL': '',
                'ARZ_VAL_ENTRATE_VAL': '',
                'ARZ_QTA_INIZIALE': '',
                'ARZ_QTA_ACQUISTI': '',
                'ARZ_QTA_RESI_CLIENTI': '',
                'ARZ_QTA_CARICHI_PROD': '',
                'ARZ_ENTRATE_VARIE': '',
                'ARZ_QTA_VENDITE': '',
                'ARZ_QTA_RESI_FORNITORI': '',
                'ARZ_QTA_SCARICHI_PROD': '',
                'ARZ_QTA_USCITE_VARIE': '',
                'ARZ_PRECEDENTE': '',
                'ARZ_PRECEDENTE_UM': '',
                'ARZ_FILLER': '',
                'ARZ_FILLER_RIS': '',
            }
            
            data4json['ARZ_CODICE'] = d[0]
            data4json['ARZ_ESISTENZA'] = d[1]
            data4json['ARZ_ESISTENZA_UM'] = d[2]
            data4json['ARZ_QTA_APERTURA'] = d[3]
            data4json['ARZ_VAL_APERTURA'] = d[4]
            data4json['ARZ_QTA_CHIUSURA'] = d[5]
            data4json['ARZ_VAL_CHIUSURA'] = d[6]
            data4json['ARZ_QTA_ENTRATE_VAL'] = d[7]
            data4json['ARZ_VAL_ENTRATE_VAL'] = d[8]
            data4json['ARZ_QTA_INIZIALE'] = d[9]
            data4json['ARZ_QTA_ACQUISTI'] = d[10]
            data4json['ARZ_QTA_RESI_CLIENTI'] = d[11]
            data4json['ARZ_QTA_CARICHI_PROD'] = d[12]
            data4json['ARZ_ENTRATE_VARIE'] = d[13]
            data4json['ARZ_QTA_VENDITE'] = d[14]
            data4json['ARZ_QTA_RESI_FORNITORI'] = d[15]
            data4json['ARZ_QTA_SCARICHI_PROD'] = d[16]
            data4json['ARZ_QTA_USCITE_VARIE'] = d[17]
            data4json['ARZ_PRECEDENTE'] = d[18]
            data4json['ARZ_PRECEDENTE_UM'] = d[19]
            data4json['ARZ_FILLER'] = d[20]
            data4json['ARZ_FILLER_RIS'] = d[21]

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

SyncroItemsWareHouse.syncro()

controller = 'Items WareHouse'
with open('logs/Syncro.ItemsWareHouse.json') as f:
    lines = f.readlines()
messageObject = OrdersAddonSyncro.get_configuration().get("general", "app_customer") + ', Syncro ' + controller +' ' + str(datetime.now())
messageBody = str(datetime.now()) + '\n\nElaborazione: ' + controller + '\n\nJson:\n\n' + str(lines)
Mail.send(messageObject,messageBody)