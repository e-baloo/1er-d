poules = int(input("Entrez le nombre de poules 🐔 tués (entier) : "))
chiens = int(input("Entrez le nombre de chiens 🐕 tués (entier) : "))
vaches = int(input("Entrez le nombre de vaches 🐄 tués (entier) : "))
amis = int(input("Entrez le nombre de amis 👦 tués (entier) : "))

point_perdu = (poules * 1) + (chiens * 3) + (vaches * 5) + (amis * 10)

somme = 200 # prix du permis de chasse

if point_perdu > 10:
    somme = somme + ((point_perdu - 10) *10) # 10€ par point perdu au dessus de 10

print(f"Le prix du permis de chasse est de {somme}€ (point perdu : {point_perdu})")
5
