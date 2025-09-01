#!/usr/bin/python3
import sys  # Import du module sys pour accéder aux arguments passés au script depuis la ligne de commande

def factorial(n):
    """
    Fonction récursive pour calculer la factorielle d'un entier n.
    
    Args:
        n (int): L'entier dont on veut calculer la factorielle. Doit être >= 0.
        
    Returns:
        int: La factorielle de n (n!).
    """
    if n == 0:
        # La factorielle de 0 est définie comme 1
        return 1
    else:
        # Appel récursif : n! = n * (n-1)!
        return n * factorial(n-1)

# Récupération du premier argument de la ligne de commande
# sys.argv[0] est le nom du script, sys.argv[1] est le premier argument utilisateur
f = factorial(int(sys.argv[1]))

# Affichage du résultat
print(f)
