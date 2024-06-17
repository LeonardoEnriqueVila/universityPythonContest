import random # el modulo random es necesario para utilizar el metodo randint
# definir diccionario en donde el key es un indice de jugadora y value son los datos de la jugadora
jugadoras = {
   1: ["Argentina", "11", "Agostina Gorzelany"], # equipo, camiseta, nombre de jugadora
   2: ["Argentina", "9", "Maria Jose Granatto"],
   3: ["Argentina", "20", "Sofia Toccalino"],
   4: ["Argentina", "10", "Agostina Alonso"],
   5: ["Argentina", "8", "Valentina Raposo"],
   6: ["Argentina", "5", "Clara Barberi"],
   7: ["Argentina", "4", "Delfina Thome"],
   8: ["Argentina", "7", "Sofia Cairo"],
   9: ["Argentina", "16", "Pilar Campoy"],
   10: ["Australia", "7", "Aleisha Power"],
   11: ["Australia", "19", "Jocelyn Bartram"],
   12: ["Australia", "15", "Lucy Sharman"],
   13: ["Australia", "42", "Karri Somerville"],
   14: ["Australia", "16", "Kaitlin Nobbs"],
   15: ["Australia", "3", "Renee Taylor"],
   16: ["Australia", "2", "Claire Colwill"],
   17: ["Australia", "12", "Amy Lawton"],
   18: ["Australia", "13", "Harriet Shand"]
}

def escribir(pases): # esta funcion abre el archivo en modo escribir y escribe el texto de los pases
    with open("pases.txt", "w") as archivo: # abre el archivo "pases.txt" en modo de escribir (determinado por "a")
        archivo.write(pases) # escribe en el archivo .txt los datos usando el metodo write

def ejecutarPases():
    # dado que se pide aproximadamente 50k pases, se obtiene un total que ronda ese numero
    totalPases = random.randint(45000, 55000) # obtiene un total de pases, que es un numero que ronda los 50k
    pases = "" # variable donde se concatenan los pases
    for _ in range(0, totalPases): # realiza la cantidad de iteraciones determinada por la variable "totalPases"
        numero = random.randint(1, 18) # elije una "key" del dict para obtener una jugadora que realizará el pase
        resultado = random.randint(0, 1) # resultado del pase, que es 0 o 1
        minuto = random.randint(0, 60) # minuto de juego: entre 0 y 60, que es la duración de un partido de hockey
        datosJugadora = jugadoras[numero] # guarda los datos de la jugadora en variable datosJugadora (que es una lista)
        # concatena la variable pases con los datos de la jugadora, mas el resultado, mas el minuto y el salto de linea
        pases += f"{datosJugadora[0]};{datosJugadora[1]};{datosJugadora[2]};{resultado};{minuto}\n"
    escribir(pases) # pasa la variable pases a escribir, que se encarga de escribir los datos en el archivo

def main(): 
    ejecutarPases()

main() # funcion principal, donde se ejecuta todo