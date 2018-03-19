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

index = 0


try:
	while index < len(urls):
		
