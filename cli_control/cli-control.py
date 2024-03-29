import datetime
import os
import imageio

from control_motor import girar_izquierda, girar_derecha, detener

def mostrar_menu():
    print("Sistema para el control de un motor de corriente directa")
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Menu:")
    print("1. Girar en sentido horario")
    print("2. Girar en sentido antihorario")
    print("3. Detener el motor")
    print("4. Salir")

def mostrar_gif(nombre_archivo):
    try:
        with imageio.get_reader(nombre_archivo) as reader:
            for image in reader:
                os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla
                print("Presiona 'Ctrl + C' para continuar...")
                imageio.imwrite("temp.gif", image)  # Guarda la imagen temporalmente
                os.system("start temp.gif")  # Abre el GIF en el visor de imágenes predeterminado
                input("Presiona Enter para continuar o 'q' para salir...")
                os.remove("temp.gif")  # Elimina el archivo temporal
                break  # Salir después de mostrar una vez
    except FileNotFoundError:
        print("Archivo de GIF no encontrado.")
    except Exception as e:
        print("Error al reproducir el GIF:", e)

def main():
    opcion = '3'
    while opcion != '4':
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            girar_izquierda()
            mostrar_gif("izquierda.gif")
        elif opcion == "2":
            girar_derecha()
            mostrar_gif("derecha.gif")
        elif opcion == "3":
            detener()
            mostrar_gif("detenido.gif")
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
