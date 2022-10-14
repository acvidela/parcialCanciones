

from tkinter import N


def agregarUnaCancion(listaCanciones, nombreIn, artistaIn, letraIn):
    cancion = {'nombre': nombreIn,'artista':artistaIn,'letra':letraIn}
    listaCanciones.append(cancion)

#primerasCanciones agrega 5 primeras canciones en la lista de canciones, para luego poder interactuar con el cancionero
def primerasCanciones(listaCanciones):
    nombre = "Pepe Lui"
    artista = "Divididos"
    letra = "Va Pepe Lui con bocho de radiograbador"
    agregarUnaCancion(listaCanciones, nombre,artista,letra) #primera canción
    nombre = "Luca"
    artista = "Divididos"
    letra = "Luca\n como una canción que zumba en el viento del corazón\nLuca\nfuelle tano que\nrespirando pampas se aporteño"
    agregarUnaCancion(listaCanciones, nombre,artista,letra) #segunda canción

def ingresarLetra():
    letra = ""
    print("Ingrese la letra de la canción. Para nuevo renglón enter y la letra f para terminar")
    lineaLetra = input()
    while lineaLetra != "f" and lineaLetra != "F":
        letra = letra + "\n" + lineaLetra
        lineaLetra = input("Ingrese nueva línea, f para terminar\n")
    return letra

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

def buscarPorNombre(listaCanciones):
    nombre = input("Ingrese el nombre de la canción a buscar: ")
    for cancion in listaCanciones:
        if cancion["nombre"] == nombre:
            print("Encontramos su canción:")
            imprimirCancion(cancion)
            return
    print("El nombre de la canción buscada no se encuentra en el cancionero")

def modificarPorNombre(listaCanciones):
    nombre = input("Ingrese el nombre de la canción a modificar: ")
    for i in range(0,len(listaCanciones)):
        if listaCanciones[i]["nombre"] == nombre:
            print("Encontramos su canción")
            opcion = input("¿Desea modificar el nombre? S/N")
            if opcion == "S" or opcion == "s":
                nombreNuevo = input("ingrese nuevo nombre: ")
                listaCanciones[i]["nombre"]=nombreNuevo
            opcion = input("¿Desea modificar el artista? S/N")
            if opcion == "S" or opcion == "s":
                artistaNuevo = input("ingrese nuevo artista: ")
                listaCanciones[i]["artista"]=artistaNuevo
            opcion = input("¿Desea modificar la letra? S/N")
            if opcion == "S" or opcion == "s":
                letraNueva = ingresarLetra()
                listaCanciones[i]["letra"]=letraNueva
            return
    print("El nombre de la canción buscada no se encuentra en el cancionero")