while True:
    # Demande à l'utilisateur d'entrer deux nombres
    nombre1 = input("Entrez le premier nombre : ")
    nombre2 = input("Entrez le deuxième nombre : ")

    # Vérifie si les entrées sont des nombres
    if nombre1.isdigit() and nombre2.isdigit():
        # Convertit les nombres en entiers et effectue l'opération
        resultat = int(nombre1) + int(nombre2)
        print("Le résultat de l'addition est :", resultat)
    else:
        print("Veuillez entrer des nombres valides.")
