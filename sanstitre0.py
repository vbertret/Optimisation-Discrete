# -*- coding: utf-8 -*-

liste=dict()
liste[1]={ 2 : 2, 3 : 7}
liste[2]={ 1 : 3, 3 : 7}
print(liste)
for x in liste.keys():
    print(x , ": ", list(liste[x].keys()))

min=10000
index=0
for i in liste.keys():
    for j in liste[i].keys():
        if(liste[i][j]<min):
            min=liste[i][j]
            index=(i,j)

#%%
liste1=[[i for i in liste[j].values()] for j in liste.keys()]









