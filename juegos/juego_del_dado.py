def juego_del_dado():
    import random
    cuenta1= 0
    cuenta2= 0
    while cuenta1 < 30 and cuenta2 < 30:
        input("Apreta enter para lanzar un dado")
        a1= random.randint(1,6)
        print("tu numero es",a1)
        a2= random.randint(1,6)
        print("mi numero es", a2)
        cuenta1 +=a1
        if cuenta1 >= 30: 
            break
        cuenta2 +=a2
        if cuenta2 >= 30:
            break
        print("Tu cuenta es",cuenta1,"y mi cuenta", cuenta2 )
    print("Tu cuenta es",cuenta1,"y mi cuenta", cuenta2 )

    if cuenta1 >= 30 and cuenta2 <=30:
        print("Ganaste")
    else:
        print("perdiste")
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    pass


