# Importation des fonctions arithmétiques depuis le module "operations"
from operation_module import addition, soustraction, multiplication, division

# Utilisation des fonctions importées
nombre1 = 10
nombre2 = 5

resultat_addition = addition(nombre1, nombre2)
resultat_soustraction = soustraction(nombre1, nombre2)
resultat_multiplication = multiplication(nombre1, nombre2)
resultat_division = division(nombre1, nombre2)

# Affichage des résultats
print("Résultat de l'addition :", resultat_addition)
print("Résultat de la soustraction :", resultat_soustraction)
print("Résultat de la multiplication :", resultat_multiplication)
print("Résultat de la division :", resultat_division)
