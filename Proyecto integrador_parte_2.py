#PROYECTO INTEGRADOR
#By Jose Gilmar Ramirez Hernandez
#Ada School - Cohete 57

#PARTE 2

'''
El proyecto de este curso consistirá en un videojuego de texto de recorrer laberintos. Este consistirá de laberintos
representados por caracteres ASCII dónde # representará una pared, . un pasillo y P el personaje.
Podrás moverte por el mapa usando las teclas ↑ ↓ ← → de tu teclado.
'''
''' Para esta segunda parte debemos aprender a usar la libreria 'readchar' que nos permitira leer un caracter suelto del teclado
    *  Instalar la librería: https://pypi.org/project/readchar/
    *  Investigrar cómo leer un caracter del teclado
    *  Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas y sólo terminará cuando se 
       presione la tecla ↑ indicada como UP'''


#Trabajo con libreria, en las lineas inferiores se importan los recursos utilizados en esta seccion del proyecto
import readchar
from readchar import readkey, key

#Declaracion de la funcion
def read_key():

    Diccionario de teclas especiales
    special_key = {
       key.RIGHT: "Flecha derecha →",
       key.LEFT: "Flecha izquierda ←",
       key.DOWN: "Flecha Abajo ↓",
       key.ENTER: "Enter",
       key.TAB: "Tab",
    }

    #Instrucción de salida del programa
    print("\nPara salir el programa presiona 'Fecha Arriba - UP'.")
    print("Presiona una tecla para iniciar.")

    #Bucle
    while True:
        presseed_key = readchar.readkey()

        if presseed_key == key.UP:
            print("Saliendo...")
            break
        elif presseed_key in special_key:
           pressed_key_name = special_key[presseed_key]
           print(f"Presionaste la tecla: {pressed_key_name}")
        else:
            print(f"Presionaste la tecla: {presseed_key}")

#Llamado de la funcion
read_key()