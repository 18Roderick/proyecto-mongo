'use strict'
const
	request = require('request'),
	mongoClient = require('mongodb').MongoClient,
	url = 'mongodb://localhost:27017/',
	dbName = 'GenomicDB',
	collectionName = 'Proteinas';


function dbConnection() {
	return new Promise((resolve, reject) => {
		return mongoClient.connect(url, (err, db) => {
			return (err) ? reject(new Error('Error al conectar con mongo')) : resolve(db);
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
			return (error) ? reject(new Error('problemas al consultar el api')) : resolve(JSON.parse(body));
		})
	})
}

function requestOptions(start = 0, size = 100) {
	let opciones = {
		url: `https://www.ebi.ac.uk/proteins/api/proteins?offset=${start}&size=${size}&organism=Botryococcus%20braunii`,
		headers: {
			"Accept": "application/json"
		}
	}
	return opciones;
}

function procces(data) {
	let lista = [];
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
						dataset.Organismo = element[i][key]['fullName']['value'];
						dataset.Funcion = element['comments'];
						dataset.CadenaDNA = element['sequence']['sequence'];



					}
				}
			}
		};
		lista.push(dataset);
		//console.log("Imprimiendo datset  \n\n", dataset)

	});

	return new Promise((resolve, reject) => {
		return (lista.length > 0) ? resolve(lista) : reject(new Error('Lista de proteinas vacia'))
	})
}


async function main(start = 400, size = 1) {
	try {

		const data = await gettingData(requestOptions(start, size));
		const registros = await procces(data);
		const database = await dbConnection();
		const execute = await dbInsertMany(database, registros);
		database.close();
		console.log(registros.length);
		setTimeout(() => {
			let tmpStart = start;
			start = size + tmpStart;
			console.log(start, size);
			main(start, size);
		}, 2000);

	} catch (error) {
		console.log("Mensaje de error ", error);
	}
}

main();

console.log(requestOptions());