# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 16:04:12 2021


import random

"""on commence par créer la grille vide de base. C'est un tableau de taille 20*10"""


""""

# L'importation de l’ensemble des éléments du paquet tkinter :
from tkinter import *
# Création d'une fenêtre avec la classe Tk :
fenetre = Tk()
# Affichage de la fenêtre créée :
fenetre.mainloop()
"""


param1,param2,param3,param4 = 10,-1,-10,-0.1

def verify(grille):
    if max(grille[0])==0:
        return True
    else :
        return False
    
    
def fonctionheuristique(grille):
    if grille == failgrid:
        return -999
    return param1*nblignes(grille) + param2*nbtrous(grille) + param3*hauteurmax(grille) + param4*hauteurrelative(grille)

def nblignes(grille):
    a=0
    for x in grille:
        if x == [1,1,1,1,1,1,1,1,1,1]:
            a+=1
    return a

def nbtrous(grille):
    a=0
    for i in range(10):
        b = hauteurmaxcolonne(i,grille)
        c = 0
        for j in range(20):
            c+=grille[j][i]
        a+=(b-c)
    return a



def hauteurmax(grille):
    """C'est l'une de nos heuristiques"""
    a = []
    for i in range(0, len(grille[0])):
        a.append(hauteurmaxcolonne(i,grille))
    return max(a)

def hauteurmaxcolonne(colonne,grille):
    """on cherche la hauteur max d'une 
    colonne de la grille considérée"""
    for i in range(0,len(grille)):
        if grille[i][colonne] == 1:
            return 20-i
    return 0

def hauteurrelative(grille):
    hr = 0
    for i in range(9):
        hr+=abs(hauteurmaxcolonne(i,grille)-hauteurmaxcolonne(i+1, grille))
    return hr

def rotationspossibles(piece):
    """on ne compte pas 0 ici, toutes les pièces ont une rotation de base, mis à part
    pour la pièce n°4/O qui n'a pas dautre rotation que celle de base."""
    if piece == 1: #tetromino I
        return 1
    elif piece == 2: #tetromino J
        return 3
    elif piece == 3: #tetromino L
        return 3
    elif piece == 4: #tetromino O
        return 0
    elif piece == 5: #tetromino S
        return 1
    elif piece == 6: #tetromino T
        return 3
    elif piece == 7: #tetromino Z
        return 1
    
def colonnespossibles(piece,rotation):
    """suivant la largeur d'une rotation du tetromino, on pourra le placer sur 
    un certain nombre de colonnes"""
    if piece == 1: #tetromino I
        if rotation == 0:
            return 7
        elif rotation == 1:    
            return 10
    elif piece == 2: # tetromino J
        if rotation == 0:
            return 8
        elif rotation == 1:    
            return 9
        elif rotation == 2:    
            return 8
        elif rotation == 3:    
            return 9
    elif piece == 3: # tetromino L
        if rotation == 0:
            return 8
        elif rotation == 1:    
            return 9
        elif rotation == 2:    
            return 8
        elif rotation == 3:    
            return 9
    elif piece == 4: #tetromino O
         return 9
    elif piece == 5: #tetromino S
        if rotation == 0:
            return 8
        elif rotation == 1:
            return 9
    elif piece == 6: #tetromino T
        if rotation == 0:
            return 8
        elif rotation == 1:    
            return 9
        elif rotation == 2:    
            return 8
        elif rotation == 3:    
            return 9
    elif piece == 7: #tetromino Z
        if rotation == 0:
            return 8
        elif rotation == 1:
            return 9
    return [[0]]
    
    

def placement(piece,grilletests,rotation,colonne):
    grille=grilletests.copy()
    if piece == 1: #tetromino I
        if rotation == 0:
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            a2 = hauteurmaxcolonne(colonne+2, grille)
            a3 = hauteurmaxcolonne(colonne+3, grille)
            b = max(a0,a1,a2,a3)
            if b > 18:
                return failgrid
            c = 19 - b
            grilletests[c][colonne]=1
            grilletests[c][colonne+1]=1
            grilletests[c][colonne+2]=1
            grilletests[c][colonne+3]=1
        elif rotation == 1:    
            a = hauteurmaxcolonne(colonne,grille)
            c = 19-a
            if a > 15:
                return failgrid
            grilletests[c][colonne]=1
            grilletests[c-1][colonne]=1
            grilletests[c-2][colonne]=1
            grilletests[c-3][colonne]=1
    elif piece == 2: # tetromino J
        if rotation == 0:
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            a2 = hauteurmaxcolonne(colonne+2, grille)
            b = max(a0,a1,a2)
            if b > 17:
                return failgrid
            c = 19 - b
            grilletests[c-1][colonne]=1
            grilletests[c][colonne]=1
            grilletests[c][colonne+1]=1
            grilletests[c][colonne+2]=1
        elif rotation == 1:    
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            b = max(a0,a1)
            if b > 16:
                return failgrid
            c = 19 - b
            grilletests[c][colonne]=1
            grilletests[c][colonne+1]=1
            grilletests[c-1][colonne+1]=1
            grilletests[c-2][colonne+1]=1
        elif rotation == 2:    
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            a2 = hauteurmaxcolonne(colonne+2, grille)
            b = max(a0,a1,a2)
            if b > 17:
                return failgrid
            c = 19 - b
            if b!=a2 or b==0:
                grilletests[c-1][colonne]=1
                grilletests[c-1][colonne+1]=1
                grilletests[c-1][colonne+2]=1
                grilletests[c][colonne+2]=1
            elif b>0:
                grilletests[c][colonne]=1
                grilletests[c][colonne+1]=1
                grilletests[c][colonne+2]=1
                grilletests[c+1][colonne+2]=1
        elif rotation == 3:    
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            b = max(a0,a1)
            if b > 16:
                return failgrid
            c = 19 - b
            if b==a1 and b>1:
                grilletests[c][colonne]=1
                grilletests[c][colonne+1]=1
                grilletests[c+1][colonne]=1
                grilletests[c+2][colonne]=1
                return grilletests
            else:
                grilletests[c][colonne]=1
                grilletests[c-1][colonne]=1
                grilletests[c-2][colonne]=1
                grilletests[c-2][colonne+1]=1
    elif piece == 3: # tetromino L
        if rotation == 0:
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            a2 = hauteurmaxcolonne(colonne+2, grille)
            b = max(a0,a1,a2)
            if b > 17:
                return failgrid
            c = 19 - b
            grilletests[c-1][colonne+2]=1
            grilletests[c][colonne]=1
            grilletests[c][colonne+1]=1
            grilletests[c][colonne+2]=1
        elif rotation == 1:    
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            b = max(a0,a1)
            if b > 16:
                return failgrid
            c = 19 - b
            if b==a0 and b>1:
                grilletests[c][colonne]=1
                grilletests[c][colonne+1]=1
                grilletests[c+1][colonne+1]=1
                grilletests[c+2][colonne+1]=1
            else :
                grilletests[c][colonne+1]=1
                grilletests[c-2][colonne]=1
                grilletests[c-1][colonne+1]=1
                grilletests[c-2][colonne+1]=1
        elif rotation == 2:    
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            a2 = hauteurmaxcolonne(colonne+2, grille)
            b = max(a0,a1,a2)
            if b > 17:
                return failgrid
            c = 19 - b
            if b==a0:
                grilletests[c][colonne]=1
                grilletests[c-1][colonne+1]=1
                grilletests[c-1][colonne+2]=1
                grilletests[c][colonne+2]=1
            else:
                grilletests[c][colonne]=1
                grilletests[c-1][colonne]=1
                grilletests[c-1][colonne+1]=1
                grilletests[c-1][colonne+2]=1
        elif rotation == 3:    
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            b = max(a0,a1)
            if b > 16:
                return failgrid
            c = 19 - b
            grilletests[c][colonne]=1
            grilletests[c][colonne+1]=1
            grilletests[c-1][colonne]=1
            grilletests[c-2][colonne]=1
    elif piece == 4: #tetromino O
        a0 = hauteurmaxcolonne(colonne, grille)
        a1 = hauteurmaxcolonne(colonne+1, grille)
        b = max(a0,a1)
        if b > 17:
            return failgrid
        c = 19 - b
        grilletests[c][colonne]=1
        grilletests[c][colonne+1]=1
        grilletests[c-1][colonne]=1
        grilletests[c-1][colonne+1]=1
    elif piece == 5: #tetromino S
        if rotation == 0:
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            a2 = hauteurmaxcolonne(colonne+2, grille)
            b = max(a0,a1,a2)
            if b > 17:
                return failgrid
            c = 19 - b
            if b==a2 and b>0:
                grilletests[c][colonne+1]=1
                grilletests[c][colonne+2]=1
                grilletests[c+1][colonne]=1
                grilletests[c+1][colonne+1]=1
            else:
                grilletests[c][colonne]=1
                grilletests[c][colonne+1]=1
                grilletests[c-1][colonne+1]=1
                grilletests[c-1][colonne+2]=1
        elif rotation == 1:
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            b = max(a0,a1)
            if b > 16:
                return failgrid
            c = 19 - b
            if b==a0 and b>0:
                grilletests[c][colonne]=1
                grilletests[c][colonne+1]=1
                grilletests[c-1][colonne]=1
                grilletests[c+1][colonne+1]=1
            else:
                grilletests[c][colonne+1]=1
                grilletests[c-1][colonne]=1
                grilletests[c-1][colonne+1]=1
                grilletests[c-2][colonne]=1
    elif piece == 6: #tetromino T
        if rotation == 0:
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            a2 = hauteurmaxcolonne(colonne+2, grille)
            b = max(a0,a1,a2)
            if b > 17:
                return failgrid
            c = 19 - b
            grilletests[c-1][colonne+1]=1
            grilletests[c][colonne]=1
            grilletests[c][colonne+1]=1
            grilletests[c][colonne+2]=1
        elif rotation == 1:    
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            b = max(a0,a1)
            if b > 16:
                return failgrid
            c = 19 - b
            if b==a0 and b>0:
                grilletests[c][colonne]=1
                grilletests[c][colonne+1]=1
                grilletests[c-1][colonne+1]=1
                grilletests[c+1][colonne+1]=1
            else:
                grilletests[c][colonne+1]=1
                grilletests[c-1][colonne]=1
                grilletests[c-1][colonne+1]=1
                grilletests[c-2][colonne+1]=1
        elif rotation == 2:    
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            a2 = hauteurmaxcolonne(colonne+2, grille)
            b = max(a0,a1,a2)
            if b > 17:
                return failgrid
            c = 19 - b
            if b==a1 or b==0:
                grilletests[c][colonne+1]=1
                grilletests[c-1][colonne]=1
                grilletests[c-1][colonne+1]=1
                grilletests[c-1][colonne+2]=1
            elif b!=a1 and b>0:
                grilletests[c][colonne]=1
                grilletests[c][colonne+1]=1
                grilletests[c][colonne+2]=1
                grilletests[c+1][colonne+1]=1
        elif rotation == 3:    
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            b = max(a0,a1)
            if b > 16:
                return failgrid
            c = 19 - b
            if b==a1 and b>0:
                grilletests[c][colonne]=1
                grilletests[c][colonne+1]=1
                grilletests[c-1][colonne]=1
                grilletests[c+1][colonne]=1
            else: 
                grilletests[c][colonne]=1
                grilletests[c-1][colonne]=1
                grilletests[c-2][colonne]=1
                grilletests[c-1][colonne+1]=1
    elif piece == 7: #tetromino Z
        if rotation == 0:
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            a2 = hauteurmaxcolonne(colonne+2, grille)
            b = max(a0,a1,a2)
            if b > 17:
                return failgrid
            c = 19 - b
            if b==a0 and b>0:
                grilletests[c][colonne]=1
                grilletests[c][colonne+1]=1
                grilletests[c+1][colonne+1]=1
                grilletests[c+1][colonne+2]=1
            else:
                grilletests[c][colonne+1]=1
                grilletests[c][colonne+2]=1
                grilletests[c-1][colonne]=1
                grilletests[c-1][colonne+1]=1
        elif rotation == 1:
            a0 = hauteurmaxcolonne(colonne, grille)
            a1 = hauteurmaxcolonne(colonne+1, grille)
            b = max(a0,a1)
            if b > 16:
                return failgrid
            c = 19 - b
            if b==a1 and b>0:
                grilletests[c][colonne]=1
                grilletests[c][colonne+1]=1
                grilletests[c-1][colonne+1]=1
                grilletests[c+1][colonne]=1
            else:
                grilletests[c][colonne]=1
                grilletests[c-1][colonne]=1
                grilletests[c-1][colonne+1]=1
                grilletests[c-2][colonne+1]=1
    return grilletests

def clean(grille):
    for x in grille :
        if x == [1,1,1,1,1,1,1,1,1,1]:
            grille.remove(x)
            grille.insert(0,[0,0,0,0,0,0,0,0,0,0])



grid = [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

failgrid = [[1,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]

#print(grid)
ingame=True
nbpieces = 0
while ingame :
    piece = random.randint(1,7)
    a=[]
    b=[]
    
    A= [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            A[i][j] = grid[i][j]
            
    B= [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            B[i][j] = A[i][j]
    
    for i in range(0,rotationspossibles(piece)+1):
        for j in range(0,colonnespossibles(piece,i)):
            a.append(fonctionheuristique(placement(piece,A,i,j)))
            a.append(i)
            a.append(j)
            A= [[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]]
            
            for k in range(len(grid)):
                for l in range(len(grid[0])):
                    A[k][l] = B[k][l] 
                    
    for k in range(0,len(a),3):
        b.append(a[k])
    w = max(b)
    if w == -999:
        ingame = False
    c = b.index(w)
    grid = placement(piece,grid,a[3*c+1],a[3*c+2])
    nbpieces += 1
    clean(grid)
    print("pièce générée : ", piece)
    print("heuristiques :", a)
    print("rotation n° ", a[3*c+1]," | " ,"colonne n° ",a[3*c+2])
    print(grid)

print(nbpieces)
        
            
