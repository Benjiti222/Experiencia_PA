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
            fin="Empate"
        if comp=="papel":
            fin="Compu gana"
        else:
            fin="Usuario gana"
    if person=="papel":
        if person==comp:
            fin="Empate"
        if comp=="piedra":
            fin="Usuario gana"
        else:
            fin="Compu gana"
    if person=="tijera":
        if person==comp:
            fin="Empate"
        if comp=="papel":
            fin="Usuario gana"
        else:
            fin="Compu gana"
    return fin
    pass