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
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        }
        r = requests.get(url,headers=headers)
        return r.text
    
    def callApiDebug(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        }
        r = requests.get(url,headers=headers)
        return r

    
    