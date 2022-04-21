import tkinter as tk
import random


# variables 

taille = 30
matrice, matrice2 = [], []
HEIGHT = 500
WIDTH = 500
couleurs = {0 : "lemonchiffon", 1 : "royalblue", 2 : "darkred"}
proie_ini = 50
naissance_proie = 2
age_proie = 5
proie = (proie_ini, naissance_proie, age_proie)


for i in range(taille) :
    matrice.append([])
    matrice2.append([])
    for j in range(taille) :
        matrice[i].append(0)
        matrice2[i].append(0)

# fonctions

def start() :
    for i in range(proie_ini) :
        case_occuper(matrice, 0, taille-1, 0, taille-1, 1, None)
    #fin_tour()
    naissance(naissance_proie)
    affichage()
    #age("proie")


def affichage() :
    for i in range(taille) :
        for j in range(taille) :
            canvas.itemconfigure(cases[j][i], fill=couleurs[matrice[i][j]])

def deplacement() :
    global matrice, matrice2, cpt, i
    matrice2 = matrice
    for i in range(taille) :
        cpt = 0
        for j in matrice[i] :
            if j == 0 :
                cpt += 1
                continue
            elif j != 0 and i == 0 and cpt == 0 :  # coin haut gauche
                case_occuper(matrice, i, i+1, cpt, cpt+1, 0, matrice[i][cpt])
                matrice2[i][cpt] = 0
                matrice2[random_ligne][random_colonne] = 1
                cpt += 1
            elif j != 0 and i == 0 and cpt == taille-1 :  # coin haut droit
                case_occuper(matrice, i, i+1, cpt-1, cpt, 0, matrice[i][cpt])
                matrice2[i][cpt] = 0
                matrice2[random_ligne][random_colonne] = 1
                cpt += 1
            elif j != 0 and i == taille-1 and cpt == 0 :  # coin bas gauche
                case_occuper(matrice, i-1, i, cpt, cpt+1, 0, matrice[i][cpt])
                matrice2[i][cpt] = 0
                matrice2[random_ligne][random_colonne] = 1
                cpt += 1
            elif j != 0 and i == taille-1 and cpt == taille-1 :  # coin bas droite
                case_occuper(matrice, i-1, i, cpt-1, cpt, 0, matrice[i][cpt])
                matrice2[i][cpt] = 0
                matrice2[random_ligne][random_colonne] = 1
                cpt += 1
            elif j != 0 and i == 0 and 0 < cpt < taille-1 :  # ligne haut
                case_occuper(matrice, i, i+1, cpt-1, cpt+1, 0, matrice[i][cpt])
                matrice2[i][cpt] = 0
                matrice2[random_ligne][random_colonne] = 1
                cpt += 1
            elif j != 0 and i == taille-1 and 0 < cpt < taille-1 :  # ligne bas
                case_occuper(matrice, i-1, i, cpt-1, cpt+1, 0, matrice[i][cpt])
                matrice2[i][cpt] = 0
                matrice2[random_ligne][random_colonne] = 1
                cpt += 1
            elif j != 0 and 0 < i < taille-1 and cpt == 0 :  # colonne gauche
                case_occuper(matrice, i-1, i+1, cpt, cpt+1, 0, matrice[i][cpt])
                matrice2[i][cpt] = 0
                matrice2[random_ligne][random_colonne] = 1
                cpt += 1
            elif j != 0 and 0 < i < taille-1 and cpt == taille-1 :  # colonne droite
                case_occuper(matrice, i-1, i+1, cpt-1, cpt, 0, matrice[i][cpt])
                matrice2[i][cpt] = 0
                matrice2[random_ligne][random_colonne] = 1
                cpt += 1
            else :
                case_occuper(matrice, i-1, i+1, cpt-1, cpt+1, 0, matrice[i][cpt])
                matrice2[i][cpt] = 0
                matrice2[random_ligne][random_colonne] = 1
                cpt += 1
    matrice = matrice2
    affichage()
    return matrice

def case_occuper(matrice, x1, y1, x2, y2, individu, pos_ini) :
    global random_ligne, random_colonne
    boucle = True
    random_ligne = random.randint(x1, y1)
    random_colonne = random.randint(x2, y2)
    while matrice[random_ligne][random_colonne] > 0 and boucle == True:  # tant que la position est prise on recherche une position libre
        random_ligne = random.randint(x1, y1)
        random_colonne = random.randint(x2, y2)
        if pos_ini != None and random_ligne == i and  random_colonne == cpt :
            boucle = False
    if individu != 0 :
        matrice[random_ligne][random_colonne] = individu
    return matrice, random_ligne, random_colonne



def fin_tour() :
    naissance(naissance_proie)
    age()

def naissance(naissance_individu) :
    for i in range(naissance_individu) :
        case_occuper(matrice, 0, taille-1, 0, taille-1, 1, None)

def age(individu) :
    global age_proie
    if individu == "proie" :
        age_proie -= 1


# tkinter
racine = tk.Tk()
canvas = tk.Canvas(height=HEIGHT, width=WIDTH, bg="black")
bouton1 = tk.Button(text="move", command=deplacement)

canvas.grid()
bouton1.grid()


# interface début


cases = []

for i in range(taille) :
    cases.append([])
    for j in range(taille) :
        cases[i].append(canvas.create_rectangle(i*(WIDTH/taille), j*(HEIGHT/taille), i*(WIDTH/taille)+WIDTH/taille, j*(HEIGHT/taille)+HEIGHT/taille, fill=couleurs[1]))


start()


racine.mainloop()