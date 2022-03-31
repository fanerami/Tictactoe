import random
import lib.fonctions as fb
import lib.config as cf
import copy
from math import inf as infinity

def mouv_possible(grille):
    """
    Fonction qui liste tous mouvements encore possible à faire,
    c'est à dire les cases vides
    :param grille: la matrice de la grille
    :return: les coordonées des cases vides
    """
    res = []
    for i in range(cf.SIZE):
        for j in range(cf.SIZE):
            if grille[i][j] == 0:
                res.append((i,j))
    return res

def bot_t_facile(grille):
    """
    Fonction pour générer les coordonnées de la case où le bot va mettre son pion.
    Niveau du bot très facile parcequ'il choisit au hasard
    :param grille: la matrice de la grille
    :return: coordonnées où le bot va mettre son pion
    """
    indice = random.choice(mouv_possible(grille))
    
    return indice
    
    
def bot_facile(grille):
    """
    Fonction pour générer les coordonnées de la case où le bot va mettre son pion.
    Niveau du bot facile parcequ'il choisi d'abord, parmi les coordonnées possibles,
    le coordonnées qui gagnent. S'il n'y en a pas, il chosit au hasard
    :param grille: la matrice de la grille
    :return: coordonnées où le bot va mettre son pion
    """
    candidats = mouv_possible(grille)
    
    trouve_vainqueur = False
    i = 0
    indice = None
    while i < len(candidats) and not trouve_vainqueur:
        indice = candidats[i]
        
        #on place la valeur au coordonnées 
        grille[indice[0]][indice[1]] = cf.COMP
                
        ## si le coup entraîne la victoire du robot, on arrête la boucle
        if fb.check_vainqueur(grille,cf.COMP):
            trouve_vainqueur = True
        
        #on reviens vers la grille d'avant modification ci-dessus
        grille[indice[0]][indice[1]] = 0
        
        
        i+=1
    
    # si non un choix random
    return indice if trouve_vainqueur else random.choice(candidats)
    
    
def bot_moyen(grille):
    """
    Fonction pour générer les coordonnées de la case où le bot va mettre son pion.
    Niveau du bot moyen parcequ'il choisi d'abord, parmi les coordonnées possibles,
    le coordonnées qui gagnent. S'il n'y en a pas, il choisit le coordonnées qui bloque
    l'autre joueur de gagner. Si non il chosit au hasard
    :param grille: la matrice de la grille
    :return: coordonnées où le bot va mettre son pion
    """
    
    mouv = None
    premier_candidats = mouv_possible(grille)
    i = 0
    trouve_coord = False
    
    while i < len(premier_candidats) and not trouve_coord:
        indice = premier_candidats[i]
        
        #on place la valeur au coordonnées 
        grille[indice[0]][indice[1]] = cf.COMP
        
            
        ## si le coup entraîne la victoire du robot, on arrête la boucle
        if fb.check_vainqueur(grille,cf.COMP):
            trouve_coord = True
            mouv = indice
            
        second_candidats = mouv_possible(grille)
        
        if len(second_candidats) > 0:
            j = 0
            while j < len(second_candidats) and not trouve_coord:
                indice_2 = second_candidats[j]
        
                #on place la valeur de l'autre joueur au coordonnées 
                grille[indice_2[0]][indice_2[1]] = -cf.COMP
                
                #Si le coup bloque la victoire de l'autre joueur, on arrête la boucle
                if fb.check_vainqueur(grille, -cf.COMP):
                    trouve_coord = True
                    mouv = indice_2
                
                #on reviens vers la grille d'avant modification ci-dessus
                grille[indice_2[0]][indice_2[1]] = 0
                
                j+=1
                
        
        #on reviens vers la grille d'avant modification ci-dessus
        grille[indice[0]][indice[1]] = 0
        
        i+=1
            
        
    return mouv if trouve_coord else random.choice(premier_candidats)

#Allez chercher sur internet pour en savoir plus sur l'algo minimax ou MinMax
# https://fr.wikipedia.org/wiki/Algorithme_minimax
def minimax(grille, profondeur, joueur):
    """
    Fonction AI qui choisit le meilleur coup
    :param grille: la matrice de la grille
    :param profondeur: index de nœud dans l'arborescence (0 <= profondeur <= 9)
    :param joueur: valeur du bot ou joueur à mettre dans la matrice
    :return: coordonnées où le bot va mettre son pion
    """
    
    #initialisation du meilleur emplacement où place le pion
    if joueur == cf.COMP:
        meilleur = [-1, -1, -infinity]
    else:
        meilleur = [-1, -1, +infinity]
    
       
    
    if fb.check_vainqueur(grille,cf.COMP):
        return [-1, -1, +1]
    elif fb.check_vainqueur(grille,cf.HUMAN):
        return [-1, -1, -1]
    elif profondeur == 0:
        return [-1, -1, 0]


    for indice in mouv_possible(grille):
        
        #on place la valeur au coordonnées 
        grille[indice[0]][indice[1]] = joueur
        
        
        # On appelle à nouveau la fonction minimax (récursivité)
        score = minimax(grille, profondeur - 1, -joueur)
        
        #on reviens vers la grille d'avant modification ci-dessus
        grille[indice[0]][indice[1]] = 0
     
        #mettre à jour les coordonnées dans score
        score[0], score[1] = indice[0], indice[1]
        
        #mettre à jour la valeur à l'indice 2 dans score.
        if joueur == cf.COMP:
            if score[2] > meilleur[2]:
                meilleur = score  # max value
        else:
            if score[2] < meilleur[2]:
                meilleur = score  # min value
                 
    return meilleur
    
    
    
def bot_difficile(grille):
    """
    Fonction pour générer les coordonnées de la case où le bot va mettre son pion.
    Niveau du bot difficile parcequ'il utilise la méthode minimax pour chosir les coordonnées
    :param grille: la matrice de la grille
    :return: coordonnées où le bot va mettre son pion
    """
    profondeur = len(mouv_possible(grille))
    if profondeur == 0 or fb.check_vainqueur(grille,cf.HUMAN) or fb.check_vainqueur(grille,cf.COMP):
        return None
    mouv = minimax(grille, profondeur, cf.COMP)
    
    return mouv[0], mouv[1]
    
    
    
def bot_joue(grille, niveau="facile"):
    """
    Cette fonction appelée différentes fonctions du bot
    en fonction de la difficulté choisit par l'utilisateur
    :param grille: la matrice de la grille
    :param niveau: niveau de difficulté de jouer contre un bot
    """
    if niveau == "t_facile":
        return bot_t_facile(grille)
    elif niveau == "facile":
        return bot_facile(grille)
    elif niveau == "moyen":
        return bot_moyen(grille)
    else:
        return bot_difficile(grille)


