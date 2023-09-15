# Demander à l'utilisateur d'entrer deux entiers
entier1 = int(input("Entrez le premier entier : "))
entier2 = int(input("Entrez le deuxième entier : "))

# Trouver le plus grand et le plus petit entier
if entier1 > entier2:
    plus_grand = entier1
    plus_petit = entier2
else:
    plus_grand = entier2
    plus_petit = entier1
  
# Vérifier si le plus grand est divisible par le plus petit
if plus_grand % plus_petit == 0:
    print(f"{plus_grand} est divisible par {plus_petit}")
else:
    print(f"{plus_grand} n'est pas divisible par {plus_petit}")