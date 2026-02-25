#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 08:13:30 2026

@author: loic.akamga-kamga@etu.umontpellier.fr
"""

#  TP3  Analyse et correction du bras de lecture d’un disque dur

#  1. Modélisation

#Analyse et correction du bras de lecture d'un disque dur
from math import*
import matplotlib.pyplot as plt
from control.matlab import*
from scipy import signal




#lorqu'on applique la transforme de laplace a l'equation 1 
#ON retrouve la fonction de trafert dont le numerateur est ki 
#et le denominateur un polynome de second degré.
#pour tracer cette fontion de transfert dans python ils nous faut:
    
#premierement déclarer les constantes qui constitue la fonction de transfert 



J = 0.01
Cv = 0.004
K = 10
Ki = 0.05


#deuxiemement definir et tracer la réponse indicielle comme suite 

num = [Ki]
den = [J, Cv, K]
H = tf(num, den)
print('la fonction de transfert  est', H)

y_ind, t = step(H)
plt.plot(t, y_ind)
plt.title('la réponse indicielle')
plt.grid(True)
plt.show()




# 02/ Correction 01 :
    
    

#question 1 : determiner les coefficient a, b et c, pour obtenir en boucle
#fermee un systeme d'ordre 3 avec un pole reel a-282 et deux poles
#complexes definis par un amortissement de 0.707 et avec une pulsation
#propre de 76rd/s.

#pour trouver les constantes a,b,c ils nous faut connaitre la fonction 
#de transfert en boucle fermé. En utilisantt la formune Hbf(p)=C1(p)G(p)/1+C1(p)*G(p)

a=71337
b=34.75     
c=38945                                                                       

#question 2 : implementer ce correcteur sous Python.

numC1 = [6985, 247965]
denC1 = [1, 389]
C1 = tf(numC1, denC1)
BF = feedback(H*C1, 1)
y,T=step(BF)
print('fonction de transfert avec le correcteur c1',C1)
plt.figure('correcteur1')
plt.plot(T.T,y.T)
plt.grid(True)
plt.xlabel('temps')
plt.ylabel('angle' )
plt.title('correcteur1')
plt.show()
y,T=step(C1) 

#question 3 : relever l'erreur de position du systeme corrige (avec un
#retour unitaire). Verifier ce resultat avec un calcul manuel.


#L'erreur de position Ep(p) est généralement définie comme la différence entre 
#la valeur de consigne et la valeur mesuré à  l'intat stable. Pour un système corrigé on a:
#E(p)=Consigne-Valeur finale=1-0.75=0.25



#question 4 : relever le temps de reponse (utiliser la figure, ne faites
#pas de calcul ni autre operation complexe)


#Le temps de réponse est le temps qu'il faut pour que la sortie atteigne 
#95% de la valeur finale.
#la valeur finale a 95% n'est pas atteinte par notre système.







#  03/ correction 02 : 
    
#question 1 : on choisit un correcteur avec un pole a=-1, determiner
#le zero de la fonction de transfert C2(p) pour obtenir une erreur de
#position de 2%

#Le zéro d'une fonction de transfert est un point dans le plan complexe ou le numérateur 
#de la fonction de transfert s'annule. En d'autres termes, un zéro est une valeur de s.
#dans ce cas le zero est obtenue comme suite :
#s+15.65=0 d'ou s=-15.65
    


#question 2 : implementer ce correcteur sous Python et tracer la reponse
#indicielle (avec un retour unitaire).

C2=tf([1,15.65],[1,1])
print('fonction de transfert avec le correcteur c2', C2)
F2BO= H* C1 * C2
F2BF= feedback(F2BO,1)
print('fonction de transfert en boucle fermé')
y2,t=step(F2BF)
plt.plot(t,y2,'r')
plt.grid(True)
plt.title('Reponse indicielle correcteur2')


#Question 3 : relever le temps de reponse (utiliser la figure, ne faites
#pas de calcul ni autre operation complexe)


#Le temps de réponse est le temps qu'il faut pour que la sortie atteigne 
#95% de la valeur finale.
#la valeur finale a 95% est atteinte a 0.2 secondes.





#  04/ CORRECTION 03 :

    

#question 1 : Determiner la fonction de transfert du correcteur C3(p).

#fonction de transfert en boucle fermé
#correction c3 
#(s + 20) / s


#Question 2 : implementer ce correcteur sous Python.

C3=tf([1,20],[1,0])
print('fonction de transfert avec le correcteur c3 est ', C3)
F3BO= H* C1 * C2 *C3
F3BF= feedback(F3BO,1)
print('fonction de transfert en boucle fermé')
y3,t=step(F3BF)
plt.plot(t,y3,'g')
plt.grid(True)
plt.title('Reponses indicielles correcteurs 2 (rouge) et 3 (vert)')
plt.plot([0.11,0.11],[0,1.05],[0.2,0.2],[0,0.95])

#question 3 : relever l'erreur de position du systeme corrige (avec un
#retour unitaire). Verifier ce resultat avec un calcul manuel.


#L'erreur de position Ep(p)  est généralement définie comme la diffÃ©rence entre 
#la valeur de consigne et la valeur mesurÃ©e Ã  l'etat stable. Pour un systeme corrige on a:
#E(p)=Consigne- Valeur finale=1.0-1.0=0
#Donc il n'y a pas d'erreur statique sur notre systeme


#Question 4 : relever le temps de reponse (utiliser la figure, ne faites
#pas de calcul ni autre operation complexe.)



#Le temps de reponse est le temps qu'il faut pour que la sortie atteigne 
#95% de la valeur finale.
#D'aprÃ©s notre trace vert, il atteint la valeur finale a  95% en 0.11 secondes.

# ===== Réponse indicielle C2 seule =====
y2, t2 = step(F2BF)

plt.figure('Correcteur C2 seul')
plt.plot(t2, y2, 'r')
plt.title('Réponse indicielle - Correcteur C2')
plt.xlabel('Temps (s)')
plt.ylabel('Angle')
plt.grid(True)
plt.show()


# ===== Réponse indicielle C3 seule =====
y3, t3 = step(F3BF)

plt.figure('Correcteur C3 seul')
plt.plot(t3, y3, 'g')
plt.title('Réponse indicielle - Correcteur C3')
plt.xlabel('Temps (s)')
plt.ylabel('Angle')
plt.grid(True)
plt.show()


# ===== Superposition C2 et C3 =====
plt.figure('Superposition C2 et C3')
plt.plot(t2, y2, 'r', label='C2')
plt.plot(t3, y3, 'g', label='C3')
plt.title('Superposition des réponses indicielles')
plt.xlabel('Temps (s)')
plt.ylabel('Angle')
plt.legend()
plt.grid(True)
plt.show()














