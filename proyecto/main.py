import requests
import sys
from pymongo import MongoClient
from connection import Mongo
import json
connection = Mongo('GenomicDB')

collection = {
    'Organismo': '',
    'Funcion': '',
    'CadenaDNA': ''
}

index = 0
start = 0
size = 2
i = 0


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
	directorio = []
	for i, index in enumerate(data):
	# Extrae los datos por directorio
		for clave in index:
        	# filtrando los datos por clave de proteina
			if clave == 'protein':
				#print(clave)
				for protein in index[clave]:
					if protein == "submittedName":
						#print(protein+' nombre de la clave')
						collection['Organismo'] = index[clave][protein][0]['fullName']['value']
						collection['Funcion'] = index[clave][protein][0]['fullName']['evidences'][0]['source']['url']
						collection['CadenaDNA'] = index["sequence"]["sequence"]
						connection.insertone('Proteinas', collection)

					elif protein == "recommendedName":
						#print(protein+' nombre de la clave')
						collection['Organismo'] = index[clave][protein]['fullName']['value']
						collection['Funcion'] = index['comments'][0]['text'][0]["value"]
						collection['CadenaDNA'] = index["sequence"]["sequence"]
						connection.insertone('Proteinas', collection)

					#print(collection)
					directorio.append(collection)


		print(i)
	#print(directorio)
	

	
	

        



try:
    while index < 1:
        url = links(start, size, 0)
        print(url)
        r = requests.get(url, headers={"Accept": "application/json"})

        if not r.ok:
            r.raise_for_status()
            sys.exit()
        responseBody = r.json()
        # print(responseBody)
        getting_data(responseBody)
        index += 1


except:
    'Erro al tratar de conseguir los datos'
