from manipularCancionero import *

canciones = []  #inicializa la lista de canciones vacía
primerasCanciones(canciones)         #agrega primeras 5 canciones "a mano"

opcion = ""
while opcion != "f" and opcion != "F":
    print("\nEste es su cancionero, ¿qué desea hacer?")
    print(" l: para listar el cancionero completo")
    print(" a: para agregar una nueva canción")
    print(" b: para buscar e imprimir una canción dado su nombre")
    print(" m: para modificar los datos de una canción")
    print(" f: para salir")
    opcion = input()
    if opcion == "l":
        listarCanciones(canciones)
        continue
    if opcion == "a":
        agregarNuevaCancion(canciones)
        continue
    if opcion == "b":
        buscarPorNombre(canciones)
        continue
    if opcion == "m":        
        modificarPorNombre(canciones)
        continue
    if opcion == "f":        
        print("chau")
        break

# listarCanciones(canciones)
# agregarNuevaCancion(canciones)
# listarCanciones(canciones)
# modificarPorNombre(canciones)
# buscarPorNombre(canciones)