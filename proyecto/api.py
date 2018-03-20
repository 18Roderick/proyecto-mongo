import requests
import sys
from connection import Mongo
connection = Mongo('GenomicDB')
urls = []

collection = {
    'Organismo': '',
    'Funcion': '',
    'CadenaDNA': ''
}


def links(start=0, size=1):
    urls = [
        "https://www.ebi.ac.uk/proteins/api/proteins?offset=" +
        str(start)+"&size="+str(size)+"&organism=Nicotiana%20tabacum",
        "https://www.ebi.ac.uk/proteins/api/proteins?offset=" +
        str(start)+"&size="+str(size)+"&organism=Escherichia%20coli",
        "https://www.ebi.ac.uk/proteins/api/proteins?offset=" +
        str(start)+"&size="+str(size)+"&organism=Cannabis%20sativa",
        "https://www.ebi.ac.uk/proteins/api/proteins?offset=" +
        str(start)+"&size="+str(size)+"&organism=Botryococcus%20braunii"
    ]
    return urls


url = links(0,100)
r = requests.get(url[0], headers={"Accept": "application/json"})

if not r.ok:
    r.raise_for_status()
    sys.exit()

responseBody = r.json()
#print(responseBody[0])

for protein in responseBody[0]['protein']:
    if protein == "submittedName":
        print(protein+' nombre de la clave')
        collection['Organismo'] = responseBody[0]['protein'][protein][0]['fullName']['value']
        collection['Funcion'] = responseBody[0]['protein'][protein][0]['fullName']['evidences'][0]['source']['url']
        collection['CadenaDNA'] = responseBody[0]["sequence"]["sequence"]
        connection.insertone('Proteinas', collection)
        print(collection)
    elif protein == "recommendedName":
    	print(protein+' nombre de la clave')
    	collection['Organismo'] = responseBody[0]['protein'][protein]['fullName']['value']
    	collection['Funcion'] = responseBody[0]['comments'][0]['text'][0]["value"]
    	collection['CadenaDNA'] = responseBody[0]['sequence']['sequence']
    	connection.insertone('Proteinas', collection)
    	print(collection)

# "submittedName"
