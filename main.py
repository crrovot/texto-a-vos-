import app

def main():
    print("Presiona Enter para comenzar a grabar, o Ctrl+C para salir.")
    
    while True:
        input("Presiona Enter para grabar: ")
        app.recognize_speech()

if __name__ == "__main__":
    main()
