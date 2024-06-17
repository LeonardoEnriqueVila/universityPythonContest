import random # importacion del modulo "random"
# definicion de variables de colores. Esto sirve para poder colorear los textos impresos en la consola. Se usa secuencias de escape ANSI
ROJO = "\033[31m"
AMARILLO = "\033[33m"
CELESTE = "\033[36m"
NARANJA = "\033[38;5;214m"
VERDE = "\033[32m"
RESET = "\033[0m"

arco = [ # definición de la lista de posiciones del arco
    "        1        ",
    "        2        ",
    "        3        ",
    "        4        ",
    "        5        ",
    "        6        ",
    "        7        ",
    "        8        ",
    "        9        " 
]

def inputUsuario(mensaje): # esta funcion permite validar el ingreso del usuario
    while True: # se repite infinitamente hasta que se obtenga un resultado valido
        ingreso = -1 # se defina la variable ingreso en -1 para permitir que se ejecute el bucle
        try: # se utiliza "try-except" para permitir el manejo de entrada invalida
            while ingreso < 1 or ingreso > 9: # se repite mientras el ingreso sea un numero fuera de rango
                ingreso = int(input(mensaje)) # obtiene el input del usuario utilizando el mensaje que se pasa de argumento (segun tenga que patear o atajar)
                if ingreso < 1 or ingreso > 9: # si el ingreso es un valor numerico por fuera del rango, genera una alerta
                    print(f"{ROJO}Ingresar un valor numérico entre 1 y 9.{RESET}")
                else: # si el ingreso es correcto, lo retorna
                    return ingreso
        except ValueError: # maneja el caso en el que no se ingrese un valor numerico
            print(f"{ROJO}Ingresar un valor numérico entre 1 y 9.{RESET}")

def realizarAccion(tiro, accion): # esta funcion define la accion a realizar segun el valor del tiro y del argumento accion
    if accion == "patear": # si la accion es patear
        # el valor del numero de tiros totales sumando los de ambos equipos determina las acciones
        if tiro % 2 != 0: # verifica que el tiro sea impar, eso supone que el jugador patea
            posicion = inputUsuario(f"{AMARILLO}Ingrese la posición donde desea patear en el arco (1-9): {RESET}")
        else: # sino, patea la computadora
            posicion = random.randint(1, 9) # el valor de pateada de la computadora es aleatorio
    elif accion == "atajar": # si la accion es atajar
        if tiro % 2 == 0: # verifica que el tiro sea par, eso supone que el jugador ataja
            posicion = inputUsuario(f"{AMARILLO}Ingrese la posición donde desea atajar en el arco (1-9): {RESET}")
        else: # sino, ataja la computadora
            posicion = random.randint(1, 9) # el valor de atajada de la computadora es aleatorio
    return posicion # devuelve el valor obtenido, que puede ser el valor de atajada o pateada de la computadora o jugador segun los argumentos

def agregarCaracteres_EnPosiciones(arco, indicesCadenas, caracteres, posiciones): # esta funcion permite colocar los caracteres alfabeticos en el arco
    # los cuales determinan donde se pateo y donde se lanzo al arquero
    nuevoArco = arco.copy() # crea una copia de la lista original para no modificarla
    for indiceCadena, caracter, posicion in zip(indicesCadenas, caracteres, posiciones): # itera sobre los índices, caracteres y posiciones proporcionadas
        # zip permite unificar los elementos de cada indice, de iterables diferentes en un nuevo iterable, donde cada indice contiene elementos de indice correspondiente de cada iterable
        # se desempaqueta el elemento obtenido en variables individuales. 
        cadena = nuevoArco[indiceCadena] # extrae la cadena de la lista en la posición especificada
        listaCaracteres = list(cadena) # convierte la cadena en una lista de caracteres
        listaCaracteres[posicion] = caracter # inserta el caracter en la posición deseada
        nuevaCadena = ''.join(listaCaracteres) # convierte la lista de caracteres de nuevo a una cadena
        nuevoArco[indiceCadena] = nuevaCadena # reemplaza la cadena original en la lista del nuevo arco con la nueva cadena
        # logrando entonces colocar la O y X junto a la posicion del arco correspondiente
    return nuevoArco # devuelve el arco actualizado

def resultadoTiro(tiroArco, atajoArco, tiro, argentina, paisesBajos): # determina el resultado de cada tiro
    indicesCadenasModificar = [tiroArco - 1, atajoArco - 1]  # los indices de la lista de posiciones del arco donde se lanzo al arquero y pateo
    caracteresInsertar = ['X', 'O'] # caracteres que se desean insertar, donde O representa el punto donde se lanzó al arquero, y X el punto donde se pateo
    posicionesInsertar = [3, 13] # los índices 3 y 13 fueron seleccionados de forma arbitraria para insertar temporalmente los caracteres 'X' y 'O' en la lista de caracteres del arco
    arcoActualizado = agregarCaracteres_EnPosiciones(arco, indicesCadenasModificar, caracteresInsertar, posicionesInsertar) # actualiza el arco
    if tiro % 2 != 0: # si el tiro no es par quiere decir que argentina pateo
        if (tiroArco in [2, 5, 8] and atajoArco in [2, 5, 8]) or tiroArco == atajoArco: # si el atajoArco coincide con el tiroArco
            print(f"{NARANJA}¡Paises Bajos atajo el penal!{RESET}") # entonces paises bajos atajo el penal
        elif tiroArco != atajoArco : # sino
            argentina += 1 # gol de argentina
            print(f"{CELESTE}¡Gol de Argentina!{RESET}")
    else: # si el tiro es par quiere decir que paises bajos pateo 
        if (tiroArco in [2, 5, 8] and atajoArco in [2, 5, 8]) or tiroArco == atajoArco: # si el atajoArco coincide con el tiroArco
            print(f"{CELESTE}¡Argentina atajo el penal!{RESET}") # entonces argentina atajo el penal
        elif tiroArco != atajoArco: # sino
            paisesBajos += 1 # gol de paises bajos
            print(f"{NARANJA}¡Gol de Paises Bajos!{RESET}")
    return argentina, paisesBajos, arcoActualizado # devuelve el arco actualizado y los puntajes de cada equipo tras la lanzada  

def imprimirArco(lista): # imprime en la consola el arco, ya sea con los caracteres numericos de posicion de acciones o sin ellos
    print("=================================================================") # barra superior
    for i in range(0, 9, 3): # itera en los indices del arco, saltando de a 3 (usando el step)
        print(f"|| {lista[i]} || {lista[i+1]} || {lista[i+2]} ||") # identifica los trios de posiciones, sumando +1 y +2 al indice actual
        if i < 6: # se asegura de no colocar una division intermedia al final
            print("||===================||===================||===================||") # divisiones intermedias
    print("=================================================================") # barra inferior

def definirGanador(golesArgentina, golesPaisesBajos, contadorTiro): # determina si un equipo gano el partido
    if contadorTiro < 11: # comprobacion en primeros 10 tiros
        # se determinan los tiros restantes de cada equipo
        tirosRestantes_Argentina = (10 - contadorTiro) // 2
        tirosRestantes_PaisesBajos = (10 - contadorTiro + 1) // 2 # se le agrega 1 porque paises bajos patea segundo
        diferenciaGoles = golesArgentina - golesPaisesBajos # se determina la diferencia de goles entre equipos
        # verificar si la diferencia de goles es mayor que los tiros restantes de algun equipo para determinar un ganador inicialmente
        if diferenciaGoles > tirosRestantes_PaisesBajos:
            return "Argentina"
        elif -diferenciaGoles > tirosRestantes_Argentina: # "-diferencia_goles" lo pasa al valor contrario en positivo o negativo
            return "Países Bajos"
    elif contadorTiro > 10: # si el contadorTiro es mayor a 10, quiere decir que lo equipos empataron y se alargaron los penales
        # las siguientes comprobaciones son teniendo en cuenta que el partido se empato y se define en base a quien logre ganar una ronda
        if golesPaisesBajos < golesArgentina and contadorTiro % 2 == 0: 
            # para que argentina gane, necesita tener mas puntaje en el turno de patear de paises bajos, ya que argentina patea primero
            # por eso debe comprobar "contadorTiro % 2 == 0"
            return "Argentina"
        elif golesPaisesBajos > golesArgentina: 
            # si el puntaje de paises bajos supera al de argentina, de forma automatica gana ya que paises bajos patea segundo
            return "Países Bajos"
    # en caso de que la ronda sea menor que la 5 o que no se hayan encontrado ganadores, retornar None 
    return None # esto se podria borar, ya que por defecto las funciones en python retornan None. Sin embargo se deja como guia visual

def penales(): # esta funcion ensambla todas las funcionalidades, permitiendo efectuar el flujo de los penales
    tiroArco = 0 # determina la posicion donde se pateo
    atajoArco = 0 # determina la posicion donde se atajo
    contadorTiro = 0 # determina el total de tiros, se usa como contador y sirve para la impresion y para saber que equipo patea y ataja
    golesArgentina = 0 # puntuacion de argentina
    golesPaisesBajos = 0 # puntuacion de paises bajos
    while True: # bucle eterno que se rompe cuando se encuentra un ganador
        ganador = definirGanador(golesArgentina, golesPaisesBajos, contadorTiro) # busca un ganador 
        if ganador == None: # si no hay un ganador entonces se deben realizar las acciones
            if contadorTiro == 10: # permite identificar si hay un empate en la ronda 10
                print(f"{VERDE}¡Empate! Se alargan los penales{RESET}\n") # informa
            print(f"{AMARILLO}TIRO {contadorTiro + 1}{VERDE} - Patea {'Argentina' if (contadorTiro + 1) % 2 != 0 else 'Paises Bajos'}{RESET}") # informa numero de tiro y quien patea
            contadorTiro += 1 # incrementa el contador de tiros
            imprimirArco(arco) # imprime el arco original (sin valores alfabeticos de posicion de atajado y tiro)
            tiroArco = realizarAccion(contadorTiro, "patear") # realiza la accion patear de la computadora o jugador
            atajoArco = realizarAccion(contadorTiro, "atajar") # realiza la accion atajar de la computadora o jugador
            # determina el resultado del tiro compuesto por la accion de patear y atajar, actualiza los puntajes y la el arco
            golesArgentina, golesPaisesBajos, arcoActualizado = resultadoTiro(tiroArco, atajoArco, contadorTiro, golesArgentina, golesPaisesBajos)
            imprimirArco(arcoActualizado) # imprime el arco con los valores alfabeticos que determinan donde se pateo y lanzo al arquero
            print(f"{AMARILLO}Resultados Tiro: {contadorTiro}\n{CELESTE}Argentina: {golesArgentina}\n{NARANJA}Paises Bajos: {golesPaisesBajos}{RESET}\n") # informa

        else: # si el ganador no es "None" entonces definirGanador encontro un ganador, se informa el ganador
            if ganador == "Argentina":
                print(f"{CELESTE}¡Argentina es el ganador!{RESET}\n")
            else:
                print(f"{NARANJA}¡Paises Bajos es el ganador!{RESET}\n")
            return # se asegura de terminar el bucle tras informar el ganador

def menu(): # Esta funcion permite al usuario decidir si quiere jugar otro partido cuando se finaliza uno, la misma es llamada al finalizar la funcion penales
    while True: # el bucle se repite hasta que el usuario ingrese alguna de las variantes de "Si, SI, si, No, NO, no"
        ingreso = input(f"{VERDE}¿Deseas jugar otro partido? (Ingresar: si/no): {RESET}") # se promptea al usuario induciendo a que ingrese si o no
        ingreso = ingreso.lower() # pasa a lowercase el ingreso del usuario, para abarcar todas las posibilidades "Si, SI, si, No, NO, no"
        if ingreso == "si":
            print(f"{VERDE}\n¡Se juega otro partido!\n{RESET}")
            return True # devuelve True si el jugador desea jugar otro partido, esto hará que la funcion penales se vuelva a ejecutar
        elif ingreso == "no":
            print(f"{VERDE}\n¡Muchas gracias por jugar!\n{RESET}")
            return False # devuelve False si el jugador no desea jugar otro partido esto marcara al flag como False y entonces el programa terminara

def main(): # funcion principal
    print(f"\n{VERDE}¡Bienvenidos al gran partido de la Copa de Algoritmia!\n{RESET}") # mensaje de bienvenida al ejecutar el script
    flag = True # permite saber si el jugador quiere jugar otro partido tras finalizar uno
    while flag == True: # se repite hasta que el jugador no quiera jugar mas, ingresando alguna de las variantes de no
        penales() # maneja el flujo del partido
        flag = menu() # cuando termina un partido, se muestra un menu que pregunta si se desea jugar otro

main() # llamada a la funcion principal

"""
---------- DOCUMENTACION ----------

-> Definición de variables globales
    - Las secuencias de escape ANSI permiten que se pueda colorear el texto impreso en la consola, para volver el programa mas interactivo
    - Se define una lista de numeros espaciados, que serán impresos en el arco para que el usuario pueda visualizar donde patea o ataja

-> inputUsuario(mensaje)
    - Esta funcion permite obtener el input del usuario que decide la posición en el arco donde va a patear o atajar
    - Obtiene de argumento el mensaje que se imprime, donde el mensaje que indica patear es diferente al que indica atajar
    - Maneja la excepcion en caso de no ser valida, tampoco permite ingresar un valor numerico fuera del rango
    - Retorna el ingreso del usuario (que es la posicion en el arco donde desea patear o atajar)
    - La funcion tiene un bucle eterno que se ejecuta las veces que sean necesarias hasta que se obtenga una entrada valida

-> realizarAccion(tiro, accion)
    - Esta funcion define la accion a realizar segun el valor del tiro y del argumento accion
    - El argumento tiro corresponde al total de tiros que se lanzaron sumando los dos equipos
        - Un valor de tiro impar, supone que el jugador patea. Un valor par, que el jugador ataja
        - Esto es debido a que Argentina (el jugador) es el primero en patear
    - El argumento accion determina cual es la accion a realizar, si se trata de atajar o patear
    - Entonces, el valor de accion determina que se realiza en esta llamada a la funcion
    - Y el valor de tiro determina si el que realiza dicha accion es la computadora o el jugador
    - Esta funcion se llama dos veces en la funcion "penales()" y permite obtener en cada llamada el valor correspondiente de pateada y atajada
        - independientemente de quien sea el que hace cada accion (computadora o jugador) ya que eso lo determina el valor del tiro
        - Recordando: tiro es el valor del total de tiros realizados entre ambos equipos

-> agregarCaracteres_EnPosiciones(arco, indicesCadenas, caracteres, posiciones)
    - Cuando se realizan las acciones, esta funcion permite representar visualmente donde se pateo y lanzo al arquero
    - Coloca una X donde se pateo y una O donde se lanzo al arquero
    - Los argumentos son:
        - arco: la lista original del arco
        - indicesCadenas: los indices de la lista del arco donde ocurrieron acciones
        - caracteres: caracteres alfabeticos que permiten visualizar la posicion de las acciones
        - posiciones: posiciones temporales arbitrarias donde se guardan los caracteres alfabeticos antes de ser colocados donde corresponde
    - La funcion retorna el arco actualizado, con los caracteres alfabeticos en sus posiciones correspondientes

-> resultadoTiro(tiroArco, atajoArco, tiro, argentina, paisesBajos)
     - Esta funcion determina el resultado de cada tiro luego de cada lanzada
     - Los argumentos son: 
        - tiro: el numero de tiro actual sumando ambos equipos, que permite determinar quien es el pateador y atajador
        - atajoArco: la posicion donde se lanzo al arquero
        - tiroArco: la posicion donde se pateo
        - argentina: la puntuación de argentina
        - paises bajos: la puntuacion de paises bajos
    - La funcion se basa en el valor del tiro actual para determinar quien pateo y lanzo al arquero
    - Compara los valores de tiro y atajada, determinando si el penal se atajo o fue gol
    - Supa el gol correspondiente en caso de haberse dado
    - Devuelve el arco actualizado y los puntajes de cada equipo tras la lanzada 

-> imprimirArco(lista)
    - Esta funcion imprime el arco actualizado
    - el argumento lista es:
        - o bien el arco sin los caracteres alfabeticos (es decir, cuando se promptea al usuario)
        - o el arco actualizado con los caracteres alfabeticos de posicion de accion

-> definirGanador(golesArgentina, golesPaisesBajos, contadorTiro)
    - Esta funcion identifica un ganador independientemente de la instancia del juego en la que se este
    - Sus argumentos son:
        - golesArgentina: la puntuacion de argentina
        - golesPaisesBajos: la puntuacion de paises bajos
        - contadorTiro: la cantidad total de tiros lanzados entre los dos equipos
    - Tiene dos posibilidades, 
        - o estan en alguno de los primeros 10 tiros
            - donde para declarar un ganador, la diferencia de goles tiene que ser mayor que los tiros restantes de algun equipo para determinar un ganador 
        - o se dio un empate tras los primero 10 tiros y estan en un tiro superior a 10
            - donde para declarar un ganador debe ocurrir lo siguiente:
                - para que argentina gane, 
                    - necesita tener mas puntaje en el turno de patear de paises bajos, ya que argentina patea primero
                    - por eso debe comprobar "contadorTiro % 2 == 0"
                - para que paises bajos gane,
                    -solo debe superar al puntaje de argentina, ya que paises bajos patea segundo
    - Devuelve una cadena que indica el nombre del equipo ganador en caso de haberlo
        - Si no hay un ganador retorna None de forma explicita por motivos de legibilidad

-> penales()
    - Esta funcion ensambla todas las funcionalidades, permitiendo efectuar el flujo de los penales
    - Se definen las variables claves que manejan el flujo del partido
    - Se ejecuta un bucle eterno que funciona hasta encontrar un ganador
    - En dicho bucle:
        - Se realizan las acciones de patear y atajar
        - la variable contadorTiro es crucial ya que permite saber quien patea y quien ataja
        - imprime el arco dos veces
            - una sin los caracteres alfabeticos, mostrando las opciones de posicion para accionar
            - y luego imprime mostrando los caracteres, logrando mostrar de forma visual donde se ejecuto la accion
        - realiza las acciones correspondientes, actualizando las variables que correspondes, llamando a realizarAccion 
        - se busca un ganador
        - si se encuentra al ganador, informa al mismo y retorna para cortar el bucle eterno

-> menu()
    - Esta funcion permite al usuario decidir si quiere jugar otro partido cuando se finaliza uno, la misma es llamada al finalizar la funcion penales
    - obtiene un input del usuario y lo pasa a lowercase, para poder comparar y saber si la respuesta es "si" o "no"
    - admite todas las variables de si y no (Si, SI, si, No, NO, no)
    - no necesita manejo de excepciones porque la entrada es siempre string
    - devuelve True si se desea jugar otro partido, False si no. 

-> main()
    - Funcion principal
    - Da la bienvenida al ejecutar el script
    - la variable flag permite saber si el jugador quiere jugar otro partido tras finalizar uno
    - llama a penales, que ejecuta el flujo del partido
    - luego llama a menu, que permite saber si el usuario desea jugar otro partido
"""