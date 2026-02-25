#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 09:45:25 2026

@author: loic.akamga-kamga@etu.umontpellier.fr
"""

import control.matlab as control
from scipy import signal
import matplotlib.pyplot as plt

def get_index(value,l,e):
    for i in range(len(l)):
        if abs(l[i]-value)<=e:
            break
    return i

def tan_gen(a,b,x,xi):
    y = []
    for i in x:
        y.append(a*(i-xi)+b)
    return y
### 1.1 Methode de Strejc

print("1-Methode de Strejc")


#1 Question 1 H(P)
sys = ((100),(1,10,29,20))
H = control.tf((100),(1,10,29,20))
print("Transfer function :", H)


#2 Question 2 determiner et afficher les zeros 
z,p,k = control.tf2zpk((100),(1,10,29,20))
print("poles:",p)
print("zeros:",z)
print("gain:",k)



#3 Tracer la reponse indicille du systeme

t1, Yind = signal.step(sys)
plt.figure()
plt.plot(t1.T,Yind.T)
plt.title('Reponse indicielle du systeme')
plt.ylabel('Amplitude')
plt.xlabel('Temps(s)')
plt.grid(True)
plt.show()

#4 Tracer la reponse indicille du systeme

t2,Yimp = signal.impulse(sys)
plt.figure()
plt.plot(t2.T,Yimp.T)
plt.title('Reponse impulsionnelle du systeme')
plt.ylabel('Amplitude')
plt.xlabel('Temps(s)')
i = get_index(Yimp.max(), Yimp.T,0)
t_inf = t2.T[i]
print("Amplitude d'inflexion :",Yimp.max())
print("Temps d'inflexion :",t_inf,"sec")
line = [t_inf,t_inf],[0,max(Yimp.T)]
plt.plot(line[0],line[1])
plt.legend(["Hp","t_inflexion"])
plt.grid(True)
plt.show()

#5 Determiner l'equation de la tagente au point i 

i = get_index(t_inf, t1.T,0)
a,b,x,xi = Yimp.max(), Yind.T[i], t1.T[:40], t_inf
d = tan_gen(a,b,x,xi)
plt.figure()
plt.plot(t1.T,Yind.T,t1.T[:40],d)
plt.legend(["Hp","tang(tinf)"])
plt.title('Reponse indicielle du systeme')
plt.ylabel('Amplitude')
plt.xlabel('Temps(s)')
plt.grid(True)
plt.show()
#6 Determiner les valeurs de Strejc 

i = get_index(Yind.max(), d,0.1)
tmax = t1.T[i]
i = get_index(0, d,0.1)
tmin = t1.T[i]
Tu = tmin
Ta = tmax-tmin
print("Ta :", Ta,"sec")
print("Tu :", Tu,"sec")
print("Rapport Tu/Ta :",Tu/Ta)
n = 2
Ta_Taux = 2.7183
Tu2_Taux = 0.2817
taux = Ta/Ta_Taux
Tu2 = taux*Tu2_Taux
r = Tu-Tu2
print("taux :",taux,"sec")
print("r :",r,"sec")
print("n :",n)
num_pade, den_pade = control.pade(r,10)
sys_approx = ((k),(taux,1))
Tp1 = control.tf((k),(taux,1))
Tp2 = control.tf((1),(taux,1))
Tp3 = control.tf(num_pade,den_pade)
Tp = control.series(Tp1, Tp2, Tp3)
print("Approximation :\n"," 5 e^(-0.0996 s)\n--------------------\n  (0.650 s + 1)^2")
Yind2,t3 = control.step(Tp,t1.T)
Yind3,t4 = control.step(H,t1.T)
plt.figure()
plt.plot(t4.T,Yind3.T)
plt.plot(t3.T,Yind2.T)
plt.legend(["Hp","Tp"])
plt.title('Reponse indicielle du systeme (Strejc)')
plt.ylabel('Amplitude')
plt.xlabel('Temps(s)')
plt.grid(True)
plt.show()

### 1.2 Methode de Broida

#1 Tracer la reponse indicielle  de H(P)

print("2-Methode de Broida")
Hp = control.tf([100],[1,10,29,20])
print("Transfer function :", Hp)
yb1, tb1 = control.step(Hp,t1.T)
i = get_index(0.28*max(yb1.T), yb1.T, 0.1)
t_1 = tb1.T[i]
i = get_index(0.4*max(yb1.T), yb1.T, 0.1)
t_2 = tb1.T[i]
print("t1 :", t_1,"sec")
print("t2 :", t_2,"sec")
plt.figure()
plt.plot(tb1.T,yb1.T)
plt.title('Reponse impulsionnelle du systeme avec t1 et t2')
plt.ylabel('Amplitude')
plt.xlabel('Temps(s)')
line1 = [t_1,t_1],[0,0.28*max(yb1.T)]
line2 = [t_2,t_2],[0,0.4*max(yb1.T)]
plt.plot(line1[0],line1[1],line2[0],line2[1])
plt.legend(["Hp","t1","t2"])
plt.grid(True)
plt.show()

#2 Determiner les valeurs de taux et r par la methode de Broida

taux = 5.5*(t_2-t_1)
r = 2.8*t_1-1.8*t_2
print("taux :",taux,"sec")
print("r :",r,"sec")
num_pade, den_pade = control.pade(r,10)
Tpb = control.tf(num_pade,den_pade)
Tpb1 = control.tf((k),(taux,1))
Tpb = control.series(Tpb,Tpb1)
print("Approximation :\n"," 5 e^(-0.3959 s)\n------------------\n   1.167 s + 1")
yb2, tb2 = control.step(Tpb, t1.T)
plt.figure()
plt.plot(tb1.T,yb1.T)
plt.plot(tb2.T,yb2.T)
plt.legend(["Hp","Tp"])
plt.title('Reponse indicielle du systÃ¨me (Broida)')
plt.ylabel('Amplitude')
plt.xlabel('Temps(s)')
plt.grid(True)
plt.show()
#Comparaison Totale
plt.figure()
plt.plot(tb1.T,yb1.T)
plt.plot(tb2.T,yb2.T)
plt.plot(t3.T,Yind2.T)
plt.legend(["Hp","Broida","Strejc"])
plt.title('Comparaison des approximations')
plt.ylabel('Amplitude')
plt.xlabel('Temps(s)')
plt.grid(True)
plt.show()


### Correccteur PID
Hp = control.tf((100),(1,10,29,20))
Ta = 1.7676767676767682
Tu = 0.2828282828282829
K = 100

# Correcteur P

Kc = Ta/(Tu*K)
Cp = control.tf(Kc,1)
Cp = control.series(Cp, Hp)
print("Transfer function :", Hp)
print("Correcteur transfer function P:", Cp)
Cp = control.feedback(Cp)
y1, t1 = control.step(Cp)
y0, t0 = control.step(Hp)
plt.figure()
plt.plot(t1.T,y1.T)
plt.title('Reponse indicielle du systeme avec correcteur P')
plt.ylabel('Amplitude')
plt.xlabel('Temps(s)')
plt.grid(True)
plt.show()

# Correcteur PI

Kc = 0.9*Ta/(Tu*K)
taux_i = 3.3*Tu
Cpi = control.tf((Kc*taux_i,Kc),(taux_i,0))
Cpi = control.series(Cpi, Hp)
print("Correcteur transfer function PI:", Cpi)
Cpi = control.feedback(Cpi)
y2, t2 = control.step(Cpi)
plt.figure()
plt.plot(t2.T,y2.T)
plt.title('Reponse indicielle du systeme avec correcteur PI')
plt.ylabel('Amplitude')
plt.xlabel('Temps(s)')
plt.grid(True)
plt.show()

# Correcteur PID

Kc = 1.2*Ta/(Tu*K)
taux_i = 2*Tu
taux_d = 0.5*Tu
Cpid = control.tf((Kc*taux_i*taux_d,Kc*taux_i,Kc),(taux_i,0))
Cpid = control.series(Cpid, Hp)
print("Correcteur transfer function PID:", Cpid)
Cpid = control.feedback(Cpid)
y3, t3 = control.step(Cpid)
plt.figure()
plt.plot(t3.T,y3.T)
plt.title('Reponse indicielle du systeme avec correcteur PID')
plt.ylabel('Amplitude')
plt.xlabel('Temps(s)')
plt.grid(True)
y1, t1 = control.step(Cp,t2)
y3, t3 = control.step(Cpid,t2)
plt.show()
plt.figure()
plt.plot(t1.T,y1.T)
plt.plot(t2.T,y2.T)
plt.plot(t3.T,y3.T)
plt.legend(["P","PI","PID"])
plt.title('Comparaison des correcteurs avec une reponse indicielle')
plt.ylabel('Amplitude')
plt.xlabel('Temps(s)')
plt.grid(True)
plt.show()
# Methode de Zigler Nicholes en boucle ferme
K0 = 2.7
T0 = 1.16
Kc = 0.6*K0
taux_i = 0.5*T0
taux_d = 0.125*T0
Cpid = control.tf((Kc*taux_i*taux_d,Kc*taux_i,Kc),(taux_i,0))
Cpid = control.series(Cpid, Hp)
print("Correcteur transfer function PID Zigler Nichols:", Cpid)
Cpid = control.feedback(Cpid)
y4, t4 = control.step(Cpid)
plt.figure()
plt.plot(t4.T,y4.T)
plt.title('Reponse indicielle du systeme avec correcteur PID Zigler Nichols BF')
plt.ylabel('Amplitude')
plt.xlabel('Temps(s)')
plt.grid(True)
plt.show()