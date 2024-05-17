def operations_arithmetiques(nombre1, nombre2):
    # Addition
    addition = nombre1 + nombre2

    # Soustraction
    soustraction = nombre1 - nombre2

    # Multiplication
    multiplication = nombre1 * nombre2

    # Division
    if nombre2 != 0:  # Vérifie que le diviseur n'est pas zéro pour éviter une division par zéro
        division = nombre1 / nombre2
    else:
        division = "Division par zéro impossible"

    return addition, soustraction, multiplication, division

# Exemple d'utilisation de la fonction
nombre1 = 10
nombre2 = 5
resultats = operations_arithmetiques(nombre1, nombre2)
print("Résultats des opérations arithmétiques :")
print("Addition :", resultats[0])
print("Soustraction :", resultats[1])
print("Multiplication :", resultats[2])
print("Division :", resultats[3])
