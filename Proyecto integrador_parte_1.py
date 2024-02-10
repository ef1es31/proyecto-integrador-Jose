#PROYECTO INTEGRADOR
#By Jose Gilmar Ramirez Hernandez
#Ada School - Cohete 57

#PARTE 1

'''
El proyecto de este curso consistirá en un videojuego de texto de recorrer laberintos. Este consistirá de laberintos
representados por caracteres ASCII dónde # representará una pared, . un pasillo y P el personaje.
Podrás moverte por el mapa usando las teclas ↑ ↓ ← → de tu teclado.
'''
''' Crea un repositorio de Github para el proyecto, en este repositorio realiza lo siguiente:
        * Crear un archivo README.md con la descripción del proyecto escrita por ti.
        * Crear el archivo main del proyecto.
        * Pedir el nombre del jugador por teclado.
        * Imprimir un mensaje de bienvenida con el nombre.'''


#Solicitud de nombre del jugador a travez de un input guardando el dato en una variable
user_name = input('Ingrese su nombre: ')

#Print de bienvenida al usuario.
print(f'Bienvenido {user_name} al proyecto integrador, disfruta el viaje.')
