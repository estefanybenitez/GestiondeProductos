
from CRUD import *
from FUNCIONES import *

ejecutar = True

while ejecutar:
    print("\n")
    print("Menu de opciones")
    print("*" * 62)
    print("1. Buscar producto por categoria")
    #filtrar por categoria
    print("2. Buscar producto por Nombre ")
    print("3. Agregar un registro")
    print("4. Modificar un registro")
    print("5. Eliminar registro")
    print("6. Salir del sistema")
    print("*" * 62)
    opcion = input("Ingrese un opcion: ")

    if opcion == "1":
       categoria = input("ingrese la categoria : ")
       read_productos_c(categoria)

    elif opcion == "2":
        nombre = input("ingrese el nombre a buscar: ")
        read_productos(nombre)

    elif opcion == "3":
        producto = create_json_productos()
        create_productos(producto)

    elif opcion == "4":
        _id = int(input("ingrese el id a modificar"))
        producto = create_json_update()
        update_productos(_id, producto)

    elif opcion == "5":
        _id = int(input("ingrese el id a eliminar"))
        delete_productos(_id)

    elif opcion == "6":
        ejecutar = False
        print("\n")
        print("Programa Terminado...")
        print("-" * 62)
        print("\n")
    else:
        print("-" * 62)
        print("Opcion no valida...")
        print("Ejecute una opcion valida...")
        print("\n")
        input()
