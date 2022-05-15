# proies-predateurs

Groupe BI TD-01 :
MACHE Ethan
MARTINET--GAULY Neven
MURALY Mathushan
https://github.com/uvsq22101464/proies-predateurs

# Fonctionnement :

Quand le code est éxecuté une fenêtre graphique s'ouvre, l'utilisateur peut alors appuyer sur le bouton "move" pour voir la simulation étape par étape ou alors appuyer sur le bouton juste en dessous "Boucle" pour que la simulation se lance en continue.

# Modification des paramètres :

Avant le lancement du programe l'utilisateur peut changer à sa guise les paramètres suivants :
-taille (modifie le nombre de cases par lignes)
-HEIGHT et WIDTH (modifie la taille de la fenetre graphique)
-proie_ini (modifie le nombre de proie au lancement)
-age_proie (modifie l'age maximum qu'une proie peut atteindre avant de mourir)
-predateur_ini (modifie le nombre de prédateur au lancement)
-age_predateur (modifie l'age maximum qu'un prédateur peut atteindre avant de mourir)
-energie_predateur (modifie le nombre de tour qu'un prédateur peut passer sans avoir manger de proie)
-energie_reproduction (modifie l'énergie qu'un prédateur doit atteindre pour se reproduire)
-miam (modifie le gain d'énergie quand un prédateur mange une proie)
-FLAIR (modifie la distance maximal où un prédateur peut sentir une proie et la traquer)

# Fonctionnement géneral :

A l'éxecution du programe les proies et les prédateurs vont êtres placés aléatoirement sur le canvas (en bleu les proies et en rouge les prédateurs, les cases blanches sont les cases vides) et leurs positions vont être stocké dans une matrice.

A chaque tours une matrice va être créer contenant les cases où les prédateurs ne peuvent pas aller, ce qui va être utilisé pour la fuite des proies.

Ensuite les proies et les prédateurs vont sois fuire si un prédateur est à coter de la proie ou sois se déplacer de manière aléatoire (fonction deplacement), tandis que les prédateurs vont traquer les proies si une est a distance FLAIR ou moins, dans le cas contraire ils se déplacent de manière aléatoire (fonction deplacement) et si un prédateur arrive sur la case d'une proie elle se fait manger et le prédateur gagne de l'énergie (+miam).

Lors du déplacement les proies ne peuvent pas aller sur une case déjà occupé ni se déplacer de plus d'une case (droite, gauche, haut, bas, diagonales), les prédateurs ne peuvent pas aller sur une case occuper par un autre prédateur mais ils peuvent aller sur la case d'une proie afin de la manger et ils se déplacent aussi d'une seule case par tour.

Suite aux déplacement la fonction reprodution_predateur va vérifier l'énergie de chaque prédateur et si elle est supérieur à celle nécessaire pour la reproduction alors l'energie_predateur va être soustraite par l'energie_redateur et un nouveau prédateur va naitre sur une case aléatoire libre.

La fonction reproduction_proie va permettre aux proies de se reproduire si deux proies sont côte à côte et la nouvelle proie va apparaitre autour des ces deux dernières. (Un seul enfant par proie et l'enfant peut se reproduire que aux tours d'après).

Ensuite les fonctions age et faim vont réspéctivement faire vieillir les proies et les prédateurs tout en vérifiant l'age maximum de l'individu, et la tue si l'age maximal est atteint (le calcul se fait dans l'autre sens ex: une proie commence a 10 ans et pert un an à chaque tour). La fonction faim, elle concerne que les prédateurs, qui vont perdre 1 d'énergie à la fin du tour et mourir si l'énergie est inférieur à 0.

Enfin la fonction compteur va compter le nombre de proies et de prédateurs et l'afficher en haut de la fenêtre, elle compare aussi le nombre du tour précedent, et la fonction affichage affiche les proies et les prédateurs sur le canvas.

# Détails

-Attention proie_ini + predateur_ini ne doivent pas dépasser taille².
-Les proies tout comme les prédateurs peuvent ne pas se déplacer.
-Un prédateur peut mourir en se reproduisant si son energie est égale à celle de reproduction.
-La fonction case_occuper ne s'arette pas meme si toute les cases de la grilles sont occuper.
-Si le miam est trop proche de l'énergie necessaire de reproduction il se peut que le programe plante car les prédateurs peuvent dépasser le nombre de cases maximales (ex : 4 cases, 1 proie, 1 prédateurs, miam = 4 * energier_reproduction, ici le prédateur va se reproduire 1 fois par tours et lors de la quatrième fois il n'y aurra plus de places libre et le programe fonctionnera plus).
-La matrice se lit de gauche à droite puis de haut en bas.
-La matrice contient des tuples dont le premier index est l'identifiant (0 : case vide, 1 : proie, 2 : prédateur, 3 : case inaccessible), le second est l'age, le troisième est l'énergie des prédateurs et le dernier est l'énergie de reprodduction.
-Afin d'éviter des problèmes de list index out of range lors de la vérification des positions alentours la matrice est entourré de (3, 3) qui ne sont pas affichés.
