masse = float(input("Poids (en kg) : "))
taille = float(input("Taille (en m) : "))

imc = masse / (taille**2) 

corpulence = "normale"
if imc < 18.0:
    corpulence = "maigre"
elif imc > 25.0:
    corpulence = "souroid"

print(f"l'IMC est de : {imc}\nla corpulence est : '{corpulence}'")

