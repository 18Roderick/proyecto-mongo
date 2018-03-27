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


function dbInsertMany(db, dato) {
	var dbo = db.db(dbName);
	dbo.collection(collectionName).insertMany(dato, (err, res) => {
		if (err) throw err;
		console.log('Documentos insertados ' + res.insertedCount);
		db.close();
	});
}

function gettingData(options){
	return new Promise( (resolve, reject ) => {
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


console.log(requestOptions());
(
	async function() {
		console.log('Temporizador corriendo ');
		try{
			dbConnection()
			 	.then(db => {
			  		console.log('conexion exitosa');
			  		db.close()
			  	})
			gettingData(requestOptions(0, 2))
				.then( data => {
					console.log(data)
				})

		}catch(error){
			console.log(error);
		}
	}

());
