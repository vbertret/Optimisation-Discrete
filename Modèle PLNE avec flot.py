# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:14:53 2020

@author: antoi
"""
from pulp import*
from itertools import combinations
import re

#Création du graphe de départ (Exemple du cours)

A={}
A[1]={2:5,5:4}
A[2]={1:5,5:6,4:4,3:2}
A[3]={2:2,4:3}
A[4]={2:4,3:3,5:2}
A[5]={1:4,2:6,4:2}

#Création du graphe de départ (Exemple de Wikipédia)

G={}
G[1]={2:6,3:3,10:9}
G[2]={1:6,3:4,4:2,5:9}
G[3]={1:3,10:9,9:9,4:2,2:4}
G[4]={3:2,9:8,5:9,2:2}
G[5]={2:9,4:9,9:7,7:5,6:4}
G[6]={5:4,7:1,8:4}
G[7]={5:5,6:1,8:3,9:9}
G[8]={6:4,7:3,9:10,10:18}
G[9]={10:8,3:9,4:8,5:7,7:9,8:10}
G[10]={1:9,3:9,9:8,8:18}

#Création du graphe de départ (Exemple youtube)

D={}
D[1]={2:2,3:5}
D[2]={1:2,3:15,5:10,6:3}
D[3]={1:5,2:15,4:5,5:3}
D[4]={3:5,5:7,6:10,7:12}
D[5]={3:3,4:7,6:1,2:10}
D[6]={2:3,5:1,4:10,7:11}
D[7]={4:12,6:11}

def ModelePLNE_ACM(A):
    #Création du problème :
    prob = LpProblem("ACPM",LpMinimize)
    S = list(A.keys())
    n = len(S)
    VsansSource = S
    s = VsansSource.pop(0)
    #Variable :
    x={}
    for i in A.keys():
        x[i] = {}
        for j in A[i].keys():
            x[i][j] = LpVariable("x_"+str(i)+"_"+str(j),0,1,LpInteger)
            
    f={}
    for i in A.keys():
        f[i] = {}
        for j in A[i].keys():
            f[i][j] = {}
            for t in VsansSource:
                f[i][j][t] = LpVariable("f"+str(i)+str(j)+str(t),0,1,LpInteger)
                    
            
    #Objectif :
    prob += 1/2*lpSum([lpSum([x[i][j]*A[i][j] for j in A[i].keys()] for i in A.keys())])

    #Contraintes :

    for i in A.keys():
        for j in A[i].keys():
            prob += x[i][j] == x[j][i]
            
    for t in VsansSource:
        for a in S:
            if(a not in [s,t]):
                prob += lpSum([f[a][j][t] for j in A[a].keys()]) == lpSum([f[i][a][t] for i in A.keys() if a in list(A[i].keys())])
    
    for t in VsansSource:
        prob += lpSum([f[s][j][t] for j in A[s].keys()]) == 1
        prob += lpSum([f[i][s][t] for i in A.keys() if s in list(A[i].keys())]) == 0
    
    for t in VsansSource:
        prob += lpSum([f[i][t][t] for i in A.keys() if t in list(A[i].keys())]) == 1
        prob += lpSum([f[t][j][t] for j in A[t].keys()]) == 0
        
    prob += lpSum([lpSum([x[i][j] for j in A[i].keys()]) for i in A.keys()]) == 2*(n-1)
    
    for t in VsansSource:
        for i in A.keys():
            for j in A[i].keys():
                prob += f[i][j][t] <= x[i][j]
            
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
    AretesTraites = []
    regexp = re.compile(r"_(\d+)_(\d+)")
    for v in Modele.variables():
        if(v.varValue != 0 and v.name[0] == 'x'):
            result = regexp.search(v.name)
            if result != None:
                i = int(result.group(1))
                j = int(result.group(2))
                if([j,i] not in AretesTraites):
                    AretesTraites.append([i,j])
            print(v.name,"=",v.varValue)
    for arete in AretesTraites:
        print("On garde l'arête {",arete[0],",",arete[1],"}")
    print('Le poids de total de l\'arbre est de : ',value(Modele.objective))
            
AffichageModele(ModelePLNE_ACM(A),"ACPM exemple du cours")
AffichageModele(ModelePLNE_ACM(G),"ACPM exemple Wikipédia")
AffichageModele(ModelePLNE_ACM(D),"ACPM exemple Youtube")