

from tkinter import N

#Recibe el cancionero y tres strings para armar el diccionario que agregará al final del cancionero
def agregarUnaCancion(listaCanciones, nombreIn, artistaIn, letraIn):
    cancion = {'nombre': nombreIn,'artista':artistaIn,'letra':letraIn}
    listaCanciones.append(cancion)


#Pide al usuario la letra de una canción, ingresando línea por línea
def ingresarLetra():
    letra = ""
    print("Ingrese la letra de la canción por líneas. Cada línea termina con ENTER, teclee f para terminar")
    lineaLetra = input()
    while lineaLetra != "f" and lineaLetra != "F" :
        letra = letra + "\n" + lineaLetra
        lineaLetra = input("Ingrese nueva línea, f para terminar\n")
    return letra

#Pide al usuario los datos de una nueva canción para agregar al cancionero
def agregarNuevaCancion(listaCanciones):
    nombre = input("Ingrese el nombre la nueva canción: ")
    artista = input("Ingrese el nombre del artista: ")
    letra = ingresarLetra()
    agregarUnaCancion(listaCanciones, nombre,artista,letra) 


#Imprime una cancion
def imprimirCancion(cancion):
    print("Nombre canción: " + cancion["nombre"])
    print("Artista: " + cancion["artista"])
    print("Letra: " + cancion["letra"])
    print("***********")  #para separar las canciones

#Imprime todas las canciones del cancionero
def listarCanciones(listaCanciones):
    print("A continuación se listarán todas las canciones almacenadas en el cancionero\n")
    for cancion in listaCanciones:
        imprimirCancion(cancion)

#Busca una canción dentro del cancionero por nombre. 
#Si está la imprime, sino muestra mensaje
def buscarPorNombre(listaCanciones):
    nombre = input("Ingrese el nombre de la canción a buscar: ").lower() 
    for cancion in listaCanciones:
        if cancion["nombre"].lower() == nombre:
            print("Encontramos su canción:")
            imprimirCancion(cancion)
            return
    print("El nombre de la canción buscada no se encuentra en el cancionero")

#Solicita el nombre de la canción que quiere modificar. Si se encuentra pide los datos y modifica.
#Si ingresa un nombre que no está le sugiere agregarla 
def modificarPorNombre(listaCanciones):
    nombre = input("Ingrese el nombre de la canción a modificar: ").lower()
    for i in range(0,len(listaCanciones)):
        if listaCanciones[i]["nombre"].lower() == nombre:
            print("Encontramos su canción")
            opcion = input("¿Desea modificar el nombre? S/N").lower()
            if opcion == "s":
                nombreNuevo = input("ingrese nuevo nombre: ")
                listaCanciones[i]["nombre"]=nombreNuevo
            opcion = input("¿Desea modificar el artista? S/N").lower()
            if opcion == "s":
                artistaNuevo = input("ingrese nuevo artista: ")
                listaCanciones[i]["artista"]=artistaNuevo
            opcion = input("¿Desea modificar la letra? S/N").lower()
            if opcion == "s":
                letraNueva = ingresarLetra()
                listaCanciones[i]["letra"]=letraNueva
            return
    print("El nombre de la canción buscada no se encuentra en el cancionero\nSi desea agregarla como nueva canción, seleccione la opción \"a\" en el menú principal")