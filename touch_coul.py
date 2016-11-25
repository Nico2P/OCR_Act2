# Script en Python d'un mini jeu en console de touché coulé très simpliste

from random import randint

# Plateau vide
plateau = []

for x in range(0, 5):
    plateau.append(["O"] * 5)

def afficher_plateau(plateau):
    for ligne in plateau:
        print " ".join(ligne)

afficher_plateau(plateau)

def alea_ligne(plateau):
    return randint(1, len(plateau) - 1) 

def alea_col(plateau):
    return randint(1, len(plateau[0]) - 1)

bateau_x = alea_ligne(plateau)
bateau_y = alea_col(plateau)

for tour in range(4):
    tir_x = int(raw_input("Quelle ligne ?"))
    tir_y = int(raw_input("Quelle colonne ?"))

    if bateau_x == tir_x and bateau_y == tir_y:
        print "Bravo ! Vous avez eu mon bateau !"
        break
    else:
        if (tir_x < 0 or tir_x > 5) or (tir_y < 0 or tir_y > 5):
            print "Oups ! Vous devez viser l'ocean."
        elif (plateau[tir_x -1][tir_y -1] == "X"):
            print "Cette case est deja decouverte."
        else:    
            print "Dommage !"
            plateau[tir_x -1][tir_y -1] = "X"
            afficher_plateau(plateau)
        print tour + 1
if tour == 3:
    print "Game Over"