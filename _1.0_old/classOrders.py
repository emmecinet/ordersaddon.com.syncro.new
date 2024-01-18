from classOrdersAddonSyncro import OrdersAddonSyncro
from classQuery import Query
from classUtility import Utility

class Orders:

    api_key = OrdersAddonSyncro.get_configuration().get("api", "api_key")
    file_controller = "_dev_wsOrders"
    controller = "Orders"
    url_api = OrdersAddonSyncro.get_configuration().get("api", "api_url")+file_controller+".php?apiKey="+api_key+"&controller="+controller+""

    def __init__(self):
        print("init...")

    def get():
        
        json = Utility.callApi(Orders.url_api)
        result = ""

        for data in json:
            head = data['head']
            COT_PROGR = Query.exQueryData("SELECT MAX(COT_PROGR+1) AS COT_PROGR FROM COX")[0]
            
            fields = [
                'COT_PROGR', 
                'COT_CODICE_AGENTE', 
                'COT_CODICE_CLI', 
                'AACOMM', 
                'MMCOMM', 
                'GGCOMM', 
                'AACONS', 
                'MMCONS', 
                'GGCONS', 
                'COT_ULTIMA_RIGA', 
                'COT_CODICE_MA',
                'COT_TIPO_ORDINE', 
                'COT_NATURA_ORDINE', 
                'COT_CODICE_DES', 
            ]

            values = [
                str(COT_PROGR),
                str(head.get('COT_CODICE_AGENTE')),
                str(head.get('COT_CODICE_CLI')),
                str(head.get('AACOMM')),
                str(head.get('MMCOMM')),
                str(head.get('GGCOMM')),
                str(head.get('AACONS')),
                str(head.get('MMCONS')),
                str(head.get('GGCONS')),
                str(head.get('COT_ULTIMA_RIGA')),
                str(head.get('COT_CODICE_MA')),
                str(head.get('COT_TIPO_ORDINE')),
                str(head.get('COT_NATURA_ORDINE')),
                str(head.get('COT_CODICE_DES')),
            ]

            sql = Query.builderQuery("INSERT","COX",fields,values)
            if(Query.exQueryNonData(sql)):
                #print(sql+"\n")
                rows = data['rows']
                for r in rows:
                    
                    fields = [
                        'COR_PROGR', 
                        'COR_RIGA', 
                        'COR_CODICE_ART', 
                        'COR_DESCRIZIONE1', 
                        'COR_QUANTITA', 
                        'COR_PREZZO', 
                        'COR_CODICE_UM', 
                        'COR_QUANTITA_UM', 
                        'COR_PREZZO_UM', 
                        'COR_COLLI', 
                        'COR_EVASO', 
                        'COR_PEZZI', 
                        'COR_FILLER', 
                    ]

                    values = [
                        str(head.get('COR_PROGR')),
                        str(head.get('COR_RIGA')),
                        str(head.get('COR_CODICE_ART')),
                        str(head.get('COR_DESCRIZIONE1')),
                        str(head.get('COR_QUANTITA')),
                        str(head.get('COR_PREZZO')),
                        str(head.get('COR_CODICE_UM')),
                        str(head.get('COR_QUANTITA_UM')),
                        str(head.get('COR_PREZZO_UM')),
                        str(head.get('COR_COLLI')),
                        str(head.get('COR_EVASO')),
                        str(head.get('COR_PEZZI')),
                        str(head.get('COR_FILLER')),
                    ]

                    sql = Query.builderQuery("INSERT","COR",fields,values)  
                    #print("[R] "+sql+"\n")
                    Query.exQueryNonData(sql)
                
            result += "Importazione ORDINE WEB #"+str(int(COT_PROGR))+"\n"

        return result

