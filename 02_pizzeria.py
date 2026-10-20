# 1. Les entrées de l'utilisateur
nb_pizzas = int(input("Combien de pizzas ? "))
prix_unitaire = float(input("Prix d'une pizza ? "))

# Calcul du total initial
total = nb_pizzas * prix_unitaire

# Réduction de 10% si plus de 5 pizzas
reduction = 0.0
if nb_pizzas > 5:
    reduction = total * 0.10
    total -= reduction

# Frais de livraison (3€ si total < 20€)
livraison = 0.0
if total < 20:
    livraison = 3.0  # Correction de la majuscule ici
    total += livraison

# Affichage du ticket 
print()
print("=== PIZZA TICKET ===")
print(f"Pizzas : {nb_pizzas} x {prix_unitaire:.2f} €")

if reduction > 0:
    print(f"Réduction : -{reduction:.2f} €")
else:
    print("Réduction : aucune")

if livraison == 0:
    print("Livraison : gratuite")
else:
    print(f"Livraison : {livraison:.2f} €")

print(f"TOTAL : {total:.2f} €")