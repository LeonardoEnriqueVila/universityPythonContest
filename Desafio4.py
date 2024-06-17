import random # importacion del modulo "random"
# definicion de variables de colores. Esto sirve para poder colorear los textos impresos en la consola. Se usa secuencias de escape ANSI
ROJO = "\033[31m"
AMARILLO = "\033[33m"
CELESTE = "\033[36m"
NARANJA = "\033[38;5;214m"
VERDE = "\033[32m"
RESET = "\033[0m"

def dibujarPatron(): # imprime interfaz
    patron = [
        "#####################",
        "#                   #",
        "#   #############   #",
        "#   #           #   #",
        "#   #   #####   #   #",
        "#   #   #   #   #   #",
        "#   #   #####   #   #",
        "#   #           #   #",
        "#   #############   #",
        "#                   #",
        "#####################"
    ]
 
    for linea in patron:
        print(linea)

tiradores = { # diccionario de tiradores
    "tirador 1": 0,
    "tirador 2": 0,
    "tirador 3": 0,
    "tirador 4": 0,
    "tirador 5": 0,
    "jugador": 0,
}

def inputUsuario(): # esta funcion permite validar el ingreso del usuario
    while True: # se repite infinitamente hasta que se obtenga un resultado valido
        ingreso = -1 # se defina la variable ingreso en -1 para permitir que se ejecute el bucle
        try: # se utiliza "try-except" para permitir el manejo de entrada invalida
            while ingreso < 1 or ingreso > 4: # se repite mientras el ingreso sea un numero fuera de rango
                ingreso = int(input("Seleccione una diana para disparar. (La 1 es mas facil, y la 4 es la más dificil): ")) # obtiene el input del usuario utilizando el mensaje que se pasa de argumento (segun tenga que patear o atajar)
                if ingreso < 1 or ingreso > 4: # si el ingreso es un valor numerico por fuera del rango, genera una alerta
                    print(f"{ROJO}Ingresar un valor numérico entre 1 y 4.{RESET}")
                else: # si el ingreso es correcto, lo retorna
                    return ingreso
        except ValueError: # maneja el caso en el que no se ingrese un valor numerico
            print(f"{ROJO}Ingresar un valor numérico entre 1 y 4.{RESET}")

def tirosComputadora(): # funcion para efectuar tiros de la computadora
    for tirador in tiradores: # iterar en diccionario de tiradores
        if tirador != "jugador": # evitar que el jugador dispare
            target = random.randint(1, 4) # selecciona un target para el tirador de la computadora actual
            randomNum = random.randint(1, 10) # probablididad de efectuar tiro del tirador actual 
            if target == 1: # 1 2 3 4
            # facil
                if randomNum in [1, 2, 3, 4]: # se utiliza lista de probabilidades
                    # se modifica el valor de cada tirador si le dio al target
                    tiradores[tirador] += 1 # cuanto mas probable sea que se de el tiro, menos puntos da
            elif target == 2: #5 6 7
            # intermedio
                if randomNum in [5, 6, 7]:
                    tiradores[tirador] += 2 
            elif target == 3: #8 9
            # complejo
                if randomNum in [8, 9]:
                    tiradores[tirador] += 3
            else: #10
                # muy dificil
                if randomNum == 10:
                    tiradores[tirador] += 4

def definirTarget(): # efectua el tiro del jugador
    dibujarPatron()
    target = inputUsuario() # obtiene el input del usuario
    randomNum = random.randint(1, 10)
    if target == 1: #1 2 3 4
        # facil
        if randomNum in [1, 2, 3, 4]:
            tiradores["jugador"] += 1
            print(f"{VERDE}Le diste al target!{RESET}")
        else:
            print(f"{ROJO}Le erraste!{RESET}")
    elif target == 2: #5 6 7
        # intermedio
        if randomNum in [5, 6, 7]:
            tiradores["jugador"] += 2
            print(f"{VERDE}Le diste al target!{RESET}")
        else:
            print(f"{ROJO}Le erraste!{RESET}")
    elif target == 3: #8 9
        # complejo
        if randomNum in [8, 9]:
            tiradores["jugador"] += 3
            print(f"{VERDE}Le diste al target!{RESET}")
        else:
            print(f"{ROJO}Le erraste!{RESET}")
    else: #10
        # muy dificil
        if randomNum == 10:
            tiradores["jugador"] += 4
            print(f"{VERDE}Le diste al target!{RESET}")
        else:
            print(f"{ROJO}Le erraste!{RESET}")

def escribir(): # esta funcion abre el archivo en modo adjuntar y escribe el texto del tiro actual
    tiradoresOrdenados = dict(sorted(tiradores.items(), key=lambda x: x[1], reverse=True)) # se utiliza sorted para ordenar a los tiradores por puntuacion
    with open("tiros.txt", "w") as archivo: # abre el archivo "tiros.txt" en modo de write (determinado por "w")
        archivo.write("TABLA DE PUNTUACIONES:\n")
        for tirador, puntuacion in tiradoresOrdenados.items(): # utilizamos el metodo .items para iterar en el dict y obtener cada tirador y sus puntos
            archivo.write(f"{tirador}: {puntuacion} puntos\n") # escribe en el archivo .txt los datos usando el metodo write

def juego(): # funcion principal
    for _ in range(0, 5): # se ejecuta para 6 rondas de tiros
        # llamada a las funciones

        definirTarget() # funcion para el jugador
        tirosComputadora() # funcion para la computadora
    escribir() # escribir en el archivo .txt

juego()






