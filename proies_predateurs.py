import tkinter as tk
import random

# variables 

taille = 3
matrice = []
HEIGHT = 500
WIDTH = 500
couleurs = {0 : "lemonchiffon", 1 : "royalblue", 2 : "darkred"}


for i in range(taille) :
    matrice.append([])
    for j in range(taille) :
        matrice[i].append(0)
print(matrice)

# fonctions

def affichage() :
    for i in range(taille) :
        for j in range(taille) :
            canvas.itemconfigure(cases[i][j], fill=couleurs[matrice[i][j]])

def deplacement() :
    global matrice
    for i in range(taille) :
        for j in matrice[i] :
            if j == 0 :
                pass
    random_ligne = random.randint(0, taille-1)
    random_colonne = random.randint(0, taille-1)
    while matrice[random_ligne][random_colonne] > 0 :  # tant que la position est prise on recherche une position libre
        random_ligne = random.randint(0, taille - 1)
        random_colonne = random.randint(0, taille - 1)




# tkinter
racine = tk.Tk()
canvas = tk.Canvas(height=HEIGHT, width=WIDTH, bg="black")


canvas.grid()

# interface début

cases = []

for i in range(taille) :
    cases.append([])
    for j in range(taille) :
        cases[i].append(canvas.create_rectangle(i*(WIDTH/taille), j*(HEIGHT/taille), i*(WIDTH/taille)+WIDTH/taille, j*(HEIGHT/taille)+HEIGHT/taille, fill=couleurs[1]))

matrice[1][1] = 2

affichage()

racine.mainloop()