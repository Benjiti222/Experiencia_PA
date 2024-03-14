def adivinar_numero():
    import random
    x=random.randint(1,11)
    y=int(input("¿Qué número es?"))
    if x==y:
        print("Correcto")
    else:
        print("Incorrecto")
    pass