from pymongo import MongoClient


class Mongo:
    """docstring for ClassName"""

    def __init__(self, dbname, port=27017):
        self.connection = ''
        self.dbname = dbname
        self.port = port
        self.db = ''
        self.collection = ''

    def open_connection(self):
        try:
            self.connection = MongoClient('localhost', self.port)
            self.db = self.connection[self.dbname]
            print('Coneccion exitosa ' + self.dbname)
        except:
            print('Error al conectar con mongo db')

    def close_connection(self):
        self.connection.close()
        print('coneccion cerrada')

    def insertone(self, collection, datos):
        try:
	        #self.open_connection()
	        self.collection = self.db[collection]
	        self.collection.insert_one(datos)
	        print('datos insertados con exito ')
	        #self.close_connection()
        except:
            print('Error al insertar en ' + collection)
            #self.close_connection()
        

    def insertmany(self, collection, datos):
        try:
        	print(datos)
        	self.open_connection()
        	self.collection = self.db[collection]
        	self.collection.insert_many(datos)
        	print('Multiples archivos insertados con exito')
        except:
        	print('Error al insertar el bulk ' + collection)
        self.close_connection()

"""
db = Mongo('GenomicDB')
new_posts = [
  {
    "Organismo": "Cytochrome c biogenesis FC",
    "Funcion": "http://www.ebi.ac.uk/ena/data/view/AJM70220.1",
    "CadenaDNA": "MVQLHNFFFFITSMVVPRGTAAPVLLKWFVSRDVPTGALFSNGTIIPIPIPSFPLLVYLHSRKFIRSADGAKSGVLVRASRPILLPDIIGRSSSETRARNALFRFVPVLHFLLLESKGDFSYLESFCGVLRLLFFRTFFFLPRDRSAKPERARRRKGQTLRPNGNEQRRNEKMRCLGHPHLERRVEGFGPVAFPVPPSSGGACVEGAPPEIGLEALTLPTSRELMAVGHDYYQKAPMKMNISHGGVCIFMLGVLLSNTKKIQFTQRLPLGSELHMGKERCCLRGLDHLHGPTFHSICGNLMIYKPSLTSDRLMFEHDESLRADLLPIHFPASYENGKLEHFFHRWMKNREHNNFWLTMFPEKRYFRERTSTTEVAIHTNLFTDLYASIGTGSSRTGGWYTTIIKLPFIFFIRIGFMLASLGGSRSLLRQLQKDKLRWN"
  },
  {
    "Organismo": "Cytochrome c biogenesis FC",
    "Funcion": "http://www.ebi.ac.uk/ena/data/view/AJM70220.1",
    "CadenaDNA": "MVQLHNFFFFITSMVVPRGTAAPVLLKWFVSRDVPTGALFSNGTIIPIPIPSFPLLVYLHSRKFIRSADGAKSGVLVRASRPILLPDIIGRSSSETRARNALFRFVPVLHFLLLESKGDFSYLESFCGVLRLLFFRTFFFLPRDRSAKPERARRRKGQTLRPNGNEQRRNEKMRCLGHPHLERRVEGFGPVAFPVPPSSGGACVEGAPPEIGLEALTLPTSRELMAVGHDYYQKAPMKMNISHGGVCIFMLGVLLSNTKKIQFTQRLPLGSELHMGKERCCLRGLDHLHGPTFHSICGNLMIYKPSLTSDRLMFEHDESLRADLLPIHFPASYENGKLEHFFHRWMKNREHNNFWLTMFPEKRYFRERTSTTEVAIHTNLFTDLYASIGTGSSRTGGWYTTIIKLPFIFFIRIGFMLASLGGSRSLLRQLQKDKLRWN"
  }
]
db.insertmany('Proteinas', new_posts)
"""