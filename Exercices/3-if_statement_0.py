# Demande à l'utilisateur d'entrer un nombre
nombre =int(input("Entrez un nombre : "))

# Vérifie si le nombre est divisible par 2
if nombre % 2 == 0:
    print(nombre, "est divisible par 2.")

# Vérifie si le nombre est divisible par 3
if nombre % 3 == 0:
    print(nombre, "est divisible par 3.")

# Vérifie si le nombre est divisible par 5
if nombre % 5 == 0:
    print(nombre, "est divisible par 5.")

# Si le nombre n'est pas divisible par 2, 3, ou 5, affiche un message spécifique
if nombre % 2 != 0 and nombre % 3 != 0 and nombre % 5 != 0:
    print(nombre, "n'est pas divisible par 2, 3, ni 5.")
