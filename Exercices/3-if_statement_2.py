# Demande à l'utilisateur d'entrer une température en degrés Celsius
temperature = input("Entrez la température en degrés Celsius : ")

# Convertit l'entrée en flottant
temperature = float(temperature)

# Vérifie la température et affiche un message approprié
if temperature >= 30:
    print("Il fait très chaud! Pensez à boire beaucoup d'eau.")
elif temperature >= 20:
    print("Il fait chaud. C'est une belle journée.")
elif temperature >= 10:
    print("Il fait frais. Vous pourriez avoir besoin d'une veste légère.")
elif temperature >= 0:
    print("Il fait froid. Habillez-vous chaudement.")
else:
    print("Il fait très froid! Restez au chaud à l'intérieur si possible.")
