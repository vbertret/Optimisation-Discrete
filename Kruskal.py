# -*- coding: utf-8 -*-
from Graphe import *


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
    



if __name__ == "__main__":
    G1=Graphe()
    G1.ajouterSommet("A")
    G1.ajouterSommet("B")
    G1.ajouterArrete("A","B",2)
    G1.ajouterArrete("A","C",3)
    G1.ajouterArrete("A","B",10)
    G1.ajouterArrete("B","A",2)
    liste=minArrete(G1)
    print(liste)