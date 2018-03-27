const mongoClient = require('mongodb').MongoClient;
const urlDefault = () => {
    return 'mongodb://localhost:27017/'
};

class Mongo {
    constructor(url = urlDefault(), dbname = 'default') {
        this.dbname = dbname;
        this.url = url;
    }

    async dbConnection() {
        return new Promise((resolve, reject) => {
            return mongoClient.connect(this.url, (err, db) => {
                return (err) ? reject(new error('Error al conectar con mongo')) : resolve(db);
            });
        });
    };

    async dbInsert(collection, dato) {
        var dbo = db.db(this.dbName);
        dbo.collection(collection).insertOne(dato, (err, res) => {
            if (err) throw err;
            console.log("documento insertado");
        });

    }

    async dbInsertMany(db, dato) {
        var dbo = db.db(dbName);
        dbo.collection(collectionName).insertMany(dato, function(err, res) {
            if (err) throw err;
            console.log('Documentos insertados ' + res.insertedCount);
            db.close();
        });
    }



}



module.exports = Mongo