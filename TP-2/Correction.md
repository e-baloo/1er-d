# TP 2


## Exercice 1

### Question 1
- 15//2 = 7
- 31//2 = 15
- 54//2 = 27
- 125//2 = 62
- 15%2 = 1
- 31%2 = 1
- 54%2 = 0
- 125%2 = 1
  

### Question 2
Si n est pair alors n%2 vaut **0** tandis que si n est impair alors n%2 vaut **1**.


## Exercice 2

| rang | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| caractére | J | ' | @ | 1 | m | e |   | l | a |   | N | S | I |

## Exercice 3

```python	
n = 5
phrase = "le triple de "+ str(n) +" est "+ str(n*3) + "\n"
print(phrase*n)
```

```console
le triple de 5 est 15
le triple de 5 est 15
le triple de 5 est 15
le triple de 5 est 15
le triple de 5 est 15
```

## Exercice 4

| A | B | (A and not B) or (not A and B) |
|---|---|---|
| True | True | False |
| True | False | 0 |
| False | True | 0 |
| False | False | False |

## Exercice 5

### Question 1

Non

### Question 2

```python
print(nombre1, type(nombre1))
print(nombre2, type(nombre2))
```

```console
45 <class 'str'>
2 <class 'str'> 
```

### Question 3

```python
nombre1 = int(input("Entrez un premier nombre : "))
nombre2 = int(input("Entrez un second nombre : "))
somme = nombre1 + nombre2
print(nombre1, "+", nombre2, "=", somme)
```

## Exercice 6

### Question 1

```console
> Entrer votre chiffre bonheur : 5
C'est un bon choix.

> Entrer votre chiffre bonheur : 7
Vous avez choisi le 7, comme 60 % des gens.
C'est un bon choix.
```

### Question 2

```console
> Entrer votre chiffre bonheur : 5

> Entrer votre chiffre bonheur : 7
Vous avez choisi le 7, comme 60 % des gens.
C'est un bon choix.
```

## Exercice 7

```python
nombre = int(input("Entrer un nombre entier : "))
if nombre % 2 == 0:
    print("Le nommbre", nombre, "est pair.")
else :
    print("Le nommbre", nombre, "est impair.")
```

## Exercice 8

### Question 1

| Affectation | v = 5 | v = "5" | v = 5.0 | v = 3 > 5 | v = str(5)
|---|---|---|---|---|---|
| Type de v | int | str | float | bool | str

### Question 2

Donner les valeurs de 27//2 = **13** et 27%2 = **1**

### Question 3

Si texte = "informatique", alors texte[5] vaut : **r**

### Question 4

L’appel de print("5"*3) affiche dans la console le message : **555**

### Question 5

Après la commande v = input("Entrer un entier"), le type de la variable v est : **str**

## Exercice 9

```python
temperature = float(input("Entrer la temperature de l'eau : "))

if temperature <= 0.0:
    print("l'eau est SOLIDE")
elif temperature >= 100.0:
    print("l'eau est GAZEUX")
else:
    print("l'eau est LIQUIDE")

```

## Exercice 10

```python
montant = float(input("Entrer le prix d'acaht : "))

if montant >= 300.0:
    montant = montant * (1.0 - 0.25) # -25%
elif montant >= 100.0:
    montant = montant * (1.0 - 0.1) # -10%

print("la somme a payer est : ", montant)
```

## Exercice 11

```python
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
```

## Exercice 12

```python
masse = float(input("Poids (en kg) : "))
taille = float(input("Taille (en m) : "))

imc = masse / (taille**2) 

corpulence = "normale"
if imc < 18.0:
    corpulence = "maigre"
elif imc > 25.0:
    corpulence = "souroid"

print(f"l'IMC est de : {imc}\nla corpulence est : '{corpulence}'")
```

## Exercice 13

```python
def afficher_resultat(moyenne):
    if moyenne < 8:
        resultat = "Recalé"
    elif moyenne < 10:
        resultat = "Oral"
    elif moyenne < 12:
        resultat = "Passable"
    elif moyenne < 14:
        resultat = "Assez Bien"
    elif moyenne < 16:
        resultat = "Bien"
    elif moyenne < 18:
        resultat = "Très Bien"
    else:
        resultat = "Félicitations"
    
    print(f"Moyenne : {moyenne} - Résultat : {resultat}")

moyenne = float(input("Entrez la moyenne de l'élève au BAC : "))

afficher_resultat(moyenne)
```

## Exercice 14

```python	
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
   
```

## Exercice 15

```python	
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
```

## Exercice 16

```python
poules = int(input("Entrez le nombre de poules 🐔 tués (entier) : "))
chiens = int(input("Entrez le nombre de chiens 🐕 tués (entier) : "))
vaches = int(input("Entrez le nombre de vaches 🐄 tués (entier) : "))
amis = int(input("Entrez le nombre de amis 👦 tués (entier) : "))

point_perdu = (poules * 1) + (chiens * 3) + (vaches * 5) + (amis * 10)

somme = 200 # prix du permis de chasse

if point_perdu > 10:
    somme = somme + ((point_perdu - 10) *10) # 10€ par point perdu au dessus de 10

print(f"Le prix du permis de chasse est de {somme}€ (point perdu : {point_perdu})")
```

## Exercice 17

```python
entier = int(input("Entrez le nombre (entier) : "))
roman = ""

num = entier

if not (1 <= num <= 3999):
     print("L'entier doit être compris entre 1 et 3999.")
     exit()

roman_numeral = ""

# Traitement des milliers (M)
roman_numeral += "M" * (num // 1000)
num %= 1000

# Traitement des centaines (C, CC, CCC, CD, D, DC, DCC, DCCC, CM)
if num >= 900:
    roman_numeral += "CM"
    num -= 900
elif num >= 500:
    roman_numeral += "D"
    num -= 500
elif num >= 400:
    roman_numeral += "CD"
    num -= 400
roman_numeral += "C" * (num // 100)
num %= 100

# Traitement des dizaines (X, XX, XXX, XL, L, LX, LXX, LXXX, XC)
if num >= 90:
    roman_numeral += "XC"
    num -= 90
elif num >= 50:
    roman_numeral += "L"
    num -= 50
elif num >= 40:
    roman_numeral += "XL"
    num -= 40
roman_numeral += "X" * (num // 10)
num %= 10

# Traitement des unités (I, II, III, IV, V, VI, VII, VIII, IX)
if num == 9:
    roman_numeral += "IX"
    num -= 9
elif num >= 5:
    roman_numeral += "V"
    num -= 5
elif num == 4:
    roman_numeral += "IV"
    num -= 4
roman_numeral += "I" * num

roman = roman_numeral

print(f"La conversion en chiffres romains de {entier} est : {roman}")
```