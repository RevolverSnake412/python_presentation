# Définition des fonctions arithmétiques

def addition(nombre1, nombre2):
    return nombre1 + nombre2

def soustraction(nombre1, nombre2):
    return nombre1 - nombre2

def multiplication(nombre1, nombre2):
    return nombre1 * nombre2

def division(nombre1, nombre2):
    if nombre2 != 0:
        return nombre1 / nombre2
    else:
        return "Division par zéro impossible"
