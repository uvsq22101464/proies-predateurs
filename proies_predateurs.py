import tkinter as tk
import random

# variables
taille = 30
matrice, tempo = [], []
HEIGHT = 800
WIDTH = 800
couleurs = {0 : "lemonchiffon", 1 : "royalblue", 2 : "darkred"}

proie_ini = 450
age_proie = 15
proie = (1, age_proie, None, None)

predateur_ini = 10
age_predateur = 25
energie_predateur = 13
energie_reproduction = 24
miam = 8
predateur = (2, age_predateur, energie_predateur, energie_reproduction)
FLAIR = 3
spot = False
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
    flair()
    deplacement()
    reproduction_predateur()
    reproduction_proie()
    age()
    faim()
    affichage()
    #canvas.after(500, tours)
    #for i in range(1, taille+1) :
    #print("mat 1 :")
    #    print(matrice[i])
    #print('\n')

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
                if spot == False :  # si le prédateur a pas manger avec FLAIR
                    case_occuper(matrice, i-1, i+1, cpt-1, cpt+1, matrice[i][cpt])
                    if test == True :  # sert quand ya pas de flair du coup il mange aléatoirement
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
    matrice2 = []
    for k in range(len(matrice)) :
        matrice2.append([])
        for l in matrice[k] :
            matrice2[k].append(l)
    for i in range(1, len(matrice)-1) :
        for j in range(1, len(matrice[i])-1) :
            if matrice2[i][j][0] != 1 :
                continue
            else :
                if matrice2[i][j][0] == 1 and matrice2[i][j+1][0] == 1 and not \
                    (matrice[i+1][j][0] != 0 and matrice[i-1][j][0] != 0 and matrice[i][j+1][0] != 0 and matrice[i][j-1][0] != 0 and matrice[i-1][j-1][0] != 0 \
                        and matrice[i-1][j+1][0] != 0 and matrice[i+1][j-1][0] != 0 and matrice[i+1][j+1][0] != 0 \
                            and matrice[i-1][j+2][0] != 0 and matrice[i][j+2][0] != 0 and matrice[i+1][j+2][0] != 0) :  # si c'est cote a cote
                    case_occuper(matrice, i-1, i+1, j-1, j+2, None)
                    matrice[random_ligne][random_colonne] = proie
                    matrice2[i][j], matrice2[i][j+1] = (0, 0), (0, 0)
                elif matrice2[i][j][0] == 1 and matrice2[i+1][j][0] == 1 and not \
                    (matrice[i+1][j][0] != 0 and matrice[i-1][j][0] != 0 and matrice[i][j+1][0] != 0 and matrice[i][j-1][0] != 0 and matrice[i-1][j-1][0] != 0 \
                        and matrice[i-1][j+1][0] != 0 and matrice[i+1][j-1][0] != 0 and matrice[i+1][j+1][0] != 0 \
                            and matrice[i+2][j-1][0] != 0 and matrice[i+2][j][0] != 0 and matrice[i+2][j+1][0] != 0) :  # si c'est cote a cote
                    case_occuper(matrice, i-1, i+2, j-1, j+1, None)
                    matrice[random_ligne][random_colonne] = proie
                    matrice2[i][j], matrice2[i+1][j] = (0, 0), (0, 0)
            
    #print(matrice2)
    return matrice

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

def flair() :
    """permet aux prédateurs de détécter les proies proches et de soit les manger si elles sont a distance de 1 ou alors se rapprocher d'une proie dans la range FLAIR"""
    global spot, matrice
    matrice2 = []
    for a in range(len(matrice)) :  # recopie la matrice pour éviter que le meme prédateur joue deux fois ou plus
        matrice2.append([])
        for b in matrice[a] :
            matrice2[a].append(b)
    for i in range(len(matrice)) :
        for j in range(len(matrice[i])) :
            if matrice[i][j][0] != 2 :
                continue
            else :  # quand u nprédateur est détécter
                proie_proche, proie_coter = [], []
                spot = False
                i_min , i_max, j_min, j_max = 0, 0, 0, 0
                if i-FLAIR < 0 : i_min = -(i-FLAIR)
                if i+FLAIR > taille+1 : i_max = i+FLAIR-taille
                if j-FLAIR < 0 : j_min = -(j-FLAIR)
                if j+FLAIR > taille+1 : j_max = j+FLAIR-taille
                for k in range(i-FLAIR+i_min, i+FLAIR+1-i_max) :  # liste toutes les proies proches de distance FLAIR et met leur position dans la liste proie_proche
                    for l in range(j-FLAIR+j_min, j+FLAIR+1-j_max) :
                        if matrice[k][l][0] == 1 :
                            spot = True
                            proie_proche.append((k, l))
                for m in range(len(proie_proche)):  # fait une liste des proies a distance 1 ou -1 du prédateur nommer proie_coter
                    if i-1 <= proie_proche[m][0] <= i+1 and j-1 <= proie_proche[m][1] <= j+1 and spot == True:
                        proie_coter.append(proie_proche[m])
                if len(proie_coter) != 0 and len(proie_proche) != 0 :
                    choose = random.randint(0, len(proie_coter)-1)
                    if matrice[proie_coter[choose][0]][proie_coter[choose][1]][0] == 1 and matrice2[proie_coter[choose][0]][proie_coter[choose][1]][0] == 1 :
                        matrice2[proie_coter[choose][0]][proie_coter[choose][1]] = (matrice[i][j][0], matrice[i][j][1], matrice[i][j][2]+miam, matrice[i][j][3])
                        matrice2[i][j] = (0, 0)
                elif len(proie_coter) == 0 and len(proie_proche) != 0 :
                    choose = random.randint(0, len(proie_proche)-1)
                    if proie_proche[choose][0] < i : new_i = -1
                    elif proie_proche[choose][0] > i : new_i = 1
                    else : new_i = 0
                    if proie_proche[choose][1] < j : new_j = -1
                    elif proie_proche[choose][1] > j : new_j = 1
                    else : new_j = 0
                    matrice2[i+new_i][j+new_j] = matrice[i][j]
                    matrice2[i][j] = (0, 0)
    
    matrice = matrice2
    return matrice, spot

# tkinter
racine = tk.Tk()
canvas = tk.Canvas(height=HEIGHT, width=WIDTH, bg="black")
bouton1 = tk.Button(text="move", command=tours)
canvas.grid()
bouton1.grid()
#racine.bind("<a>", tours)

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

#tours()
racine.mainloop()
