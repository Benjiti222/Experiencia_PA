import random

def adivinar_par_o_impar():
    x = input("Par o impar: ")
    N = random.randint(1, 10)  # Genera un número entre 1 y 10
    y = str(input("¿Estás seguro?"))
    if y=="si":
        print("checkpoint1")
        if x.lower() == "par":
            print("checkpoint2")
            if N % 2 == 0:
                R = "Correcto :)"
            else:
                R = "Incorrecto :("
        elif x.lower() == "impar":
            if N % 2 != 0:
                R = "Correcto :)"
            else:
                R = "Incorrecto :("
        print(R)
    elif y=="no":
        x = input("Entonces, ¿par o impar?: ")
        if x.lower() == "par":
            if N % 2 == 0:
                R = "Correcto :)"
            else:
                R = "Incorrecto :("
        elif x.lower() == "impar":
            if N % 2 != 0:
                R = "Correcto :)"
            else:
                R = "Incorrecto :("
        print(R)
    return R


            


    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """
    pass