import numpy as np 
from vpython import *
import latexify

@latexify.function
def f(x):
    return np.sqrt(1-x**2)



def Integration_MC(a:float, b:float, N: int, f: callable, g1, gd1, gd2, fonction:str)-> float:
    """Estimer la valeur d'une integrale en dimension 1
    
    Args
    ----
    a: float    borne inferieur de l'integrale
    b: float    borne superieur de l'integrale
    N: int      Nombre total de valeur à tirer au hasard suivant la loi uniforme
    f: callable  fonctions à integrer 

    Renvoie
    --------
    float:  l'approche de l'integrale de f(x) sur [a,b] par la méthode de Monte Carlo
    l'affichage de l'animation du tirage des points dans le calcul de l'integrale de f(x) sur [a,b] 
    calcul aussi l'erreur sur le calcul de l'integrale

    """


    # Initialisation des variables et des graphes pour l'animation

    i = 0
    somme_fx_i = 0
    somme_fx_i2 = 0
    A = b-a

    while i < N:
        rate(100)
        # Choix d'un point aleatoire dans l'intervalle [a,b]
        x_i = np.random.random()
        f_xi = f(x_i)
        somme_fx_i +=  f_xi                      # sommation des f(x_i)
        somme_fx_i2 +=  f_xi*f_xi                # sommation des f(x_i)**2

        # Partie graphique de l'animation
        y_i = np.random.random()
        if y_i <f_xi:

            gd1.plot(x_i,y_i)                  # Affichage du point interieur
        else:
            gd2.plot(x_i,y_i)                    # Affichage du point exterieur
    
    
        i += 1

    # estimation de l'integrale et de l'erreur sur le calcul de l'integrale
    somme_fx_i /= float(N)                                       # <f(x)> 
    somme_fx_i2 /= float(N)                                      #<f(x)**2>
    integrale = np.round(A*somme_fx_i, 4)                       # calcul de l'aire sous la courbe de f(x) sur [a,b]                             
    var_fx_i = somme_fx_i2 - somme_fx_i**2                       #  variance = <f(x)**2> - <f(x)>**2
    Integration_MC.erreur = np.round(np.sqrt(var_fx_i/float(N)), 4)

    gd1.label = f"l'aire sous la courbe de {fonction}:"
    gd2.label = f" {integrale} +/- {Integration_MC.erreur}"
    return integrale


if __name__ == "__main__" :
   N = 1000
   g1 = graph(title = f"Estimation de Pi pour N = {N}"  , xtitle='x', ytitle='y')
   gd1 = gdots(graph = g1, color = color.red)
   gd2 = gdots(graph = g1, color = color.blue)
   fonction = str(f)
   print( f" Pour N = {N}\n Pi = {4*Integration_MC(0,1,N, f, g1, gd1, gd2, fonction)} +/- {Integration_MC.erreur}")