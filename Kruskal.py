# -*- coding: utf-8 -*-
from Graphe import *


def minArrete(G):
    listetrie=[]
    dictArrete=G.ar
    while(len(listetrie)<G.nbA):
        mini=100000000
        for i in dictArrete.keys():
            for j in dictArrete[i].keys():
                if(min(dictArrete[i][j])<mini):
                    mini=min(dictArrete[i][j])
                    index=(i,j)
        listetrie.append({ i : { j : mini }})
        del(dictArrete[i][j])
    return(listetrie)


if __name__ == "__main__":
    G1=Graphe()
    G1.ajouterSommet("A")
    G1.ajouterSommet("B")
    G1.ajouterArrete("A","B",2)
    G1.ajouterArrete("A","C",3)
    G1.ajouterArrete("A","B",10)
    G1.ajouterArrete("B","A",2)
    ls=minArrete(G1)
    print(ls)