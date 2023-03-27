from conexion import productos
import json

def read_productos_c(categoria = None): #buscarCategoria
    if categoria is not None:
        query = {"categoria": categoria}
        documents = productos.find(query)
        for document in documents:
            print(document)

def read_productos(nombre = None): #buscarNombre
    if nombre is not None:
        query = {"nombre": nombre}
        document = productos.find_one(query)
        print(document)
    else:
        documents = productos.find()
        for document in documents:
            print(document)

def create_productos(json_productos): #agregar
    result = productos.insert_one(json_productos)
    print(result.inserted_id)
    print("Registro Agregado")


def update_productos(_id, json_productos_update): #actualizar
    query = {"_id": _id}
    new_values = {"$set": json_productos_update}
    result = productos.update_one(query,new_values)
    print(result.modified_count)


def delete_productos(_id=None):
    if _id is not None:
        query = {"_id": _id}
        document = productos.delete_many(query)
        print(document)
        print("Se elimino con exito")
    else:
        print("No se encontro ningun registro")


