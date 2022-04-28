import tkinter as tk
import random

# variables

taille = 12
matrice, tempo = [], []
HEIGHT = 500
WIDTH = 500
couleurs = {0 : "lemonchiffon", 1 : "royalblue", 2 : "darkred", 3 : "dimgray"}

proie_ini = 60
age_proie = 10
proie = (1, age_proie, None, None)

predateur_ini = 30
age_predateur = 13
energie_predateur = 7
energie_reproduction = 10
miam = 5
predateur = (2, age_predateur, energie_predateur, energie_reproduction)
flair = 2

# création listes
for i in range(taille) :
    matrice.append([])
    for j in range(taille) :
        matrice[i].append((0, 0))
    matrice[i].append((3, 3))
    matrice[i].insert(0, (3, 3))

for i in range(taille+2) :
    tempo.append((3, 3))
matrice.append(tempo)
matrice.insert(0, tempo)

# fonctions

def tours() :
    """effectue un tour complet de simulation"""
    deplacement()
    reproduction_predateur()
    age()
    faim()
    affichage()
    #canvas.after(250, tours)
    for i in range(3) :
        print(matrice[i+1])

def affichage() :
    """affiche les proies et les prédateurs sur le canvas"""
    for i in range(taille) :
        for j in range(taille) :
            canvas.itemconfigure(cases[j][i], fill=couleurs[matrice[i+1][j+1][0]])

def deplacement() :
    """déplace les proies et les prédateurs"""
    global matrice, matrice2, cpt, i
    matrice2 = matrice
    for i in range(len(matrice)) :
        cpt = 0
        for j in matrice[i] :
            if j[0] == 0 or j[0] == 3 :
                cpt += 1
                continue
            if j[0] == 1 :
                case_occuper(matrice, i-1, i+1, cpt-1, cpt+1, matrice[i][cpt])
                matrice2[i][cpt] = (0, 0)
                matrice2[random_ligne][random_colonne] = j
                cpt += 1
            if j[0] == 2 :
                case_occuper(matrice, i-1, i+1, cpt-1, cpt+1, matrice[i][cpt])
                if test == True :
                    matrice2[i][cpt] = (0, 0)
                    matrice2[random_ligne][random_colonne] = j
                cpt += 1
    matrice = matrice2
    affichage()
    return matrice

def case_occuper(matrice, x1, y1, x2, y2, pos_ini) :
    """permet de vérifier si une case est occuper a la position matrice[random_ligne][random_colonne], permet aussi a un prédateurs de manger une proie"""
    global random_ligne, random_colonne, test
    boucle = True
    test = True
    random_ligne = random.randint(x1, y1)
    random_colonne = random.randint(x2, y2)
    while matrice[random_ligne][random_colonne] != (0, 0) and boucle == True :  # tant que la position est prise on recherche une position libre
        random_ligne = random.randint(x1, y1)
        random_colonne = random.randint(x2, y2)
        if pos_ini != None and random_ligne == i and  random_colonne == cpt :
            boucle = False
        if pos_ini != None and matrice[i][cpt][0] == 2 and matrice[random_ligne][random_colonne][0] == 1 :
            matrice[random_ligne][random_colonne] = (matrice[i][cpt][0], matrice[i][cpt][1], matrice[i][cpt][2]+miam, matrice[i][cpt][3])
            matrice[i][cpt] = (0, 0)
            test = False
    return random_ligne, random_colonne, matrice, test


def reproduction_proie() :
    """ajoute une nouvelle proie si elles sont côte à côte"""
    for i in range(taille) :
        for j in range(taille) :
            if matrice[i][j][0] == 1 and matrice[i][j+1] == 1 or matrice[i][j-1] == 1 \
                or matrice[i+1][j] == 1 or matrice[i-1][j] == 1 :
                pass

def reproduction_predateur() :
    """ajoute un prédateur si ils ont assez d'énergie necessaire"""
    for i in range(len(matrice)) :
        for j in range(len(matrice[i])) :
            if matrice[i][j][0] != 2 :
                continue
            if matrice[i][j][2] >= energie_reproduction :
                matrice[i][j] = (matrice[i][j][0], matrice[i][j][1], matrice[i][j][2]-energie_reproduction, matrice[i][j][3])
                case_occuper(matrice, 1, taille, 1, taille, None)
                matrice[random_ligne][random_colonne] = predateur
    return matrice

def age() :
    """réduit l'age des individus et les fait mourir si l'age <= 0"""
    for i in range(len(matrice)) :
        for j in range(len(matrice)) :
            if matrice[i][j][0] == 0 or matrice[i][j][0] == 3 :
                continue
            matrice[i][j] = (matrice[i][j][0], matrice[i][j][1]-1, matrice[i][j][2], matrice[i][j][3])
            if matrice[i][j][0] != 0 and matrice[i][j][1] <= 0 :
                matrice[i][j] = (0, 0)
    return matrice

def faim() :
    """réduit la faim des prédateurs et les fait mourir si la faim <= 0"""
    for i in range(len(matrice)) :
        for j in range(len(matrice)) :
            if matrice[i][j][0] != 2 :
                continue
            else :
                matrice[i][j] = (matrice[i][j][0], matrice[i][j][1], matrice[i][j][2]-1, matrice[i][j][3])
                if matrice[i][j][2] <= 0 :
                    matrice[i][j] = (0, 0)
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
    case_occuper(matrice, 1, taille, 1, taille, None)
    matrice[random_ligne][random_colonne] = proie
for i in range(predateur_ini) :
    case_occuper(matrice, 1, taille, 1, taille, None)
    matrice[random_ligne][random_colonne] = predateur
affichage()

tours()
racine.mainloop()

# pour plus tard faire des déplacements aléatoire et pas de gauche a droite car sinon les trucs se bloquent en haut