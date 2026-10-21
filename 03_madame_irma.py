# Récupération des informations pour Mme Irma lol
prenom = input("ton prénom ? ")
age = int(input("ton age ? "))
annee_naissance = 2026 - age

# Prédictions
if age < 18:
    prediction = "ton chat va ouvrir une chaîne YouTube sur les croquettes et devenir plus riche que toi !"
elif age <= 30:
    prediction = "tu vas inventer une application pour traduire les aboiements de chiens en poésie et devenir millionnaire !"
elif age <= 60:
    prediction = "tu vas maîtriser Python en 3 jours et ton prof va te demander de lui donner des cours particuliers !"
else:
    prediction = "tu vas être sélectionné pour le premier championnat du monde de tricot de l'extrême sur un volcan !"

# Affichage  
print()
print(f"Madame Irma voit tout, {prenom} !")
print(f"Tu es né(e) vers {annee_naissance}.")
print(f"Dans 10 ans, tu auras {age + 10} ans.")
print(f"Prédiction : {prediction} .")
