#!/usr/bin/python
# -*- coding: latin-1 -*-

#EX 4

import numpy as np

#Creez (automatiquement) une matrice A 10 × 10 peuplee avec les nombres de 0 à 99, de gauche à droite et de haut en bas.

#A = np.random.randint(99,size=(10,10))
A= np.arange(100)
A= A.reshape(10,10)
print(A)
print(A.shape)

#— Sélectionnez les parties correspondant aux nombres de 60 à 99, dans une matrice B.

B = A[A>=60]
BB = A[6:10]
print(B)
print(BB)
#— Sélectionnez les multiples de 10 dans A, dans un vecteur y.

y = A[A%10==0]
yy= A[1:10,0]
print(y)
print(yy)

#— Sélectionnez les lignes de 3 à 6 incluses, et les colonnes de 0 à 5 incluses, dans une matrice C.

C = A[3:7,0:6]
print(C)
#— Créez un vecteur z avec les multiples de 3 entre 21 et 48 inclus.

z = np.arange(21,49,3)
zz = A[(20<A)&(A<49)]
zz = zz[zz%3==0]
print(z)
print(zz)

#— Calculez le produit scalaire des multiples de 10 (A) et des multiples de 3.
scal = np.dot(y, z)
print(scal)
#— Pour chaque ligne 60..69, 70..79 jusqu’à 99, calculez le produit scalaire du vecteur correspondant avec le vecteur z.
B = B.reshape(40,1)
z = z.reshape(1,10)
scal_bis = np.dot(B, z)

#exercice AIDS

etat_sante = np.array([0.85, 0.1, 0.05, 0])
transition = np.array([(0.9, 0.07, 0.02, 0.01), (0, 0.93, 0.05, 0.02), (0,0,0.85, 0.15), (0,0,0,1)])
res = np.dot(etat_sante, transition)
print(res)
#ou np.dot(np.transpose(transition),etat_sante)

#exercice shopping

food = np.array([(6,5,3,1),(3,6,2,2),(3,4,3,1)])
shops = np.array([(1.5, 1), (2, 2.5), (5, 4.5), (16, 17)])
result = np.dot(food, shops)
print(result)

#exos TAL
food[1,1]+=1
print(food)
