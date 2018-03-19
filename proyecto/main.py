import requests
import sys
from connection import Mongo
connection = Mongo('GenomicDB')

collection = {
    'Organismo': '',
    'Funcion': '',
    'CadenaDNA': ''
}

index = 0
start = 0
size = 1


def links(start=0, size=1, index=0):
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
    return urls[index]


def getting_data(data):
    for index in data:
        for clave in index:
        	print(clave)


try:
    while index < 1:
        url = links(start, size, 0)
        print(url)
        r = requests.get(url, headers={"Accept": "application/json"})

        if not r.ok:
            r.raise_for_status()
            sys.exit()
        responseBody = r.json()
        #print(responseBody)
        getting_data(responseBody)
        index += 1


except:
    'Erro al tratar de conseguir los datos'
