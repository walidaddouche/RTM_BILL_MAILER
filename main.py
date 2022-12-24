import requests
from rtm_client import *


client = RtmClient()

client.login()

bills = client.get_all_bills()

url = client.get_bill_By_Id(bills[0]["PK_VENTES"])


response = requests.get(url)

print(response.content)

with open('mon_fichier.pdf', 'wb') as f:
    # Écrivez du contenu binaire dans le fichier
    f.write(bytes(response.content))
    # Fermez le fichier
    f.close()
