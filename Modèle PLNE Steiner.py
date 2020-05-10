# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:14:53 2020

@author: antoi
"""
from pulp import*
from itertools import combinations
import re

def ModelePLNE_Steiner(A,terminaux):
    #Création du problème :
    prob = LpProblem("ACPM",LpMinimize)
    S = list(A.keys())
    n = len(S)
    TerminauxSansSource = terminaux
    s = TerminauxSansSource.pop(0)
    #Variable :
    v={}
    for i in A.keys():
        v[i] = LpVariable("v_"+str(i),0,1,LpInteger)
    
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
            for t in TerminauxSansSource:
                f[i][j][t] = LpVariable("f"+str(i)+str(j)+str(t),0,1,LpInteger)
                    
            
    #Objectif :
    prob += 1/2*lpSum([lpSum([x[i][j]*A[i][j] for j in A[i].keys()] for i in A.keys())])

    #Contraintes :

    for i in A.keys():
        for j in A[i].keys():
            prob += x[i][j] == x[j][i]
            
    for t in TerminauxSansSource:
        for a in S:
            if(a not in [s,t]):
                prob += lpSum([f[a][j][t] for j in A[a].keys()]) == lpSum([f[i][a][t] for i in A.keys() if a in list(A[i].keys())])
    
    for t in TerminauxSansSource:
        prob += lpSum([f[s][j][t] for j in A[s].keys()]) == 1
        prob += lpSum([f[i][s][t] for i in A.keys() if s in list(A[i].keys())]) == 0
    
    for t in TerminauxSansSource:
        prob += lpSum([f[i][t][t] for i in A.keys() if t in list(A[i].keys())]) == 1
        prob += lpSum([f[t][j][t] for j in A[t].keys()]) == 0
        
    prob += lpSum([lpSum([x[i][j] for j in A[i].keys()]) for i in A.keys()]) == 2*(lpSum([v[i] for i in A.keys()])-1)
    
    for t in TerminauxSansSource:
        for i in A.keys():
            for j in A[i].keys():
                prob += f[i][j][t] <= x[i][j]
    
    for i in A.keys():
        for j in A[i].keys():
            prob += x[i][j] <= v[i]
            prob += x[j][i] <= v[j]
            
    #Retour du problème :
    return(prob)



def AffichageModele(Modele,name):
    Modele.writeLP(name)
    #print(Modele)

    # Résolution du problème :
    #print("Solve with CBC")
    Modele.solve(PULP_CBC_CMD())
    #print("Status :",LpStatus[Modele.status])
    
    #Affichage de la solution :
    #print("Optimal value =",value(Modele.objective))
    #print("Optimal solution :")
    AretesTraites = []
    Sommets = []
    regexp = re.compile(r"_(\d+)_(\d+)")
    regexp2 = re.compile(r"v_(\d+)")
    for v in Modele.variables():
        if(v.varValue != 0 and (v.name[0] == 'x' or v.name[0] == 'v')):
            result = regexp.search(v.name)
            result2 = regexp2.search(v.name)
            if result != None:
                i = int(result.group(1))
                j = int(result.group(2))
                if([j,i] not in AretesTraites):
                    AretesTraites.append([i,j])
            if result2 != None:
                Sommets.append(int(result2.group(1)))
            #print(v.name,"=",v.varValue)
    print("RESULTAT :",name)
    for arete in AretesTraites:
        print("On garde l'arête {",arete[0],",",arete[1],"}")
    print("L'arbre de Steiner contient les sommets : ",Sommets)
    print('Le poids de total de l\'arbre est de : ',value(Modele.objective),end="\n")
    print("------")
            
if __name__ == "__main__":
    
    #Exemple n°1:

    G1={}
    G1[1]={2:5,5:4}
    G1[2]={1:5,5:6,4:4,3:2}
    G1[3]={2:2,4:3}
    G1[4]={2:4,3:3,5:2}
    G1[5]={1:4,2:6,4:2}
    
    T_G1 = [1,3,4,5]  #Les terminaux
    
    AffichageModele(ModelePLNE_Steiner(G1,T_G1),"Steiner Exemple 1")
    
    #Exemple n°2:

    G2={}
    G2[1]={2:6,3:3,10:9}
    G2[2]={1:6,3:4,4:2,5:9}
    G2[3]={1:3,10:9,9:9,4:2,2:4}
    G2[4]={3:2,9:8,5:9,2:2}
    G2[5]={2:9,4:9,9:7,7:5,6:4}
    G2[6]={5:4,7:1,8:4}
    G2[7]={5:5,6:1,8:3,9:9}
    G2[8]={6:4,7:3,9:10,10:18}
    G2[9]={10:8,3:9,4:8,5:7,7:9,8:10}
    G2[10]={1:9,3:9,9:8,8:18}

    T_G2 = [1,5,7,10] #Les terminaux
    
    AffichageModele(ModelePLNE_Steiner(G2,T_G2),"Steiner Exemple 2")
    
    #Exemple 3

    G3 = {}
    G3[1] = {2:10,5:10}
    G3[2] = {1:10,3:10}
    G3[3] = {2:10,4:1,9:10}
    G3[4] = {5:1,3:1,8:1}
    G3[5] = {1:10,4:1,6:1}
    G3[6] = {5:1,7:10}
    G3[7] = {6:10,8:10,12:10}
    G3[8] = {4:1,7:10,10:1}
    G3[9] = {3:10,10:10}
    G3[10] = {9:10,8:1,11:10}
    G3[11] = {10:10,12:10}
    G3[12] = {7:10,11:10}

    T_G3 = [3,4,6,10]
    
    AffichageModele(ModelePLNE_Steiner(G3,T_G3),"Steiner Exemple 3")
    
    #Exemple 4

    G4 = {}
    G4[1] = {2:10,3:1,6:1}
    G4[2] = {1:10,3:1,5:1}
    G4[3] = {1:1,2:1,4:1,10:1}
    G4[4] = {3:1,5:1,6:1,7:1}
    G4[5] = {2:1,4:1,6:1,8:1,9:1}
    G4[6] = {1:1,4:1,5:1,8:1,9:1}
    G4[7] = {4:1,8:1}
    G4[8] = {5:1,6:1,7:1,10:1}
    G4[9] = {5:1,6:1,10:1}
    G4[10] = {3:1,8:1,9:1}

    T_G4 = [1,2,4,7,10]
    
    AffichageModele(ModelePLNE_Steiner(G4,T_G4),"Steiner Exemple 4")
    
    #Exemple 5

    G5 = {}
    G5[1] = {2:1,3:10,6:10}
    G5[2] = {1:1,5:1,3:1}
    G5[3] = {2:1,1:10,4:10,7:1}
    G5[4] = {7:10,3:10,6:10,5:10}
    G5[5] = {2:1,6:10,4:10}
    G5[6] = {1:10,4:10,5:10}
    G5[7] = {3:1,4:10}

    T_G5 = [1,5,7]
    
    AffichageModele(ModelePLNE_Steiner(G5,T_G5),"Steiner Exemple 5")


