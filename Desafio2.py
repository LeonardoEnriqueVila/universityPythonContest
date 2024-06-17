"""
    Por Favor, leer la documentación en el pié del archivo, que complementa los comentarios del código, 
    para explicarlo de la mejor forma posible
    Tener en cuenta, que el archivo ".txt" tiene que estar en la misma carpeta de ejecución de este script
"""

# estructurar los datos 
equipos = { # este diccionario permite tener un registro de los pases de las jugadoras, para poder obtener estadisticas
    "Argentina": {
        "11": {"nombre": "Agostina Gorzelany", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0},
        "9": {"nombre": "Maria Jose Granatto", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0},
        "20": {"nombre": "Sofia Toccalino", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0},
        "10": {"nombre": "Agostina Alonso", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0},
        "8": {"nombre": "Valentina Raposo", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0},
        "5": {"nombre": "Clara Barberi", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0},
        "4": {"nombre": "Delfina Thome", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0},
        "7": {"nombre": "Sofia Cairo", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0},
        "16": {"nombre": "Pilar Campoy", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0}
    },
    "Australia": {
        "7": {"nombre": "Aleisha Power", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0},
        "19": {"nombre": "Jocelyn Bartram", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0},
        "15": {"nombre": "Lucy Sharman", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0},
        "42": {"nombre": "Karri Somerville", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0},
        "16": {"nombre": "Kaitlin Nobbs", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0},
        "3": {"nombre": "Renee Taylor", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0},
        "2": {"nombre": "Claire Colwill", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0},
        "12": {"nombre": "Amy Lawton", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0},
        "13": {"nombre": "Harriet Shand", "pases_bien": 0, "pases_mal": 0, "total_pases": 0, "porcentaje": 0}
    }
}

def contar_pases_y_efectividad():
    # leer el Archivo
    with open("pases.txt", "r") as archivo: # abrir el archivo en modo lectura ("r")
        for linea in archivo: # iterar por las lineas
            # elimina espacios en blanco al inicio y al final, incluyendo el salto de linea
            datos = linea.strip().split(";") # ahora "datos" es una lista donde cada elemento corresponde a un componente de la linea
            # se pasan los datos necesarios a la funcion
            # añadir los pases en cada iteracion en la jugadora correspondiente
            añadir_estadisticas(datos[0], datos[1], datos[3]) # pasamos pais, remera y resultado
    calcular_promedios() # llama a función que calcula los promedios con los datos actualizados
    ordenar_jugadoras() # ordena a las jugadoras segun su promedio
    return preparar_datos_para_salida() # estructura los datos para retornarlos segun se solicita

def añadir_estadisticas(pais, numero_camiseta, resultado):
    # acceder al diccionario de la jugadora especifica y actualizar sus estadisticas
    # se accede a la jugadora mediante su numero de camiseta en formato string
    jugadora = equipos[pais][numero_camiseta] # jugadora es una referencia al mismo diccionario en la memoria
    # entonces se puede acceder a sus valores y modificarlos
    # a traves de la nueva variable, se puede modificar el valor de la key obtenida
    jugadora["total_pases"] += 1  # incrementar el total de pases
    if resultado == "1":
        jugadora["pases_bien"] += 1  # incrementar pases bien si el pase fue exitoso
    else:
        jugadora["pases_mal"] += 1  # incrementar pases mal si el pase fue fallido

def calcular_promedios():
    # "equipos.values()"" retorna una vista de los valores del diccionario "equipos",
    # que son los diccionarios representando los equipos (Argentina y Australia).
    # este bucle for itera sobre cada uno de esos diccionarios de equipo.
    for jugadoras in equipos.values():  # se ejecuta una vez por cada equipo
        # "jugadoras" es el diccionario de las jugadoras de un equipo especifico.
        # cada clave en "jugadoras" es el número de camiseta de una jugadora,
        # y cada valor es otro diccionario con las estadísticas de esa jugadora.

        # "jugadoras.values()"" retorna una vista de los valores del diccionario "jugadoras",
        # que son los diccionarios de estadísticas de cada jugadora.
        # este segundo bucle for itera sobre cada uno de estos diccionarios de estadisticas.
        for estadisticas in jugadoras.values():  # se ejecuta una vez por cada jugadora en el equipo
            # "estadisticas" es un diccionario que contiene las estadísticas de una jugadora específica.
            # Incluye campos como "pases_bien", "pases_mal" y "total_pases".
            # aqui se comprueba si la jugadora ha realizado algun pase.
            if estadisticas["total_pases"] > 0:
                # si la jugadora ha hecho pases, se calcula el porcentaje de pases bien.
                # se calcula como el número de pases bien dividido por el total de pases,
                # se obtiene el porcentaje
                estadisticas["porcentaje"] = (estadisticas["pases_bien"] * 100) / estadisticas["total_pases"]
                # este calculo actualiza el campo "porcentaje" en el diccionario de estadísticas
                # de la jugadora, que es accesible directamente a través de la referencia en "estadisticas".

def ordenar_jugadoras(): # ordena a las jugadoras y reconstruye el diccionario para respetar el criterio de estructuracion de datos
    for pais, jugadoras in equipos.items(): # iterar por las 2 claves de pais del diccionario
        # convertir el diccionario de jugadoras en una lista de tuplas para poder ordenarlas
        lista_jugadoras = [(numero, datos) for numero, datos in jugadoras.items()] # obtener clave y valor de jugadoras
        # donde numero es el numero de camiseta y los datos las estadisticas de la jugadora
        # ordenar la lista de jugadoras basandose en el porcentaje de pases bien, de mayor a menor
        lista_jugadoras.sort(key=lambda x: x[1]["porcentaje"], reverse=True)
        # el argumento key de sort, determina la funcion lambda que se utiliza para ordenar, es decir el criterio
        # x representa el criterio, el cual es el elemento [1] de la tupla, que es un diccionario, al cual se le pide ordenar por el valor de "porcentaje"
        # reconstruir el diccionario de jugadoras con las jugadoras ordenadas
        equipos[pais] = {numero: datos for numero, datos in lista_jugadoras}
        # a la clave de pais se le pasa un diccionario donde numero es la clave (que representa al numero de camiseta)
        # y datos es el valor; ambos se obtienen de la lista de tuplas que devuelve un numero en formato string y un diccionario de datos (datos)
        

def preparar_datos_para_salida():
    # lista final que contendrá todos los equipos con sus jugadoras ordenadas
    resultado_final = [] # esta lista seguira el criterio de estructuración de datos solicitada
    # iterar sobre cada equipo y sus jugadoras ordenadas
    for pais, jugadoras in equipos.items(): # iterar por los paises, obteniendo los diccionarios de jugadoras que son el valor de la clave de pais
        # lista para almacenar los diccionarios de cada jugadora
        lista_jugadoras = []
        # agregar cada jugadora al resultado de este equipo
        for numero_camiseta, datos in jugadoras.items(): # iterar en el diccionario de jugadoras, obteniendo la clave como numero de camiseta
            # y los datos como diccionario para sus estadísticas
            # crear un diccionario por cada jugadora con su número y estadisticas
            datos_jugadora = {
                "numero": numero_camiseta,
                "nombre": datos["nombre"],
                "cantidad_pases": datos["total_pases"],
                "pases_bien": datos["pases_bien"],
                "pases_mal": datos["pases_mal"],
                "porcentaje": round(datos["porcentaje"], 2)  # redondeo a dos decimales
            }
            # añadir el diccionario de la jugadora a la lista de jugadoras
            lista_jugadoras.append(datos_jugadora)
        # añadir el diccionario del equipo al resultado final
        resultado_final.append({pais: lista_jugadoras})
    return resultado_final # devolver la lista con los datos estructurados como se solicitan

print(contar_pases_y_efectividad()) # la llamada a la funcion "contar_pases_y_efectividad()" se hace directamente como argumento del print
# lo cual permite que se imprima directamente la data organizada como se solicita

"""
 ------ DOCUMENTACION ------
A continuación, se detalla de forma exhaustiva lo que se realiza en el código:

1. Definición del diccionario "equipos":
   - Claves Principales: "Argentina" y "Australia", representando cada equipo participante.
   - Valor de cada Clave Principal: Un diccionario que contiene a las jugadoras del equipo.
   - Claves de Jugadoras: Representadas por el número de camiseta en formato string.
   - Valor de cada Clave de Jugadora: Un diccionario con las estadísticas relevantes de cada jugadora, que incluye:
     - "nombre": Nombre de la jugadora, valor estático que no cambia durante la ejecución del programa.
     - "pases_bien": Número de pases exitosos realizados por la jugadora, se actualiza leyendo el archivo ".txt".
     - "pases_mal": Número de pases no exitosos realizados por la jugadora, también se actualiza durante la ejecución.
     - "total_pases": Suma total de "pases_bien` y `pases_mal", proporcionando el total de intentos de pases de la jugadora.
     - "porcentaje": Representa el porcentaje de éxito en los pases de la jugadora. Se calcula luego de la lectura. 

2. Definición de la función "contar_pases_y_efectividad()":
    Esta función coordina el flujo principal del procesamiento de datos de pases de jugadoras y la preparación de los mismos para su presentación final.
    Proceso:
    - Lectura de Archivo: Primero, abre y lee el archivo 'pases.txt', ubicado en el mismo directorio que el script.
        - "with open("pases.txt", "r") as archivo": Abre el archivo en modo lectura.
        - "for linea in archivo": Itera sobre cada línea del archivo.
        - "datos = linea.strip().split(";")": ".strip()" procesa cada línea para eliminar espacios en blanco o saltos de línea y ".split(";")" divide la línea en partes usando ';' como delimitador.
        retornando entonces la linea de texto partida en diferentes elementos que se guardan en la lista "datos".
            - "datos[0]": Nombre del equipo (p.ej., "Argentina" o "Australia").
            - "datos[1]": Número de camiseta.
            - "datos[2]": Nombre de la jugadora.
            - "datos[3]": Resultado del pase ('1' para exitoso, '0' para fallido).
            - "datos[4]": Minuto del juego en que se realizó el pase.
    - A continuación, se realizan llamadas a varias funciones que permiten las siguientes funcionalidades:
    - Actualización de Estadísticas: Utiliza "añadir_estadisticas()" para actualizar las estadísticas basadas en los datos extraídos.
        - los argumentos pasados a "añadir_estadisticas(datos[0], datos[1], datos[3])" se obtuvieron en el paso anterior y son los que se necesitan para actualizar las estadísticas
    - Cálculo de Promedios: Utiliza "calcular_promedios()" para calcular y actualizar el porcentaje de pases exitosos una vez completada la actualización de estadísticas.
    - Ordenamiento de Jugadoras: Utiliza "ordenar_jugadoras()" para ordenar a las jugadoras dentro de cada equipo basado en el porcentaje de pases exitosos. 
    - Preparación de Datos para Salida: retorna el retorno de la llamada a la función "preparar_datos_para_salida()".
        - Esto permite que se retornen los datos en el formato deseado

3. Definición de la función "añadir_estadisticas(pais, numero_camiseta, resultado)":
    Esta función actualiza las estadísticas de una jugadora específica basándose en los resultados de un pase individual.
    Permite mantener actualizadas las estadísticas de cada jugadora a medida que se procesan los datos del archivo 'pases.txt'.
    Argumentos: son elementos de la lista "datos" que se genera en la lectura de cada linea del archivo ".txt"
    Proceso:
    - Acceder al diccionario de la jugadora específica mediante su número de camiseta en formato string
    - jugadora = equipos[pais][numero_camiseta]:
        - Pasando "pais" y "numero_camiseta" al diccionario equipos, obtenemos la clave que representa a la jugadora
        - La variable "jugadora" se convierte en una referencia directa a este diccionario, lo que permite la modificación en tiempo real de las estadísticas almacenadas. 
        - A traves de la nueva variable, se puede modificar el valor de la key obtenida
    - Modificación de valores de la key obtenida (que representa a la jugadora):
        - Incrementa el valor "total_pases" en 1 de forma independiente al resultado del pase
        - Dependiendo del valor de "resultado", se incrementa "pases_bien" si el resultado es "1" (indicando un pase exitoso), o "pases_mal" si es "0" (indicando un pase fallido).

4. Definición de la función "calcular_promedios()":
    Esta función permite calcular los promedios de los pases de las jugadoras, en base a los valores que se obtuvieron tras las llamadas a la función anterior.
    Proceso:
    - iterar a traves de los equipos:
    - for jugadoras in equipos.values()
        - Este bucle se ejecuta una vez por cada equipo. Se utiliza el método .values() del diccionario, para permitir obtener una vista de los valores del diccionario "equipos"
        - Esto significa, que las claves de equipo son ignoradas, y que se accede directamente a los valores que contienen. 
        - Dado que es una iteración por equipo, en cada iteración, se obtiene el diccionario de jugadoras cuyos valores son sus estadísticas
    - for estadisticas in jugadoras.values()
        - Este bucle se ejecuta una vez por cada jugadora. Recordar que "jugadoras" es el valor de las claves principales de "equipos"
        - Por ende "jugadoras" es también un diccionario, que dentro de si, contiene a su vez, varios diccionarios que representan las estadísticas de cada jugadora
        - usamos ".values" para poder acceder a dichos valores dentro de cada jugadora, representado por "estadísticas"
        - "estadísticas" entonces, es cada uno de los diccionarios de estadisticas de jugadoras
        - por cada "set de estadísticas" se verifica primero que el valor "total_pases" sea mayor a 0 (para asegurarse de que dicah jugadora tiene pases realizados)
        - se calcula el porcentaje modificando el valor "porcentaje" de el diccionario de estadísticas de la jugadora de la iteración actual.
        - estadisticas['porcentaje'] = (estadisticas['pases_bien'] * 100) / estadisticas['total_pases']

5. Definición de la función "ordenar_jugadoras()":
    La función ordenar_jugadoras() se encarga de organizar a las jugadoras dentro de cada equipo 
    según el porcentaje de éxito de sus pases, y esto se hace de mayor a menor.
    Proceso:
    - iterar a traves de los equipos:
        - La ejecución de esta función comienza con un bucle que utiliza for pais, jugadoras in equipos.items(), 
        - lo cual significa que se recorre cada uno de los equipos almacenados en el diccionario equipos. 
        - La función .items() es útil aquí porque devuelve cada par de clave-valor del diccionario, 
        - donde pais es la clave que representa el nombre del país como "Argentina" o "Australia", 
        - y jugadoras es el valor correspondiente que es un diccionario conteniendo todas las jugadoras de ese país. 
        - Cada jugadora está representada por un número de camiseta, y asociado a este número, un diccionario de sus estadísticas.
    - Transformar diccionario de jugadoras en lista de tuplas, para facilitar el ordenamiento:
        - En el siguiente paso, se transforma el diccionario jugadoras en una lista de tuplas para facilitar el ordenamiento. 
        - Esto se logra con la comprensión de lista lista_jugadoras = [(numero, datos) for numero, datos in jugadoras.items()], 
        - donde cada numero es la clave que corresponde al número de camiseta de la jugadora y datos son las estadísticas de esa jugadora. 
        - Estas tuplas luego se ordenan por el porcentaje de pases exitosos utilizando lista_jugadoras.sort(key=lambda x: x[1]['porcentaje'], reverse=True). 
        - Aquí, lambda x: x[1]['porcentaje'] especifica que el criterio de ordenamiento es el valor de 'porcentaje' dentro del diccionario de estadísticas de cada jugadora, 
        - que se accede con x[1] porque x[0] sería el número de la camiseta. 
        - El parámetro reverse=True asegura que el ordenamiento sea descendente, es decir, de mayor a menor porcentaje.
    - Actualizar diccionario "equipos":
        - Finalmente, el diccionario jugadoras dentro del diccionario equipos se actualiza para reflejar este nuevo orden. 
        - Esto se hace con la expresión {numero: datos for numero, datos in lista_jugadoras}, 
        - que reconstruye el diccionario de jugadoras utilizando los pares de clave-valor ordenados de lista_jugadoras. 
        - Este paso es crucial porque asegura que los datos modificados y ordenados se guarden de nuevo en la estructura principal equipos, 
        - permitiendo que los cambios tengan efecto en las operaciones futuras del programa. 
        - En resumen, ordenar_jugadoras() no solo reorganiza los datos de manera que las jugadoras con mejores desempeños queden al principio de cada lista de equipo, 
        - sino que también prepara el conjunto de datos para cualquier procesamiento o análisis posterior que dependa del rendimiento de las jugadoras.

6. Definición de función preparar_datos_para_salida():
    Esta funcion prepara la estructura de datos solicitada en los requerimientos del ejercicio
    Proceso:
    - Primero se declara "resultado_final" que es donde se guarda todos los datos (diccionarios de equipos y jugadoras con sus respectivos diccionarios de datos)
    - for pais, jugadoras in equipos.items():
        - Se itera sobre cada equipo, de nuevo usando el método de diccionario ".items()"
        - Que como se explicó anteriormente devuelve la clave y el valor. Donde país es la clave, y jugadoras el diccionario de jugadoras (el valor)
    - A "jugadoras", que es el diccionario que servía como valor anteriormente, se le aplica ".items()" nuevamente, para obtener su duo clave-valor
        - Donde la clave es el numero de camiseta, y datos es el diccionario de datos de la jugadora, que en este caso es el valor. 
    - Se crea un diccionario por cada jugadora con su numero y estadisticas
    datos_jugadora = {
                "numero": numero_camiseta,
                "nombre": datos["nombre"],
                "cantidad_pases": datos["total_pases"],
                "pases_bien": datos["pases_bien"],
                "pases_mal": datos["pases_mal"],
                "porcentaje": round(datos["porcentaje"], 2) 
            }
    - En cada clave, se le añade el valor correspondiente, numero_camiseta lo obtenemos directamente de la clave tras haber usado "jugadoras.items()"
    - Los datos, son un diccionario que contiene las estadisticas de la jugadora
    - Se le pasa al diccionario datos, la clave del valor que se desea obtener. 
    - En el caso de "porcentaje" se utiliza "round()", que permite redondear el numero a 2 decimales. 
    - Se añade mediante ".append()" el diccionario de las estadisticas o datos de cada jugadora
    - Se recuerda que "lista_jugadoras" es una lista donde se guardan los diccionarios de los datos de las jugadoras
    - Finalmente, a la lista que se declaró al principio "resultado_final" se le agrega el diccionario, usando la clave ontenida en el primer bucle for
    - mediante "for pais, jugadoras in equipos.items()", donde obtenemos el pais actual. 
    - resultado_final.append({pais: lista_jugadoras}) pasamos como clave, el pais que se obtuvo al principio (que es la clave del diccionario incial)
    - y la lista de jugadoras como valor. Recordar, que esta lista, dentro de si, es una lista de diccionarios de datos de jugadoras
    - Por último, se retorna la lista "resultado_final" que es el formato que se solicita en la consigna. 

    7. Ejecución y Salida del Programa:
    - La función "contar_pases_y_efectividad()" se invoca directamente dentro de un "print()". Esta práctica asegura que los resultados procesados se muestren inmediatamente en la consola al ejecutar el script. 
    - La salida final es una lista estructurada de equipos y sus jugadoras, ordenada conforme a los porcentajes de éxito en los pases, siguiendo las especificaciones del desafío.
    - Este enfoque facilita la revisión de los resultados y verifica que el formato de salida cumpla con los requerimientos del desafío, garantizando que la presentación de los datos sea clara y adecuada.
"""

