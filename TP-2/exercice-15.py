somme = int(input("Entrez la somme a rendre (entier) : "))

if somme // 20 > 0 :
    print(f"{somme // 20} x billets de 20 euros")
    somme = somme % 20

if somme // 10 > 0 :
    print(f"{somme // 10} x billets de 10 euros")
    somme = somme % 10

if somme // 5 > 0 :
    print(f"{somme // 5} x billets de 5 euros")
    somme = somme % 5

if somme // 2 > 0 :
    print(f"{somme // 2} x pieces de 2 euros")
    somme = somme % 2

if somme // 1 > 0 :
    print(f"{somme // 1} x pieces de 1 euros")
    somme = somme % 1
