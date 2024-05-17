# Déclaration d'un tuple de nombres
nombres = (101, 23, 37, 420, 69)

# Initialisation d'un index pour parcourir le tuple
index = 0

# Utilisation d'une boucle while pour parcourir le tuple
while index < len(nombres):
    print("Nombre à l'index", index, "est", nombres[index])
    # Incrémente l'index pour passer à l'élément suivant
    index += 1
