# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:14:53 2020

@author: antoi
"""
from pulp import*
import numpy as np
from itertools import combinations


def MatriceToList(M):
    Dic = {}
    for i in range(np.shape(M)[0]):
        liste = []
        for j in range(np.shape(M)[1]):
            if(M[i][j] == 1):
                liste.append(j)
        Dic[i] = set(liste)
    return(Dic)

def ModelePLNE (M,P):
    
    #Création du problème :
    prob = LpProblem("ACPM",LpMinimize)
    
    n = len(M.keys())
    m = len(P.keys())
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
        L = list(combination(S,k))
        for ensemble in L:
            E = []
            for arc in A:
                for sommet1 in ensemble:
                    for sommet2 in ensemble:
                        if(sommet1 != sommet2 and arc in M[sommet1] and arc in M[sommet2] and arc not in E):
                            E.append(arc)
            prob += lpSum([x[a] for a in E])<=k-1
                
    #Retour du problème :
    return(prob)



def SolveAndPrint(Modele,name): 
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
            print(v.name,"=",v.varValue)

if __name__ == "__main__":
    
    #Création du graphe de départ (Exemple du cours, Test 1)

    M1 = np.array([[1,1,0,0,0,0,0],
                   [0,1,1,0,1,1,0],
                   [0,0,0,0,0,1,1],
                   [0,0,0,1,1,0,1],
                   [1,0,1,1,0,0,0]])

    P1 = {0:4,1:5,2:6,3:2,4:4,5:2,6:3}
    
    G1 = {0:{0,1},1:{1,2,4,5},2:{5,6},3:{3,4,6},4:{0,2,3}}

    #Création du graphe de départ (Test 2)

    M2 = np.array([[1,0,1,0,0,0,0,0,0,0,0,0],
                   [1,1,0,0,0,1,1,0,0,0,0,0],
                   [0,1,1,1,1,0,0,0,0,0,0,0],
                   [0,0,0,1,0,0,0,1,0,1,1,0],
                   [0,0,0,0,1,1,0,1,1,0,0,0],
                   [0,0,0,0,0,0,1,0,1,1,0,1],
                   [0,0,0,0,0,0,0,0,0,0,1,1]])

    P2 = {0:2,1:15,2:5,3:5,4:3,5:10,6:3,7:7,8:1,9:10,10:12,11:11}
    
    G2 = MatriceToList(M2)
    
    #Création du graphe de départ (Test 3)
    
    M3 = np.array([[1,1,0,1,0,0,0,0],
                  [1,0,1,0,0,0,1,0],
                  [0,1,1,0,1,1,0,0],
                  [0,0,0,1,1,0,0,1],
                  [0,0,0,0,0,1,1,1]])
    
    P3 = {0:9,1:2,2:6,3:5,4:4,5:4,6:5,7:5}
    
    G3 = MatriceToList(M3)
    
    #Création du graphe de départ (Wikipédia)
    
    M4 = np.zeros((10,21))
    
    M4[0][0]=1; M4[0][20]=1; M4[0][16]=1
    M4[1][0]=1; M4[1][1]=1; M4[1][2]=1; M4[1][4]=1
    M4[2][20]=1; M4[2][1]=1; M4[2][3]=1; M4[2][3]=1; M4[2][14]=1; M4[2][15]=1
    M4[3][3]=1; M4[3][2]=1; M4[3][5]=1; M4[3][6]=1
    M4[4][4]=1; M4[4][5]=1; M4[4][7]=1; M4[4][9]=1; M4[4][8]=1
    M4[5][8]=1; M4[5][11]=1; M4[5][10]=1
    M4[6][13]=1; M4[6][9]=1; M4[6][11]=1; M4[6][12]=1
    M4[7][10]=1; M4[7][12]=1; M4[7][18]=1; M4[7][19]=1
    M4[8][17]=1; M4[8][14]=1; M4[8][6]=1; M4[8][7]=1; M4[8][13]=1; M4[8][18]=1
    M4[9][16]=1; M4[9][15]=1; M4[9][17]=1; M4[9][19]=1
    
    G4 = MatriceToList(M4)
    
    
    P4={}
    
    P4[0]=6; P4[1]=4; P4[2]=2; P4[3]=2; P4[4]=9
    P4[5]=9; P4[6]=8; P4[7]=7; P4[8]=4; P4[9]=5
    P4[10]=4; P4[11]=1; P4[12]=3; P4[13]=9; P4[14]=9
    P4[15]=9; P4[16]=9; P4[17]=8; P4[18]=10; P4[19]=18
    P4[20]=3
    
    
    #SolveAndPrint(ModelePLNE(G1,P1),"ACPM exemple du cours ")
    #SolveAndPrint(ModelePLNE(G2,P2),"ACPM Test 2")
    #SolveAndPrint(ModelePLNE(G3,P3),"ACPM Test 3")
    SolveAndPrint(ModelePLNE(G4,P4),"ACPM Wilipédia")

