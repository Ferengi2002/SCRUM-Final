import sys
import os

# Añade la ruta de la carpeta 'code' al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from controller import MathController

def main():
    while True:
        controller = MathController()
        controller.run()
        
        repeat = input("¿Quieres jugar otra vez? (sí/no): ").strip().lower()
        if repeat != 'si':
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    main()