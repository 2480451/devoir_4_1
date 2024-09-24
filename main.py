# Devoir 4 ; problème numéro 4.1
# Programme fait par ED 2024
# Logiciel permettant de déterminer quel type d'achat, en vrac ou en sac, est le plus avantageux

from math import ceil

# CONSTANTES
QUANTITÉ_PETIT_SAC = 2  # Quantité de produit en kg contenue dans un petit sac
QUANTITÉ_GRAND_SAC = 5  # Quantité de produit en kg contenue dans un grand sac
TAUX_RABAIS_PETIT_SAC = 0.10  # Taux rabais obtenu par l'achat d'un petit sac
TAUX_RABAIS_GRAND_SAC = 0.15  # Taux rabais obtenu par l'achat d'un grand sac

# VARIABLES
quantité_désirée: float  # Quantité désirée de produit en kg
prix_base_par_kg: float  # Prix du produit par kg
prix_achat_vrac: float  # Prix total si achat en vrac
prix_base_en_petit_sac: float  # Prix sans rabais pour l'achat en petits sacs
prix_achat_en_petit_sac: float  # Prix final si achat en petits sacs
rabais_achat_en_petit_sac: float  # Montant soustrait au prix de base de l'achat en petits sacs
rabais_achat_en_grand_sac: float  # Montant soustrait au prix de base de l'achat en grands sacs
prix_base_en_grand_sac: float  # Prix sans rabais pour l'achat en grands sacs
prix_achat_en_grand_sac: float  # Prix final si achat en grands sacs
quantité_petit_sac_nécessaire: float
quantité_grand_sac_nécessaire: float
meilleur_prix_achat: float
meilleure_option_achat: str
quantité_réelle_en_petits_sacs: float
quantité_réelle_en_grands_sacs: float
économie_petits_sacs: float
économie_grands_sacs: float

# LOGIQUE
quantité_désirée = float(input("Veuillez saisir la masse désirée du produit (en kg): "))
prix_base_par_kg = float(input("Veuillez saisir le prix de base par kg du produit: "))

prix_achat_vrac = quantité_désirée * prix_base_par_kg
quantité_petit_sac_nécessaire = ceil(quantité_désirée / QUANTITÉ_PETIT_SAC)
quantité_grand_sac_nécessaire = ceil(quantité_désirée / QUANTITÉ_GRAND_SAC)
prix_base_en_petit_sac = (quantité_petit_sac_nécessaire * QUANTITÉ_PETIT_SAC) * prix_base_par_kg
prix_base_en_grand_sac = (quantité_grand_sac_nécessaire * QUANTITÉ_GRAND_SAC) * prix_base_par_kg
rabais_achat_en_petit_sac = TAUX_RABAIS_PETIT_SAC * prix_base_en_petit_sac
rabais_achat_en_grand_sac = TAUX_RABAIS_GRAND_SAC * prix_base_en_grand_sac
prix_achat_en_petit_sac = prix_base_en_petit_sac - rabais_achat_en_petit_sac
prix_achat_en_grand_sac = prix_base_en_grand_sac - rabais_achat_en_grand_sac
quantité_réelle_en_petits_sacs = quantité_petit_sac_nécessaire * QUANTITÉ_PETIT_SAC
quantité_réelle_en_grands_sacs = quantité_grand_sac_nécessaire * QUANTITÉ_GRAND_SAC
économie_petits_sacs = prix_achat_vrac - prix_achat_en_petit_sac
économie_grands_sacs = prix_achat_en_grand_sac - prix_achat_en_grand_sac

print("")
print(f"Le prix d'achat du produit en vrac est de: {prix_achat_vrac:17.2f} $")
print(f"Le prix d'achat du produit en petits sacs est de: {prix_achat_en_petit_sac:10.2f} $")
print(f"Le prix d'achat du produit en grands sacs est de: {prix_achat_en_grand_sac:10.2f} $")
print("")

if prix_achat_en_petit_sac < prix_achat_vrac and prix_achat_en_petit_sac < prix_achat_en_grand_sac:
    meilleure_option_achat = "petits sacs"
    print(f"La meilleure option est l'achat en {meilleure_option_achat}.")
elif prix_achat_en_grand_sac < prix_achat_vrac and prix_achat_en_grand_sac < prix_achat_en_petit_sac:
    meilleure_option_achat = "grands sacs"
    print(f"La meilleure option est l'achat en {meilleure_option_achat}.")
else:
    meilleure_option_achat = "vrac"
    print(f"La meilleur option est l'achat en {meilleure_option_achat}.")

if meilleure_option_achat == "petits sacs":
    print(f"La quantité réelle achetée sera de {quantité_réelle_en_petits_sacs} kg.")
    print(f"L'économie sera de {économie_petits_sacs:.2f} $ par rapport à l'achat en vrac.")
elif meilleure_option_achat == "grands sacs":
    print(f"La quantité réelle achetée sera de {quantité_réelle_en_grands_sacs} kg.")
    print(f"L'économie sera de {économie_grands_sacs:.2f} $ par rapport à l'achat en vrac.")
