import requests, sys
from connection import Mongo 
connection = Mongo()
urls = [
	"https://www.ebi.ac.uk/proteins/api/proteins?offset=6&size=1&organism=Nicotiana%20tabacum",
	'https://www.ebi.ac.uk/proteins/api/proteins?offset=0&size=2&organism=Escherichia%20coli',
	'https://www.ebi.ac.uk/proteins/api/proteins?offset=0&size=2&organism=Cannabis%20sativa',
	'https://www.ebi.ac.uk/proteins/api/proteins?offset=0&size=2&organism=Botryococcus%20braunii'
]

collection = {
	'Organismo': '',
	'Funcion' : '',
	'CadenaDNA'
}

r = requests.get(urls[0], headers={ "Accept" : "application/json"})

if not r.ok:
	r.raise_for_status()
	sys.exit()

responseBody = r.json()
print(responseBody[0])

for protein in responseBody[0]['protein']:
	if protein == "submittedName":
		print(protein+' nombre de la clave')
		print(responseBody[0]['protein'][protein][0]['fullName']['value'])
	elif protein == "recommendedName":
		print(protein+' nombre de la clave')
		collection['Organismo'] = responseBody[0]['protein'][protein]['fullName']['value']
		print('funcion de la proteina ')

# "submittedName"