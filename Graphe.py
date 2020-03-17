# -*- coding: utf-8 -*-

class Graphe():
    
    def __init__(self):
        self.nbS = 0 #nombre de Sommet du Graphe
        self.nbA = 0 #nombre d'Arretes du Graphe
        self.so= [] #liste des différents sommets
        self.ar= {} #dictionnaire contenant les arretes
  
    #Methode pour rajoiuter un sommet au graphe      
    def ajouterSommet(self,nom,impress=1):
        if(nom not in self.so):
            self.nbS=self.nbS+1;
            self.so.append(nom)
        else:
            if(impress==1):
                print("Warning : Il existe deja un sommet avec ce nom !")
    
    #Methode pour rajouter une arrête au graphe
    def ajouterArrete(self,depart,arrivee,val):
        self.ajouterSommet(depart,0)
        self.ajouterSommet(arrivee,0)
        if(depart not in self.ar.keys()):
            self.ar[depart]={}
        if(arrivee not in self.ar[depart].keys()):
            self.ar[depart][arrivee]=[]
        self.ar[depart][arrivee].append(val)
        self.nbA+=1
      
    #Creation d'une copie d'un graphe avec une adresse mémoire différente   
    def copie(self):
        Gcopie=Graphe()
        for sommet in self.so:
            Gcopie.ajouterSommet(sommet)
        for i in self.ar.keys():
            Gcopie.ar[i]={}
            for j in self.ar[i].keys():
                Gcopie.ar[i][j]=list(self.ar[i][j])
                Gcopie.nbA+=len(self.ar[i][j])
        return(Gcopie)
     
    #Supression d'une arrête
    def enleverArrete(self,depart,arrivee,val):
        if(not(depart in self.ar.keys() and arrivee in self.ar[depart].keys() and val in self.ar[depart][arrivee])):
            print("Cette arrête n'existe pas !")
            return(False)
        self.ar[depart][arrivee].remove(val)
        self.nbA-=1
        if(len(self.ar[depart][arrivee])==0):
            del(self.ar[depart][arrivee])
        if(len(self.ar[depart])==0):
            del(self.ar[depart])
        return(True)
        

        
if __name__ == "__main__":
    G1=Graphe()
    G1.ajouterSommet("A")
    G1.ajouterSommet("B")
    G1.ajouterArrete("A","B",2)
    G1.ajouterArrete("A","C",3)
    G1.ajouterArrete("A","B",10)
    G1.ajouterArrete("B","A",2)
    G1.enleverArrete("B","A",2)
    
        