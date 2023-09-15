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