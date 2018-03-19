from pymongo import MongoClient


class Mongo:
    """docstring for ClassName"""

    def __init__(self, dbname, host=27017):
        self.connection = ''
        self.dbname = dbname
        self.host = host
        self.db = ''
        self.collection = ''

    def open_connection(self):
        try:
            self.connection = MongoClient('localhost', self.host)
            self.db = self.connection[self.dbname]
            print('Coneccion exitosa')
        except:
            print('Error al conectar con mongo db')

    def close_connection(self):
        self.connection.close()
        print('coneccion cerrada')

    def insertone(self, collection, datos):
        try:
            self.open_connection()
            self.collection = self.db[collection]
            id = self.collection.insert_one(datos).inserted_id
            print('datos insertados con exito '+ id)
        except:
            print('Error al insertar en ' + collection)
        self.close_connection()


"""
DB = Mongo('GenomicDB')
DB.open_connection()
DB.close_connection()
"""
