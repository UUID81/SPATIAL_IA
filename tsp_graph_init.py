import numpy as np
import pandas as pd
import tkinter as tk
import time
import random

NB_LIEUX = 5
LARGEUR = 800
HAUTEUR = 600

random.seed(1)
np.random.seed(1)


class Lieu :
    @classmethod
    def init_lieu (cls, x, y) :
        return np.array([x,y])
    @classmethod
    def calc_dist(cls,lieu1,lieu2) :
        dist =np.sqrt(np.sum((lieu1-lieu2)**2))
        return dist.round(1)

class Graph :
    @classmethod
    def creation_points(cls):
        cls.liste_lieux ={}
        for i in range(NB_LIEUX):
            cls.x=np.random.randint(10,LARGEUR-10)
            cls.y=np.random.randint(10,HAUTEUR-10)
            cls.liste_lieux[i]=Lieu.init_lieu(cls.x,cls.y)
        return cls.liste_lieux

    @classmethod
    def calcul_matrice_cout_od(cls) :
        cls.matrix=np.zeros([NB_LIEUX,NB_LIEUX])
        for i in range(len(cls.matrix)):
            for j in range(len(cls.matrix[i])):
                if cls.matrix[i,j]==0:
                    cls.matrix[i,j]=Lieu.calc_dist(cls.fichier[i],cls.fichier[j])
                    cls.matrix[j,i]=Lieu.calc_dist(cls.fichier[i],cls.fichier[j])
        cls.matrice_od=cls.matrix
        return cls.matrice_od
    
    @classmethod
    def knn(cls, point) : 
        v = cls.matrice_od[point]
        cls.voisin = [i for i in v if i != 0]
        cls.voisin = cls.voisin.index(min(cls.voisin))
        return cls.voisin

    @classmethod
    def charger(cls,fichier) : 
        cls.fichier = pd.read_csv(fichier)
        cls.fichier=np.array(cls.fichier)
        return cls.fichier
    
    @classmethod
    def sauvegarder(cls) : 
        cls.matrice=pd.DataFrame(cls.matrice_od)
        cls.matrice.to_csv('Graphe_voisin',index=False)
        print('Ok')

print(Graph.charger('graph_5.csv'))
f=Graph.calcul_matrice_cout_od()
print('##################')
print(f)
print("Le plus proche voisin :",Graph.knn(1))
