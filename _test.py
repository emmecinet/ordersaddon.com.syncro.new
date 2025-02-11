import requests

urlApi = "https://api.i-quadra.com/curafarma/wsCustomers.php?apiKey=7268fa26-fc8e-4ead-97c0-819517bcd1c7&controller=Customers"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
}

page = requests.get(urlApi, headers=headers)

print(page.text)
