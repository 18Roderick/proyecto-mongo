'use strict'
const
	request = require('request'),
	mongoClient = require('mongodb').MongoClient,
	url = 'mongodb://localhost:27017/',
	dbName = 'GenomicDB',
	collectionName = 'Proteinas';

let
	start = 0,
	size = 100;

function dbConnection() {
	return new Promise((resolve, reject) => {
		return mongoClient.connect(url, (err, db) => {
			return (err) ? reject(new error('Error al conectar con mongo')) : resolve(db);
		});
	});
};

function findeSome(db, dato) {
	var dbo = db.db(dbName);
	dbo.collection(collectionName).find(dato)
}

function dbInsert(db, dato) {
    var dbo = db.db(dbName);
    dbo.collection(collectionName).insertOne(dato, (err, res) => {
        if (err) throw err;
        console.log("documento insertado");
    });

}

function dbInsertMany(db, dato) {
	var dbo = db.db(dbName);
	dbo.collection(collectionName).insertMany(dato, (err, res) => {
		if (err) throw err;
		console.log('Documentos insertados ' + res.insertedCount);
		db.close();
	});
}

function gettingData(options) {
	return new Promise((resolve, reject) => {
		return request(options, (error, response, body) => {
			return (error) ? reject(new error('problemas al consultar el api')) : resolve(JSON.parse(body));
		})
	})
}

function requestOptions(start = 0, size = 100) {
	let opciones = {
		url: `https://www.ebi.ac.uk/proteins/api/proteins?offset=${start}&size=${size}&organism=Nicotiana%20tabacum`,
		headers: {
			"Accept": "application/json"
		}
	}
	return opciones;
}

function procces(data) {
	let lista = []

	data.forEach(element => {
		let dataset = {};
		for (const i in element) {
			//console.log(element[i])
			if (i === 'protein') {
				for (const key in element[i]) {
					if (key === "submittedName") {

						//console.log(element[i][key]);
						if (typeof(element[i][key]) == 'array') {
							dataset.Organismo = element[i][key][0]['fullName']['value'];
							dataset.Funcion = element[i][key][0]['fullName']['evidences']['source']['url'];

						} else {
							dataset.Organismo = element[i][key][0]['fullName']['value'];
							dataset.Funcion = element[i][key][0]['fullName']['evidences'][0]['source']['url'];
						}
						dataset.CadenaDNA = element['sequence']['sequence'];

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
		//console.log("Imprimiendo datset  \n\n", dataset)

	});

	return new Promise((resolve, reject) => {
		return (lista.length > 0) ? resolve(lista) : reject(new error('Lista de proteinas vacia'))
	})
}


async function main(start = 0, size = 1) {
	console.log('Temporizador corriendo ');
	try {

		const data = await gettingData(requestOptions(start, size));
		const registros = await procces(data);
		console.log(registros);
		setTimeout(() => {
			let tmpStart = start;
			start = size + tmpStart;
			console.log(start, size);
			//main()
		}, 10000);

	} catch (error) {
		console.log(error);
	}
}

main();

console.log(requestOptions());