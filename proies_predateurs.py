import tkinter as tk
import random


# variables 

taille = 3
matrice, matrice2, matrice_age = [], [], []
HEIGHT = 500
WIDTH = 500
couleurs = {0 : "lemonchiffon", 1 : "royalblue", 2 : "darkred"}
proie_ini = 5
naissance_proie = 0
age_proie = 10
proie = (1, age_proie)

# création listes
for i in range(taille) :
    matrice.append([])
    for j in range(taille) :
        matrice[i].append((0, 0))

# fonctions

def tours() :
    """effectue un tour complet de simulation"""
    deplacement()
    age("proie")
    print("apres age         " + str(matrice))
    #naissance(naissance_proie)
    affichage()
    canvas.after(500, tours)

def affichage() :
    for i in range(taille) :
        for j in range(taille) :
            canvas.itemconfigure(cases[j][i], fill=couleurs[matrice[i][j][0]])

def deplacement() :
    global matrice, matrice2, cpt, i
    matrice2 = matrice
    #matrice[0][0] = proie
    #matrice[0][0] = (1, 1)
    print("av deplacement    " + str(matrice))
    #random_ligne, random_colonne = 1, 1
    for i in range(taille) :
        cpt = 0
        for j in matrice[i] :
            if j[0] == 0 :
                cpt += 1
                continue
            elif j[0] != 0 and i == 0 and cpt == 0 :  # coin haut gauche
                case_occuper(matrice, i, i+1, cpt, cpt+1, 0, matrice[i][cpt])
                matrice2[i][cpt] = (0, 0)
                matrice2[random_ligne][random_colonne] = j
                #age_matrice()
                cpt += 1
            elif j[0] != 0 and i == 0 and cpt == taille-1 :  # coin haut droit
                case_occuper(matrice, i, i+1, cpt-1, cpt, 0, matrice[i][cpt])
                matrice2[i][cpt] = (0, 0)
                matrice2[random_ligne][random_colonne] = j
                #age_matrice()
                cpt += 1
            elif j[0] != 0 and i == taille-1 and cpt == 0 :  # coin bas gauche
                case_occuper(matrice, i-1, i, cpt, cpt+1, 0, matrice[i][cpt])
                matrice2[i][cpt] = (0, 0)
                matrice2[random_ligne][random_colonne] = j
                #age_matrice()
                cpt += 1
            elif j[0] != 0 and i == taille-1 and cpt == taille-1 :  # coin bas droite
                case_occuper(matrice, i-1, i, cpt-1, cpt, 0, matrice[i][cpt])
                matrice2[i][cpt] = (0, 0)
                matrice2[random_ligne][random_colonne] = j
                #age_matrice()
                cpt += 1
            elif j[0] != 0 and i == 0 and 0 < cpt < taille-1 :  # ligne haut
                case_occuper(matrice, i, i+1, cpt-1, cpt+1, 0, matrice[i][cpt])
                matrice2[i][cpt] = (0, 0)
                matrice2[random_ligne][random_colonne] = j
                #age_matrice()
                cpt += 1
            elif j[0] != 0 and i == taille-1 and 0 < cpt < taille-1 :  # ligne bas
                case_occuper(matrice, i-1, i, cpt-1, cpt+1, 0, matrice[i][cpt])
                matrice2[i][cpt] = (0, 0)
                matrice2[random_ligne][random_colonne] = j
                #age_matrice()
                cpt += 1
            elif j[0] != 0 and 0 < i < taille-1 and cpt == 0 :  # colonne gauche
                case_occuper(matrice, i-1, i+1, cpt, cpt+1, 0, matrice[i][cpt])
                matrice2[i][cpt] = (0, 0)
                matrice2[random_ligne][random_colonne] = j
                #age_matrice()
                cpt += 1
            elif j[0] != 0 and 0 < i < taille-1 and cpt == taille-1 :  # colonne droite
                case_occuper(matrice, i-1, i+1, cpt-1, cpt, 0, matrice[i][cpt])
                matrice2[i][cpt] = (0, 0)
                matrice2[random_ligne][random_colonne] = j
                #age_matrice()
                cpt += 1
            else :
                case_occuper(matrice, i-1, i+1, cpt-1, cpt+1, 0, matrice[i][cpt])
                matrice2[i][cpt] = (0, 0)
                matrice2[random_ligne][random_colonne] = j
                #age_matrice()
                cpt += 1
    matrice = matrice2
    print("apres deplacement "+str(matrice))
    affichage()
    #canvas.after(250, deplacement)

    return matrice

def case_occuper(matrice, x1, y1, x2, y2, type_individu, pos_ini) :
    """permet de vérifier si une case est occuper a la position matrice[random_ligne][random_colonne]"""
    global random_ligne, random_colonne
    boucle = True
    random_ligne = random.randint(x1, y1)
    random_colonne = random.randint(x2, y2)
    while matrice[random_ligne][random_colonne] != (0, 0) and boucle == True:  # tant que la position est prise on recherche une position libre
        random_ligne = random.randint(x1, y1)
        random_colonne = random.randint(x2, y2)
        if pos_ini != None and random_ligne == i and  random_colonne == cpt :
            boucle = False
    if type_individu != 0 :
        matrice[random_ligne][random_colonne] = type_individu
    return matrice, random_ligne, random_colonne




#def naissance(naissance_individu) :
 #   for i in range(naissance_individu) :
        #case_occuper(matrice, 0, taille-1, 0, taille-1, 1, None)

def age(individu) :
    for i in range(taille) :
        for j in range(taille) :
            if individu == "proie" :
                if matrice[i][j][0] == 0 :
                    continue
                matrice[i][j] = (1, matrice[i][j][1]-1)
                if matrice[i][j][0] != 0 and matrice[i][j][1] <= 0 :
                    matrice[i][j] = (0, 0)
                    print("test             " + str(i) +"    " + str(j))

    return matrice

# tkinter
racine = tk.Tk()
canvas = tk.Canvas(height=HEIGHT, width=WIDTH, bg="black")
bouton1 = tk.Button(text="move", command=tours)

canvas.grid()
bouton1.grid()


# interface début


cases = []

for i in range(taille) :
    cases.append([])
    for j in range(taille) :
        cases[i].append(canvas.create_rectangle(i*(WIDTH/taille), j*(HEIGHT/taille), i*(WIDTH/taille)+WIDTH/taille, j*(HEIGHT/taille)+HEIGHT/taille, fill=couleurs[1]))



# lancement

for i in range(proie_ini) :
    case_occuper(matrice, 0, taille-1, 0, taille-1, proie, None)
affichage()



# pour plus tard faire des déplacements aléatoire et pas de gauche a droite car sinon les trucs se bloquent en haut

tours()
racine.mainloop()