import speech_recognition as sr

def recognize_speech():
    # Crear un objeto recognizer
    recognizer = sr.Recognizer()

    # Usar el micrófono como fuente
    with sr.Microphone() as source:
        print("Ajustando al ruido ambiental, un momento...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Di algo!")

        try:
            # Escuchar la entrada de audio
            audio = recognizer.listen(source)
            print("Grabación terminada, procesando...")

            # Intentar reconocer la voz usando el servicio de Google
            text = recognizer.recognize_google(audio, language="es-ES")
            print(f"Texto reconocido: {text}")

        except sr.UnknownValueError:
            print("No pude entender lo que dijiste.")
        except sr.RequestError as e:
            print(f"Error de solicitud al servicio de reconocimiento: {e}")

    return text
