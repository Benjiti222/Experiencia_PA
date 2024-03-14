import random

def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    ns = ""
    
    for i in range(9):
        ns += str(random.randint(0,9))

    print(f"Recuerda el número telefónico! {ns}")
    ni = input("Reescribe el número: ")

    if ni == ns:
        print(f"Correcto! El número era {ni}")
    else:
        print(f"Incorrecto! El número correcto era {ns} y escribiste {ni}")