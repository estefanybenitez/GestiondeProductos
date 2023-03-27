
def create_json_productos():
    _id = int(input("_id :"))
    nombre = input ("nombre: ")
    categoria = input("categoria: ")
    existencia = int(input("existencia: "))
    precio = float(input("precio: "))

    producto = {
        "_id": _id,
        "nombre" : nombre,
        "categoria": categoria,
        "existencia": existencia,
        "precio": precio,
    }
    return producto


def create_json_update():
    print("Que Desea Modificar")
    print("1.Modificar todo ")
    print("2.Modificar un elemento ")
    opcion = input("Ingrese una opcion: ")

    if opcion=="1":
        _id = int(input("_id: "))
        nombre = input("nombre: ")
        categoria = input("categoria: ")
        existencia = int(input("existencia"))
        precio = float(input("precio"))

        producto = {
            "_id": _id,
            "nombre": nombre,
            "categoria": categoria,
            "existencia": existencia,
            "precio": precio,
        }
        return producto

    elif opcion == "2":
        indice = input("Ingrese el indice")
        valor = input("Ingrese el valor a modificar ")
        producto = {indice: valor}
        return producto
    else:
        print("No valido")






