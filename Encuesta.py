def mostrar_menu():
    print("menu")
    print("1. Responder encuesta")
    print("2. Ver resultados")
    print("3. Salir")
    
def responder_encuesta(encuesta):
    for pregunta, opciones in encuesta.items():
        print(f"\n{pregunta}")
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
            
        respuesta = int(input("Seleccione una opción: "))
        if respuesta in range(1, len(opciones) + 1):
            respuestas[pregunta][respuesta - 1] += 1
        else:
            print("Respuesta inválida. Intente nuevamente.")
            responder_encuesta(encuesta)
            
        
def ver_resultados(respuestas, encuesta):
    for pregunta, conteos in respuestas.items():
        print(f"\n{pregunta}")
        opciones = encuesta[pregunta]
        for i, conteo in enumerate(conteos):
            print(f"{opciones[i]}: {conteo} votos")


encuesta = {
    "¿Cuál es tu animal favorito?": ["Perro", "Gato", "Pájaro", "Pez"],
    "¿Cuál es tu deporte favorito?": ["basketball","Futbol", "softbol"]
}


respuestas = {pregunta: [0] * len(opciones) for pregunta, opciones in encuesta.items()}


while True:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        responder_encuesta(encuesta)
    elif opcion == 2:
        ver_resultados(respuestas, encuesta)
    elif opcion == 3:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
        ValueError
        print("Por favor, ingrese un número.")