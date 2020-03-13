# -*- coding: utf-8 -*-

liste=dict()
liste[1]={ 2 : 2, 3 : 7}
liste[2]={ 1 : 3, 3 : 7}
print(liste)
for x in liste.keys():
    print(x , ": ", list(liste[x].keys()))

#%%
liste1=[[i for i in liste[j].values()] for j in liste.keys()]









