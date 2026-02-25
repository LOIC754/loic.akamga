#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 09:27:47 2026

@author: loic.akamga-kamga@etu.umontpellier.fr
"""

#TP1 INITIATION A PYTHON 

#OBJECTIF 
#Sâ€™initier Ã  lâ€™utilisation du langage Python

# PARTIE 1 :squelette de programme

import numpy as np  # Importation de numpy

print("TP Algebre Lineaire !\n\n")  # Affichage du message

# Scalaire
s = 5
print("s vaut \n", s)  # Affichage de s

#  Vecteur ligne
v_ligne = np.array([1, 2, 3, 4, 5, 6, 7])
print("Vecteur ligne v :", v_ligne)  # Affichage du vecteur ligne

# TRAVAIL PRATIQUE 1

#quesioon 1: Definir avec array un vecteur colonne de 7 lignes et lâ€™afficher.
v_colonne = np.array([[1], [2], [3], [4], [5], [6], [7]])  # Matrice (7,1)
print("Vecteur colonne v_colonne :\n", v_colonne)  # Affichage du vecteur colonne


#Question 2 Definir et afficher (methode zeros) une matrice 2x2 de zeros.
M_zeros = np.zeros((2, 2))
print("Matrice 2x2 de zeros :\n", M_zeros)  # Affichage de la matrice

#Question 3 Definir et afficher une matrice 3x4 de valeurs arbitraires,
#nommee M.
M = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print("Matrice 3x4 M :\n", M)  # Affichage de la matrice


#Question 4 Afficher le produit sxM.
produit_sM = s * M
print("Produit sM :\n", produit_sM)  # Affichage du produit 

#Question 5 Afficher la dimension de M.
print("Dimension de M :", M.shape)


#Question 6 Afficher premier et dernier (indice -1) element de v ligne, et
#l'element a la 3 eme ligne et 2eme colonne de M
v_ligne= np.array([1, 2, 3, 4, 5, 6, 7])
print("vecteur  ligne :", v_ligne)
# Affichage du premier et du dernier element de v
print("Premier Ã©lement de v ligne :", v_ligne[0])
print("Dernier Ã©lement de v ligne :", v_ligne[-1])
# Affichage de l'element Ã  la  3eme ligne et 2eme colonne de M
print("Ã©lement Ã  la 3eme ligne et 2eme colonne de M :", M[2, 1])

#Question 7 Definir et afficher (avec la mÃ©thode diag une matrice diagonale
# de dimension et valeurs arbitraires
valeurs_diagonale = np.array([1, 2, 3, 4])

# CrÃ©eons une matrice diagonale en utilisant np.diag
matrice_diagonale = np.diag(valeurs_diagonale)

# Afficher la matrice diagonale
print("Matrice diagonale :\n", matrice_diagonale)

# DÃ©finir la dimension souhaiter pour la matrice 
dimension = 4


#Question 8 DÃ©finir et afficher (avec la mÃ©thode eye) une matrice identitÃ© de dimension arbitraire.


matrice_identite = np.eye(dimension)

# Afficher la matrice identitÃ©
print("Matrice identitÃ© de dimension", dimension, ":\n", matrice_identite)



#Question 9 DÃ©finir deux matrices 2 x 2 arbitraires, nommÃ©es A et B.
# DÃ©finition de la matrice A
A = np.array([[1, 2],
              [3, 4]])

# DÃ©finition de la matrice B
B = np.array([[5, 6],
              [7, 8]])

# Affichage des matrices A ET B 
print("Matrice A :\n", A)
print("Matrice B :\n", B)


#Question 10 Afficher : leur somme, leur multiplication element par element
#et les multiplications matricielles AB et BA.
# 1. SOMME Ã©lÃ©ment par Ã©lÃ©ment
somme = A + B
print("\nSomme de A et B :\n", somme)

# 2. Multiplication Ã©lÃ©ment par Ã©lÃ©ment
multiplication_element_par_element = A * B
print("\nmultiplication_element_par_element  de A et B :\n", multiplication_element_par_element)

# 3. Multiplication matricielle AB
multiplication_AB = np.matmul(A, B)
print("\nMultiplication matricielle AB :\n", multiplication_AB)

# 4. Multiplication matricielle BA
multiplication_BA = np.matmul(B, A)
print("\nMultiplication matricielle BA :\n", multiplication_BA)



#Question 11: Afficher les matrices transposÃ©s de A et de B.
print("\nTransposÃ© de A :\n", A.T)
print("TransposÃ© de B :\n", B.T)



#Question 12 Afficher le dÃ©terminant de C
C = np.array([[1, 2],
              [3, 4]])

# Calcul du dÃ©terminant de C  
determinant = np.linalg.det(C)

# Affichage du dÃ©terminant
print("Le dÃ©terminant de la matrice C est :", determinant) 


#Question 13 Afficher le rang de F
F = np.array([[1, 2, 7],
              [-2, -4, -14]])
print("la matrice F est :\n",F)
# Calcul du rang de F
rang_F = np.linalg.matrix_rank(F)

# Affichage du rang
print("Le rang de la matrice F est :", rang_F)




#Question 14 Afficher l'inverse de X
#  DÃ©finition de la matrice X
X = np.array([[3, 1],
              [0, 1]])
print("la matrice x est :\n",X)
# Calcul de l'inverse de X
X_inv = np.linalg.inv(X)

# Affichage de l'inverse de x
print("L'inverse de la matrice X est :\n", X_inv)

# VÃ©rification en calculant les produits
identite1 = np.dot(X, X_inv)
identite2 = np.dot(X_inv, X)

print("\nProduit de X et X_inv (X * X_inv) :\n", identite1)
print("\nProduit de X_inv et X (X_inv * X) :\n", identite2)



# Questioon 15 DÃ©finir la matrice Y
Y = np.array([[0, 1],
              [1, 1],
              [1, 0]])
print("la matrice Y est :\n",Y)
# Calculer la pseudoinverse de Moore-Penrose de Y
Y_pseudo_inv = np.linalg.pinv(Y)
print("la pseudo inverse est:\n",Y_pseudo_inv)
# VÃ©rifier les conditions Y fois transposer de Y 
YY_inv_Y = np.dot(Y, np.dot(Y_pseudo_inv, Y))  #  Y fois transposer de Y 
Y_inv_YY_inv = np.dot(Y_pseudo_inv, np.dot(Y, Y_pseudo_inv))  # transposer de Y fois Y

# Afficher la pseudoinverse de Y
print("La pseudoinverse de Moore-Penrose de Y est :\n", Y_pseudo_inv)

# VÃ©rification des conditions
print("\nY fois transposer de Y (devrait etre Ã©gal Ã  Y) :\n", YY_inv_Y)
print("\ntransposer de Y fois Y  (devrait etre Ã©gal Ã  transposer de Y ) :\n", Y_inv_YY_inv)




#Question 16 Realiser une fonction compteur5() qui permet de compter et
#d'afficher des valeurs de 0 a 5.
def compteur5():
    """Affiche les nombres de 0 Ã   5 inclus."""
    for i in range(6):
        print(i)

def cube(n):
    """Retourne le cube du nombre n."""
    return n ** 3

# Exemple d'utilisation
compteur5()
print("Le cube de 3 est :", cube(3))




#Partie 2 : simulation des systÃ¨mes asservis


# TRAVAIL PRATIQUE 2

# IMPORTATION DES LIBRAIRIE NECESSAIRE 


import numpy as np  # Importation de numpy
import matplotlib.pyplot as plt 
import control
from control.matlab import *



#Question 17 : 

# la fonction de transfert H :
    
num = [1] 
den = [1, 2, 5] 
H = tf(num, den)
# afficher la fonction de transfert H :
print("Fonction de transfert H:", H)




#Question 18 :
    
# la reponse indicielle a partir de la methode T=STEP(H): 
y,T=step (H) 





#Question 19 : 

# Tracer la rÃ©ponse indicielle en utilisant plt.plot: 

plt.plot(T.T, y.T)
plt.title("Reponse indicielle systeme avec plt")
plt.xlabel("Temps en secondes (s)") 
plt.ylabel("Reponse") 
plt.grid(True) 
plt.show()

#Question 20 : 


def plot_step_response(transfer_function):
    # la rÃ©ponse indicielle du systÃ¨me :
    T, y = step(transfer_function) 


#Tracer la rÃ©ponse indicielle :
    
plt.plot(T, y,'r') 
plt.title("Reponse Indicielle Systeme avec DEF")
plt.xlabel("Temps en secondes (s)") 
plt.ylabel("Reponse") 
plt.grid(True) 
plt.show()
# Appeler la fonction pour tracer la rÃƒÂ©ponse indicielle : 
plot_step_response(H) 
    




