import random

# Demande à l'utilisateur le nombre de caractères
caract_nombre = int(input("Combien de caractères veux-tu pour ton mot de passe ? "))

# Si moins de 4 → message d'erreur
if caract_nombre < 4:
    print("Le mot de passe doit contenir au moins 4 caractères.")
else:
    # Tous les caractères possibles
    lettres_min = "abcdefghijklmnopqrstuvwxyz"
    lettres_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chiffres = "0123456789"
    caracteres_speciaux = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"

    # On commence avec 1 caractère de chaque type
    mot_de_passe = (
        random.choice(lettres_min) +
        random.choice(lettres_maj) +
        random.choice(chiffres) +
        random.choice(caracteres_speciaux)
    )

    # On complète le mot de passe jusqu'à atteindre le nombre demandé
    tous_les_caracteres = lettres_min + lettres_maj + chiffres + caracteres_speciaux
    for _ in range(caract_nombre - 4):
        mot_de_passe += random.choice(tous_les_caracteres)

    # On mélange les caractères
    mot_de_passe = ''.join(random.sample(mot_de_passe, len(mot_de_passe)))

    # On affiche le mot de passe
    print("\nVoici ton mot de passe généré :")
    print(mot_de_passe)
