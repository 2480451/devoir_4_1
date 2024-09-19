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
prix_achat_en_petit_sac: float  # Prix
prix_achat_en_grand_sac: float
quantité_petit_sac_nécessaire: float
quantité_grand_sac_nécessaire: float
meilleure_option_achat: str
meilleur_prix_achat: float

# LOGIQUE
quantité_désirée = float(input("Veuillez saisir la masse désirée du produit: "))
prix_base_par_kg = float(input("Veuillez saisir le prix de base par kg du produit: "))

prix_achat_vrac = quantité_désirée * prix_base_par_kg
quantité_petit_sac_nécessaire = ceil(quantité_désirée / QUANTITÉ_PETIT_SAC)
quantité_grand_sac_nécessaire = ceil(quantité_désirée / QUANTITÉ_GRAND_SAC)
prix_achat_en_petit_sac = (quantité_petit_sac_nécessaire * QUANTITÉ_PETIT_SAC) * prix_base_par_kg
prix_achat_en_grand_sac = (quantité_grand_sac_nécessaire * QUANTITÉ_GRAND_SAC) * prix_base_par_kg

meilleur_prix_achat = prix_achat_vrac

if prix_achat_en_petit_sac < prix_achat_vrac or prix_achat_en_grand_sac:
    meilleur_prix_achat = prix_achat_en_petit_sac
elif prix_achat_en_grand_sac < prix_achat_vrac or prix_achat_en_petit_sac:
    meilleur_prix_achat = prix_achat_en_grand_sac

print(f"Le prix d'achat du produit en vrac est de {prix_achat_vrac:.2f} $")
print(f"Le prix d'achat du produit en petits sacs est de {prix_achat_en_petit_sac:.2f} $")
print(f"Le prix d'achat du produit en grands sacs est de {prix_achat_en_grand_sac:.2f} $")


