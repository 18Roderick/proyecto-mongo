'use strict'
const mongoClient = require('mongodb').MongoClient,
	url = 'mongodb://localhost:27017/',
	dbName = 'GenomicDB',
	collectionName = 'Proteinas';
const request = require('request');
var link = `https://www.ebi.ac.uk/proteins/api/proteins?offset=0&size=5&organism=Nicotiana%20tabacum`
var options = {
	url: link,
	headers: {
		"Accept": "application/json"
	}
};

function gettingData(data) {

}

request(options, (error, response, body) => {
	let data = JSON.parse(body);
	let lista = []
	let dataset = {};
	data.forEach(element => {
		for (const i in element) {
			//console.log(element[i])
			if (i === 'protein') {
				for (const key in element[i]) {
					if (key === "submittedName") {
						dataset.CadenaDNA = element['sequence']['sequence'];
						//console.log(element[i][key]);
						if (typeof (element[i][key]) == 'array') {
							dataset.Organismo = element[i][key][0]['fullName']['value'];
							dataset.Funcion = element[i][key][0]['fullName']['evidences']['source']['url'];
							
						} else {
							console.log('Sumited name ############', element[i][key]);
						}
					} else if (key === "recommendedName") {
						//console.log(element[i][key]);
						dataset.Organismo = element[i][key]['fullName']['value'];
						dataset.Funcion = element['comments'][0]['text'][0]['value'];
						dataset.CadenaDNA = element['sequence']['sequence'];

					}
				}
			}
		};
		lista.push(dataset);
		//console.log(dataset)
	});
})