#PROYECTO INTEGRADOR
#By Jose Gilmar Ramirez Hernandez
#Ada School - Cohete 57

#PARTE 3

'''
El proyecto de este curso consistirá en un videojuego de texto de recorrer laberintos. Este consistirá de laberintos
representados por caracteres ASCII dónde # representará una pared, . un pasillo y P el personaje.
Podrás moverte por el mapa usando las teclas ↑ ↓ ← → de tu teclado.
'''
''' Para esta sección del proyecto integrador necesitaremos aprender a manipular la terminal:
    Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, borrar la terminal y e
    imprimir el nuevo número hasta el número 50.
    La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.
    Para borrar la terminal antes de imprimir nuevo contenido usar la instrucción:
    os.system('cls' if os.name=='nt' else 'clear'), para esto se debe importar la librería os'''


#Trabajo con libreria, en las lineas inferiores se importan los recursos utilizados en esta seccion del proyecto
import os
import readchar

#Funcion borrar terminal e imprimir el nuevo número
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Contruccion de la funcion
def manipulate_terminal():
    numbers = 0

    while numbers <= 50:
        print('Presiona la tecla "n" para incrementar el numero')
        print(f'Numero actual: {numbers}')
        presseed_key = readchar.readkey()

        if presseed_key.lower() == 'n':
            numbers += 1
        else:
            break
        clear_terminal()

#Llamado a la funcion
manipulate_terminal()

