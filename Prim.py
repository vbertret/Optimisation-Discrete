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
    
def Prim(G):
    Gfinal=Graphe()
    Gfinal.ajouterSommet(random.choice(G.so))
    arTrie=minArrete(G)
    for i in range(1,G.nbS):
        find=False
        j=0
        while j < len(arTrie) and find == False :
            if( not ( arTrie[j][0] in Gfinal.so) and arTrie[j][1] in Gfinal.so):
                Gfinal.ajouterArrete(arTrie[j][0],arTrie[j][1],arTrie[j][2])
                find=True
            j+=1
    return(Gfinal)
    
if __name__ == "__main__":
    G1=Graphe(False)
    G1.ajouterSommet("A")
    G1.ajouterSommet("B")
    
    G1.ajouterArrete("A","B",5)
   
    G1.ajouterArrete("A","E",4)
   
    G1.ajouterArrete("E","B",6)
   
    G1.ajouterArrete("E","D",2)
    
    G1.ajouterArrete("B","D",4)

    G1.ajouterArrete("B","C",2)
    
    G1.ajouterArrete("D","C",3)
    print(G1.ar)
    print("################ALGOO#######################")
    Garbre=Prim(G1)
    print(Garbre.ar)    