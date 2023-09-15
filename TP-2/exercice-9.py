temperature = float(input("Entrer la temperature de l'eau : "))

if temperature <= 0.0:
    print("l'eau est SOLIDE")
elif temperature >= 100.0:
    print("l'eau est GAZEUX")
else:
    print("l'eau est LIQUIDE")
