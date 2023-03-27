import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["expractico1"]
productos = db["productos"]

'''Productos = {
    "_id": 2,
    "nombre": "cartera",
    "categoria": "accesorio",
    "existencia": 80,
    "precio": 50.0
}
#insert en la coleccion productos
result = productos.insert_one(Productos)
print(result.inserted_id)'''

productos.create_index([("nombre",1)])