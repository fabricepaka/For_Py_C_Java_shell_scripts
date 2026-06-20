# Objectif: 
#        Estimer la valeur de pi en utilisant la méthode de Monte Carlo.
#
# Date                                   Programmeur             Version      
# ====                                   =============         ============
# 2026-06-19                              Fabrice PAKA            Premiere

# Importation des bibliothèques nécessaires
import random
import numpy as np 


n_cercle = 0
n_carre = 0
i=0
while i<=10000000:
    # choix aleatoire des coordonées x et y entre 0 et 1
    x = random.random()
    y = random.random()

    # Calcul de la longueur entre le centre O(0;0) et le point de coordonnée (x, y)
    r = np.sqrt(x**2 +y**2)
    
    if r<1:
        n_cercle +=1
    n_carre +=1
    i += 1
p = n_cercle/n_carre

pi = 4*p

print(f"pi = {pi}")

    