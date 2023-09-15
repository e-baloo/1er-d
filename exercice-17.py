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