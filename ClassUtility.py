import requests
import json

class Utility:

    def callApiBk(url):
        r = requests.get(url)
        #'http://echo.jsontest.com/key/value/one/two'
        #cprint(r.text) # contenuto della risposta HTTP
        #print(r.json) # oggetto JSON
        #print(r.status_code) # codice di status
        #print(r.headers) # informazione contenuta negli headers della risposta
        #print(r.history) # informazioni sui reindirizzamenti
        result = json.loads(r.text)
        return result
    

    def callApi(url):
        r = requests.get(url)
        return r.text

    
    