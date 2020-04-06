# -*- coding: utf-8 -*-
import turtle

class Graphe():
    
    def __init__(self,oriente=True):
        self.nbS = 0 #nombre de Sommet du Graphe
        self.nbA = 0 #nombre d'Arretes du Graphe
        self.so= [] #liste des différents sommets
        self.ar= {} #dictionnaire contenant les arretes
        self.oriente=oriente #defintion du type de graphe
  
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
         #on ajoute les sommets du depart et de l'arrivée si il n'existent pas
        self.ajouterSommet(depart,0)  
        self.ajouterSommet(arrivee,0)
        #if(depart not in self.ar.keys()):
         #   self.ar[depart]={}
        #if(self.oriente==False and arrivee not in self.ar.keys()):
         #   self.ar[arrivee]={}
        #Si l'arrivée n'est pas deja un sucesseur, on vient la rajouter dans le dictionnaire.
        if(arrivee not in self.ar[depart].keys()): 
            self.ar[depart][arrivee]=[]
        if(self.oriente ==False and depart not in self.ar[arrivee].keys()):
            self.ar[arrivee][depart]=[]
        #On rajoute l'arc et on augmente le nombre d'arc de 1
        self.ar[depart][arrivee].append(val)
        self.nbA+=1
        if(self.oriente==False):
            self.ar[arrivee][depart].append(val)
    
    #Creation de la liste des arrêtes trié par ordre croissant    
    def minArrete(self):
        minimum=[]
        for key1 in self.ar.keys():
            for key2 in self.ar[key1].keys():
                for val in self.ar[key1][key2]:
                    minimum.append([key1,key2,val])
        minimum = sorted(minimum, key= lambda x : x[2])
        return(minimum)
        
     
    #Supression d'une arrête
    def enleverArrete(self,depart,arrivee,val):
        if(not(depart in self.ar.keys() and arrivee in self.ar[depart].keys() and val in self.ar[depart][arrivee])):
            print("Cette arrête n'existe pas !")
            return(False)
        self.ar[depart][arrivee].remove(val)
        self.nbA-=1
        if(len(self.ar[depart][arrivee])==0):
            del(self.ar[depart][arrivee])
        #if(len(self.ar[depart])==0):
        #    del(self.ar[depart])
        if(not self.oriente):
            self.ar[arrivee][depart].remove(val)
            if(len(self.ar[arrivee][depart])==0):
                del(self.ar[arrivee][depart])
         #   if(len(self.ar[arrivee])==0):
         #       del(self.ar[arrivee])
        return(True)
        
    def afficherGraphe(self):
        wn = turtle.Screen()
        wn.bgcolor("light green")
        wn.title("Turtle")
        skk = turtle.Turtle()
        skk.up()
        x=-300
        y=200
        location={}
        for i in range(self.nbS):
            skk.goto(x,y)
            skk.down()
            skk.write(self.so[i])
            location[self.so[i]]=[x,y]
            skk.up()
            x+=299
            if(x>300):
                x=-300
                y-=200
        skk.color("red")
        for key1 in self.ar.keys():
            for key2 in self.ar[key1].keys():
                pos1=location[key1]
                skk.goto(pos1[0],pos1[1])
                skk.down()
                pos2=location[key2]
                skk.goto(pos2[0],pos2[1])
                skk.up()
                pos3=[(pos1[0]+pos2[0])/2,(pos1[1]+pos2[1])/2+15]
                skk.goto(pos3[0],pos3[1])
                skk.write(self.ar[key1][key2][0])
        turtle.hideturtle()
        turtle.done()
        turtle.reset()
            
        

        
if __name__ == "__main__":
    G1=Graphe(True)
    G1.ajouterSommet("A")
    G1.ajouterSommet("B")
    
    G1.ajouterArrete("A","B",5)
   
    G1.ajouterArrete("A","E",4)
   
    G1.ajouterArrete("E","B",6)
   
    G1.ajouterArrete("E","D",2)
    
    G1.ajouterArrete("B","D",4)

    G1.ajouterArrete("B","C",2)
    
    G1.ajouterArrete("D","C",3)
    G1.afficherGraphe()
    
        