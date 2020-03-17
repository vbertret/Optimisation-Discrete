# -*- coding: utf-8 -*-
from Graphe import *
import random


def minArrete(G):
    listetrie=[]
    Gcopie=G.copie()
    dictArrete=Gcopie.ar
    while(len(listetrie)<G.nbA):
        mini=10^100
        for i in dictArrete.keys():
            for j in dictArrete[i].keys():
                if(min(dictArrete[i][j])<mini):
                    mini=min(dictArrete[i][j])
                    index=[i,j]
        listetrie.append([index[0],index[1],mini])
        dictArrete[index[0]][index[1]].remove(mini)
        if(len(dictArrete[index[0]][index[1]])==0):
            del(dictArrete[index[0]][index[1]])
    return(listetrie)
    
def detectionCycle(G):
    color={s : "w" for s in G.so}
    while(any([c=="w" for c in color.values()])):
        rand=random.choice([sommet for sommet in G.so if color[sommet]=="w"])
        pile=[rand]
        while(len(pile)>=1):
            s=pile.pop()
            color[s]="g"
            cpt=0
            if(s in G.ar.keys()):
                for j in G.ar[s].keys():
                    if(color[j]=="g"):
                        return(True)
                    if(color[j]=="w"):
                        pile.append(j)
                        cpt+=1
            if(cpt==0):
                colorier_noir(G,s,color)
    return(False)
    
def colorier_noir(G,sommet,color):
    color[sommet]="b"
    for i in G.ar.keys():
        if sommet in G.ar[i].keys():
            if(all([color[j]=="b" for j in G.ar[i].keys()])):
                colorier_noir(G,i,color)
                
def Kruskal(G):
    arretetrie=minArrete(G)
    Garbre=Graphe()
    for sommet in G.so:
        Garbre.ajouterSommet(sommet)
    while(Garbre.nbA<Garbre.nbS-1):
        arc=arretetrie[0]
        Garbre.ajouterArrete(arc[0],arc[1],arc[2])
        if(detectionCycle(Garbre)):
            print("test")
            Garbre.enleverArrete(arc[0],arc[1],arc[2])
        del(arretetrie[0])
    return(Garbre)
            
    
    

if __name__ == "__main__":
    G1=Graphe()
    G1.ajouterSommet("A")
    G1.ajouterSommet("B")
    G1.ajouterArrete("A","B",2)
    G1.ajouterArrete("B","C",2)
    G1.ajouterArrete("A","C",3)
    G1.ajouterArrete("A","B",10)
    print(detectionCycle(G1))
    Garbre=Kruskal(G1)
    print(Garbre.ar)
    
    