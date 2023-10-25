"""
Un algoritmo genético es una técnica de optimización que imita el proceso de
selección natural. En este ejemplo, usaremos un algoritmo genético
para encontrar una cadena de caracteres que coincida con una frase objetivo.

"""

import random

# Frase objetivo que deseamos generar
frase_objetivo = "Hola, mundo!"

# Función de evaluación: calcular la aptitud de una cadena
def calcular_aptitud(cadena):
    return sum(1 for a, b in zip(cadena, frase_objetivo) if a == b)

# Generar una cadena aleatoria
def generar_cadena(longitud):
    return ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.!?") for _ in range(longitud))

# Mutación: cambiar aleatoriamente un carácter en la cadena
def mutar(cadena):
    indice = random.randint(0, len(cadena) - 1)
    return cadena[:indice] + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.!?") + cadena[(indice + 1):]

# Crear una población inicial de cadenas aleatorias
def crear_poblacion(num_cadenas, longitud_cadena):
    return [generar_cadena(longitud_cadena) for _ in range(num_cadenas)]

# Algoritmo genético
def algoritmo_genetico(frase_objetivo, num_generaciones, tam_poblacion, tasa_mutacion):
    longitud_cadena = len(frase_objetivo)
    poblacion = crear_poblacion(tam_poblacion, longitud_cadena)

    for generacion in range(num_generaciones):
        poblacion = sorted(poblacion, key=lambda x: -calcular_aptitud(x))
        mejor_cadena = poblacion[0]

        if calcular_aptitud(mejor_cadena) == longitud_cadena:
            return mejor_cadena

        nueva_poblacion = [mejor_cadena]

        for _ in range(1, tam_poblacion):
            padre = random.choice(poblacion)
            madre = random.choice(poblacion)
            punto_cruce = random.randint(1, longitud_cadena - 1)
            hijo = padre[:punto_cruce] + madre[punto_cruce:]
            
            if random.random() < tasa_mutacion:
                hijo = mutar(hijo)

            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    return None

# Ejecutar el algoritmo genético
num_generaciones = 1000
tam_poblacion = 100
tasa_mutacion = 0.01

resultado = algoritmo_genetico(frase_objetivo, num_generaciones, tam_poblacion, tasa_mutacion)

if resultado:
    print(f"Se encontró la frase: {resultado}")
else:
    print("No se encontró la frase objetivo.")


"""
Este código muestra un ejemplo de un algoritmo genético que busca generar una frase objetivo.
La población de cadenas evoluciona a lo largo de las generaciones mediante la selección, el cruce y la mutación.
El objetivo es encontrar una cadena que coincida con la frase objetivo.
"""
