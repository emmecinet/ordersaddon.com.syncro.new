from classOrdersAddonSyncro import OrdersAddonSyncro
from classQuery import Query
from classUtility import Utility

fields = [
    'COT_PROGR', 
    'COT_CODICE_AGENTE', 
    'COT_CODICE_CLI',
]

sql = Query.builderQuery("SELECT","COX",fields,[],[],{'COT_PROGR':'DESC'})
data = Query.exQueryData(sql)

for d in data:
    print('COT_PROGR ' + str(d[0]))
    print('COT_CODICE_AGENTE ' + str(d[1]))
    print('COT_CODICE_CLI ' + str(d[2]))


