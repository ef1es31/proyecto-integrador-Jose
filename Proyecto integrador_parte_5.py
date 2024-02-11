# PROYECTO INTEGRADOR
# By Jose Gilmar Ramirez Hernandez
# Ada School - Cohete 57

# PARTE 5

'''
Proyecto integrador Parte 5

Encapsulando el juego en una clase
Ahora que disponemos de muchas más herramientas, podemos notar que reutilizamos la variable que contiene el mapa muchas veces y es molesto llamar funciones desconectadas
enviando el mismo parámetro.
La programación orientada a objetos viene a nuestro rescate!
Implementa la clase Juego, ahora el mapa y las posiciones inicial y final son atributos de esta clase, reescribe todas tus funciones anteriores de forma que sean métodos de
la clase y todo esté encapsulado.
Instanciar el juego y ejecutarlo desde el main

Almacenando mapas en archivos
En lugar de almacenar el mapa en el mismo código, podemos guardarlo en archivos con sus posiciones de inicio y fin y las dimensiones del mapa en la primera línea del archivo,
de esta manera los componentes de la aplicación estarán separados y podremos mejorar la experiencia del juego.
1. Crear una nueva clase JuegoArchivo la cual hereda de Juego,
2. Reescribir el constructor para leer un archivo al azar de una carpeta que contenga los mapas cada vez que se instancia el juego.
    i. Para listar los archivos de un directorio usar os.listdir(path) , esto devolverá una lista con el nombre los archivos en ese directorio
    ii. Para elegir un elemento aleatorio de una lista usar random.choice(lista).
    iii. Note que para poder leer el archivo tenemos que componer el path, una forma de hacerlo es path_completo = f"{path_a_mapas}/{nombre_archivo}
3. Crear un método que lea los datos de estos archivos de mapa y devuelva una cadena que tenga concatenada todas las filas leídas del mapa y las coordenadas de inicio y fin.
   Al final de la lectura antes de retornar usar cadena.strip() para eliminar caracteres en blanco residuales.
'''
# Librerias utilizadas en el proyecto
import os
import random
from typing import List, Tuple
import readchar
from readchar import readkey, key


# clase madre del juego
class Juego:
    def __init__(self, laberinto, punto_inicial, punto_final):
        self.mapa = self.convertir_a_matriz(laberinto)
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def convertir_a_matriz(self, laberinto):
        filas = laberinto.split('\n')[1:]  # Excluye la primera fila con datos de inicio y fin
        matriz = [list(fila) for fila in filas]
        return matriz
    
    def mostrar_mapa(self, eje_x, eje_y):
        self.mapa[eje_x][eje_y] = 'P'
        self.mapa_visual()

    def mapa_visual(self):
        self.clear_terminal()
        for fila in self.mapa:
            print(''.join(fila))
    
    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_loop(self):
        eje_x, eje_y = self.punto_inicial

        while (eje_x, eje_y) != self.punto_final:
            self.mostrar_mapa(eje_x, eje_y)

            pressed_key = readchar.readkey()
            nuevo_eje_x, nuevo_eje_y = eje_x, eje_y

            if pressed_key == key.UP and eje_x > 0 and self.mapa[eje_x - 1][eje_y] != '#':
                nuevo_eje_x -= 1
            elif pressed_key == key.DOWN and eje_x < len(self.mapa) - 1 and self.mapa[eje_x + 1][eje_y] != '#':
                nuevo_eje_x += 1
            elif pressed_key == key.LEFT and eje_y > 0 and self.mapa[eje_x][eje_y - 1] != '#':
                nuevo_eje_y -= 1
            elif pressed_key == key.RIGHT and eje_y < len(self.mapa[0]) - 1 and self.mapa[eje_x][eje_y + 1] != '#':
                nuevo_eje_y += 1

            self.mapa[eje_x][eje_y] = '.'
            eje_x, eje_y = nuevo_eje_x, nuevo_eje_y

        self.mostrar_mapa(eje_x, eje_y)

# Clase heredada para la adición de nuevas funcionalidades al juego
class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        mapa_aleatorio, punto_inicial, punto_final = self.elegir_mapa_aleatorio(path_a_mapas)
        super().__init__(mapa_aleatorio, punto_inicial, punto_final)
    
    def elegir_mapa_aleatorio(self, path_a_mapas):
        archivos_de_mapas = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(archivos_de_mapas)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo:
            contenido_mapa = archivo.read()

        # Leer datos de inicio y fin desde la primera fila
        primer_fila = contenido_mapa.strip().split('\n')[0]
        puntos = list(map(int, primer_fila.split()))
        
        punto_inicial = (puntos[0], puntos[1])
        punto_final = (puntos[2], puntos[3])

        return contenido_mapa.strip(), punto_inicial, punto_final
    
    def ejecutar(self):
        self.main_loop()


# Bloque de codigo para la ejecucion del codigo
# Mensaje de bienvenida al usuario para el inicio del juego
print('Bienvenido al juego del laberinto.')
name_user = input('Ingrese su nombre: ')
print(f'{name_user} el juego está por comenzar, prepárate.')
input('Enter para comenzar...')

# Instanciar el juego con mapas aleatorios
path_a_mapas = os.path.join(os.path.dirname(__file__), 'mapas')
juego_archivo = JuegoArchivo(path_a_mapas)

# Ejecucion del juego
juego_archivo.ejecutar()

# Mensaje de finalización del juego
print(f'Felicitaciones por terminar el juego, {name_user}!')
