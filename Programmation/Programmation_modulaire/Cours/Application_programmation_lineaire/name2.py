# Pour tout script python, nommer 'NomFichier', il existe une variable __name__ qui vaut le '__NomFichier__'  
# lorsque le programme est importé.
import name
#print("affichage du nom du module apres import")
print("Le nom du module est : " + name.__name__)
