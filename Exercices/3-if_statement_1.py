# Demande à l'utilisateur d'entrer un nombre
nombre = input("Entrez un nombre : ")

# Convertit l'entrée en entier
nombre = int(nombre)

# Vérifie si le nombre est pair
if nombre % 2 == 0:
    print(nombre, "est un nombre pair.")
# Si la condition précédente n'est pas remplie, le nombre est impair
else:
    print(nombre, "est un nombre impair.")