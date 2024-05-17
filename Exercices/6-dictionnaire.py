# Déclaration d'un dictionnaire de fruits avec leurs quantités
fruits = {
    'pomme': 10,
    'banane': 5,
    'orange': 8,
    'fraise': 12,
    'kiwi': 3
}

# Affiche les fruits avec une quantité supérieure à 5
print("Fruits avec une quantité supérieure à 5 :")
for fruit, quantite in fruits.items():
    if quantite > 5:
        print(fruit, ":", quantite)
