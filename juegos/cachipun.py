import random

def cachipun():
    comp=random.randint(0,3)
    if comp==0:
        comp="piedra"
    if comp==1:
        comp="papel"
    if comp==2:
        comp="tijera"
    person=input("piedra, papel o tijera?")
    if person=="piedra":
        if comp==person:
            fin="Compu eligio piedra y hubo un Empate"
        if comp=="papel":
            fin="Compu eligio papel y Compu gana"
        else:
            fin="Compu eligio tijera y Usuario gana"
    if person=="papel":
        if person==comp:
            fin="Compu eligio papel y hubo un Empate"
        if comp=="piedra":
            fin="Compu eligio piedra y Usuario gana"
        else:
            fin="Compu eligio tijera y Compu gana"
    if person=="tijera":
        if person==comp:
            fin="Compu eligio tijera y hubo un Empate"
        if comp=="papel":
            fin="Compu eligio papel y Usuario gana"
        else:
            fin="Compu eligio piedra y Compu gana"
    print(fin)
    return
    pass