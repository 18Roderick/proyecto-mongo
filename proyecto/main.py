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

def links(start=0, size=1, index):
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


url = links(10, 0)




try:
	while index < len(urls):
		r = requests.get(url, headers={"Accept": "application/json"})

		if not r.ok:
		    r.raise_for_status()
		    sys.exit()
		responseBody = r.json()
		

except:
	'Erro al tratar de conseguir los datos'