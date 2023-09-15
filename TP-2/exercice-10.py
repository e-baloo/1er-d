montant = float(input("Entrer le prix d'acaht : "))

if montant >= 300.0:
    montant = montant * (1.0-0.25)
elif montant >= 100.0:
    montant = montant * (1.0-0.1)

print("la somme a payer est : ", montant)
