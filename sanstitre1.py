# -*- coding: utf-8 -*-
#%%
class Graphe():
    
    def __init__(self):
        self.nbS = 0 #nombre de Sommet du Graphe
        self.nbA = 0 #nombre d'Arretes du Graphe
        self.so= [] #liste des différents sommets
        self.ar= {} #dictionnaire contenant les arretes
  
    #Methode pour rajouter un sommet au graphe      
    def ajouterSommet(self,nom,impress=1):
        if(nom not in self.so):   #On teste si le nom du sommet n'existe pas deja
            self.nbS=self.nbS+1;
            self.so.append(nom)
            self.ar[nom]={}
        else:
            if(impress==1):
                print("Warning : Il existe deja un sommet avec ce nom !")
    
    #Methode pour rajouter une arrête au graphe
    def ajouterArrete(self,depart,arrivee,val):
         #on ajoute les 2 sommets si il n'existent pas
        self.ajouterSommet(depart,0)  
        self.ajouterSommet(arrivee,0)
        #si il n'y a pas d'arc reliant deja les 2 sommets,
        # on vient initialiser une liste qui va contenir la valeur des arcs
        if(arrivee not in self.ar[depart].keys()): 
            self.ar[depart][arrivee]=[]
        if(depart not in self.ar[arrivee].keys()):
            self.ar[arrivee][depart]=[]
        #On rajoute l'arc et on augmente le nombre d'arc de 1
        self.ar[depart][arrivee].append(val)
        self.ar[arrivee][depart].append(val)
        self.nbA+=1

    #Creation de la liste des arrêtes trié par ordre croissant    
    def minArrete(self):
        minimum=[]
        #Remplissage de la liste avec toutes les arrêtes
        for key1 in self.ar.keys():
            for key2 in self.ar[key1].keys():
                for val in self.ar[key1][key2]:
                    minimum.append([key1,key2,val])
        #On trie la liste par ordre croissant avec la valeur de l'arc
        minimum = sorted(minimum, key= lambda x : x[2])
        return(minimum)
        
    #Supression d'une arrête
    def enleverArrete(self,depart,arrivee,val):
        #Test pour savoir si l'arc existe
        if(not(depart in self.ar.keys() and arrivee in self.ar[depart].keys() and val in self.ar[depart][arrivee])):
            print("Cette arrête n'existe pas !")
            return(False)
        #On retire l'arc
        self.ar[depart][arrivee].remove(val)
        self.ar[arrivee][depart].remove(val)
        self.nbA-=1
        #Si il n'y a plus d'arc entre ces 2 sommets, on vient supprimer la liste
        if(len(self.ar[depart][arrivee])==0):
            del(self.ar[depart][arrivee]) 
        if(len(self.ar[arrivee][depart])==0):
            del(self.ar[arrivee][depart])
        return(True)

#%%
import random
#%%

def genGraphe(nbSom=6,nbAr=10,minVal=0,maxVal=8):
    graphe=Graphe()
    for k in range(nbSom) :
        graphe.ajouterSommet(str(k))
    
    for i in range(1,nbSom+1):
        for j in range(i+1,nbSom+1):
            graphe.ajouterArrete(str(i),str(j),random.randint(minVal,maxVal))
    
    return(graphe)

#%%
A=genGraphe2()

#%%
B=genGraphe2(20,40,1,4)






















