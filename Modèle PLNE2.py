# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:14:53 2020

@author: antoi
"""
from pulp import*
from itertools import combinations
import numpy as np


def ModelePLNE (M,P):
    
    #Création du problème :
    prob = LpProblem("ACPM",LpMinimize)
    
    n = np.shape(M)[0]
    m = np.shape(M)[1]
    S = [i for i in range(n)]
    A = [i for i in range(m)]
    
    #Variable :
    x={}
    for i in range(m):
        x[i] = LpVariable("x"+"_"+str(i),0,1,LpInteger)

            
    #Objectif :
    prob += lpSum([x[i]*P[i] for i in A])

    #Contraintes :
    
    prob += lpSum([x[i] for i in A]) == n-1
    
    for k in range(3,n):
        L = list(combinations(S,k))
        for ensemble in L:
            E = []
            for j in A:
                if(np.sum([M[i][j] for i in ensemble]) == 2):
                    E.append(j)
            prob += lpSum([x[a] for a in E])<=k-1
                
    #Retour du problème :
    return(prob)

def AffichageModele(Modele,name):
    Modele.writeLP(name)
    print(Modele)

    # Résolution du problème :
    print("Solve with CBC")
    Modele.solve(PULP_CBC_CMD())
    print("Status :",LpStatus[Modele.status])

    #Affichage de la solution :
    print("Optimal value =",value(Modele.objective))
    print("Optimal solution :")
    for v in Modele.variables():
        if(v.varValue != 0):
            print(v.name,"=",v.varValue, "On choisit l'arête ",v.name)

if __name__ == "__main__":
    
    #Création du graphe de départ (Exemple du cours, Test 1)

    M1 = np.array([[1,1,0,0,0,0,0],
                   [0,1,1,0,1,1,0],
                   [0,0,0,0,0,1,1],
                   [0,0,0,1,1,0,1],
                   [1,0,1,1,0,0,0]])

    P1 = {0:4,1:5,2:6,3:2,4:4,5:2,6:3}

    #Création du graphe de départ (Test 2)

    M2 = np.array([[1,0,1,0,0,0,0,0,0,0,0,0],
                   [1,1,0,0,0,1,1,0,0,0,0,0],
                   [0,1,1,1,1,0,0,0,0,0,0,0],
                   [0,0,0,1,0,0,0,1,0,1,1,0],
                   [0,0,0,0,1,1,0,1,1,0,0,0],
                   [0,0,0,0,0,0,1,0,1,1,0,1],
                   [0,0,0,0,0,0,0,0,0,0,1,1]])

    P2 = {0:2,1:15,2:5,3:5,4:3,5:10,6:3,7:7,8:1,9:10,10:12,11:11}
    
    #Création du graphe de départ (Test 3)
    
    M3 = np.array([[1,1,0,1,0,0,0,0],
                  [1,0,1,0,0,0,1,0],
                  [0,1,1,0,1,1,0,0],
                  [0,0,0,1,1,0,0,1],
                  [0,0,0,0,0,1,1,1]])
    
    P3 = {0:9,1:2,2:6,3:5,4:4,5:4,6:5,7:5}
    
    
    
    AffichageModele(ModelePLNE(M1,P1),"ACPM exemple du cours ")
    AffichageModele(ModelePLNE(M2,P2),"ACPM Test 2")
    AffichageModele(ModelePLNE(M3,P3),"ACPM Test 3")
