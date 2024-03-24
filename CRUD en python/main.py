import os
import time

def print_options():
        print("AGENDA DE CONTACTOS")
        print("*" * 50)
        print("Selecciona una opcion: ")
        print("[C]rear Contacto")
        print("[L]istado de contactos")
        print("[M]odificar contacto")
        print("[E]liminar Contacto")
        print("[B]uscar contacto")
        print("[S]alir")

'''Aquí lo que hacemos es llamar a la función print_options() y con la función input() recuperamos el
texto escrito en la consola por un usuario, después convertimos en mayúscula el texto introducido para que 
nuestro script acepte un comando tanto
en mayúsculas como en minúsculas.'''
def run():
        print_options()

        command = input()
        command = command.upper()
        ''' '''
        if command == "C":
                pass
        elif command =="L":
                pass
        elif command =="M":
                pass
        elif command =="E":
                pass
        elif command =="B":
                pass
        elif command =="S":
                os._exit(1)

                '''Después comprobamos que comando ha introducido el usuario y si no es un comando válido, 
                mostramos un mensaje, dormimos el script durante un  segundo con time.sleep(1) y volvemos a llamar 
                a la función run() para mostrar el menú de nuevo.'''
        else:
                print("Comando invalido!")
                time.sleep(1)
                run()
        
        '''Al usar if __name__ == "__main__": lo que hacemos es indicar al intérprete de Python que lo que debe ejecutar al 
        lanzarse por consolar python main.py es lo que hay dentro de ello, en este caso la función run() que es la función principal 
        del programa.'''
        if __name__ == "__main__":
                run()