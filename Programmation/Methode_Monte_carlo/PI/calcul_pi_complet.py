#================================================================================================================#
# Objectif:                                                                                                      #
#        Estimer la valeur de pi en utilisant la méthode de Monte Carlo.                                         #
#                                                                                                                #  
#    Date                                   Programmeur             Version                                      # 
#    -----                                  -----------             --------                                     # 
#    2026-06-20                             Fabrice PAKA            Premiere                                     #
#                                                                                                                #
#    Paramètres                                                                                                  # 
#    ----------                                                                                                  #
#    N: Nombre total de valeurs aleatoires choisi                                                                #
#    x; y: coordonnées x et y  d'un point choisi aleatoirement                                                   #
#                                                                                                                # 
#    Retour                                                                                                      #
#    -------                                                                                                     #
#    Pi: valeur approchée de Pi                                                                                  #
#    Animation de l'echantillonnage (le tirage des points dans le calcul de l'aire du quart de disque )          #
#================================================================================================================#



# Importation des bibliothèques nécessaires
import numpy as np
from vpython import *

#definition des graphes pour l'animation
g1 = graph(title="Représentation graphique de l'ensemble des points", xtitle='x', ytitle='y')
gd1 = gdots(graph = g1, color = color.red)
gd2 = gdots(graph = g1, color = color.blue)


N_interieur = 0
N_total  = 100000             # Nombre total de points a choisir aleatoirement
i = 0
while i < N_total:
    rate (5)
    x = np.random.random()
    y = np.random.random()

    if np.sqrt(x**2 +y**2) < 1:
        # comptage du nombre de poins interieur
        N_interieur += 1

        # Affichage du point interieur
        gd1.plot(x,y) 

    else:
        # Affichage du point exterieur
        gd2.plot(x,y)
    i+=1

Aire_quart_cercle = N_interieur/N_total
pi = 4*Aire_quart_cercle

# Affichage de la superficie, de l'estimation de Pi et de l'erreur sur son calcul
print(f"Aire du  quart = {Aire_quart_cercle}")
print(f"Estimation de Pi est donc = {pi}")
print(f"Erreur d'estimation = {np.abs(np.pi -pi)}" )