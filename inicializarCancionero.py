from manipularCancionero import *

#Inicializa el cancionero vacío
def inicializar():
    listaCanciones = []
    return(listaCanciones)

#Agrega 5 primeras canciones en la lista de canciones, para luego poder interactuar con el cancionero    
def primerasCanciones(listaCanciones):
    nombre = "Pepe Lui"
    artista = "Divididos"
    letra = "Va Pepe Lui con bocho de radiograbador"
    agregarUnaCancion(listaCanciones, nombre,artista,letra) #primera canción
    nombre = "Luca"
    artista = "Divididos"
    letra = "Luca\n como una canción que zumba en el viento del corazón\nLuca\nfuelle tano que\nrespirando pampas se aporteño"
    agregarUnaCancion(listaCanciones, nombre,artista,letra) #segunda canción
    nombre = "La hija del fletero"
    artista = "Patricio Rey y sus redonditos de Ricota"
    letra = "La hija del fletero, linda infinita\n volvió a Madrid, donde parece que es feliz\nEse día me mandó al descenso\nrecuerdo como su mirada me volteó"
    agregarUnaCancion(listaCanciones, nombre,artista,letra) #tercera canción
    nombre = "Pasajera en trance"
    artista = "Charly Garcia"
    letra = "Ella está por embarcar\n quizás consiga un pasaje en la borda\nElla está por despegar\nella se va"
    agregarUnaCancion(listaCanciones, nombre,artista,letra) #cuarta canción   
    nombre = "Zamba para olvidar"
    artista = "Pedro Aznar"
    letra = "No se para que volviste\nSi ya empezaba a olvidar\nNo si ya lo sabrás\nlloré cuando vos te fuiste\nNo se para que volviste\nQue mal me hace recordar"
    agregarUnaCancion(listaCanciones, nombre,artista,letra) #quinta canción
