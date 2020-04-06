# -*- coding: utf-8 -*-
from Graphe import *
import random

    #Algo de detection de cycle p14
def detectionCycle(G):
    color={s : "w" for s in G.so}  #Couleur des sommets(w : pas visite, g : visite, n visite avec que des successeurs noirs)
    while(any([c=="w" for c in color.values()])):
        rand=random.choice([sommet for sommet in G.so if color[sommet]=="w"]) #On choisit un sommet aléatoire non traité
        pile=[rand] #on le rajoute dans la pile
        prec="" #on garde en mémoire le sommet precédent 
        while(len(pile)>=1):
            s=pile.pop()  #on traite le premier sommet de la pile
            color[s]="g"
            cpt=0 #compteur qui permet de déterminer les sommets qui n'ont pas de succeseurs(0 : pas de succeseur , >=1 plusieurs succeseurs)
            if(s in G.ar.keys()):
                for j in G.ar[s].keys():
                    if(color[j]=="g" and not (j==prec)):   #si on rencontre un sommet gris qui n'est pas le sommet précédent , alors il y a un cycle
                        return(True)
                    if(color[j]=="w"):  #si le sommet n a pas encore été visite on l'ajoute à la pile
                        pile.append(j)
                        cpt+=1
            prec=s
            if(cpt==0):
                colorier_noir(G,s,color)  #si le sommet n'a plus de succeseur ...
    return(False)
    
    #Fonction auxilaire de la fonction detection de cycle
def colorier_noir(G,sommet,color):
    color[sommet]="b"  #on colorie en noir, le sommet qui n'a pas de succeseur
    for i in G.ar.keys():
        if(color[i] != "b"):
            if sommet in G.ar[i].keys():
                if(all([color[j]=="b" for j in G.ar[i].keys() if not (i  in G.ar[j].keys()) ])):
                    colorier_noir(G,i,color) # si tous ces successeurs sont noirs, alors on le colorie en noir
                
def Kruskal(G):
    arretetrie=G.minArrete()
    Garbre=Graphe(False)
    for sommet in G.so:
        Garbre.ajouterSommet(sommet)
    while(Garbre.nbA<Garbre.nbS-1):
        arc=arretetrie[0]
        Garbre.ajouterArrete(arc[0],arc[1],arc[2])
        if(detectionCycle(Garbre)):
            Garbre.enleverArrete(arc[0],arc[1],arc[2])
        del(arretetrie[0])
        if not G.oriente:
            del(arretetrie[arretetrie.index([arc[1],arc[0],arc[2]])])
    return(Garbre)
            
    
    

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
    
    
    print(detectionCycle(G1))
    Garbre=Kruskal(G1)
    Garbre.afficherGraphe()
    print(Garbre.ar)

    
    