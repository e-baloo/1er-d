heures = int(input("Nombre d'heure(s) d'utilisation : "))
montant = 0.0

if heures > 5:
    heures_fact = heures - 5
    heures = heures - heures_fact
    montant = montant + (heures_fact * 3.00)

if heures > 2:
    heures_fact = heures - 2
    heures = heures - heures_fact
    montant = montant + (heures_fact * 5.00)

montant = montant + (heures * 7.50)

print("la somme a payer est : ", montant)
