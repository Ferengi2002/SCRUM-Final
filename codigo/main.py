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