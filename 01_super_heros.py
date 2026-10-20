# Récupération des informations de l'utilisateur
prenom = input("Quel est ton prénom ? ")
animal = input("Quel est ton animal préféré ? ")
couleur = input("Quel est ta couleur préférée ? ")
ville = input("Quel est ta ville ? ")

# Affichage des résultats en f-string
print(f"Ton nom de super-héros : Capitaine {animal} {couleur}")
print(f"Ton QG secret : {ville}")
print(f"Félicitations {prenom}. Votre badge de super-héros a été envoyé à la mairie de {ville} !")