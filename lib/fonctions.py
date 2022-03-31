import lib.config as cf
import lib.dessin_board as db
import lib.message as ms
import lib.bot as bt


def initialiser_grille(taille):
    """
    Fonction pour initialiser la matrice de la grille
    :param taille: taille de la grille
    :return: la matrice de la grille
    """
    grille = []
    
    for i in range(taille):
        grille.append([0]*taille)
            
    return grille  
      
      
def check_vainqueur(grille, joueur=-1):
    """
    Fonction pour test si un joueur (ou bot) a gagné. Possibilités:
    * Trois ligne      [X X X] or [O O O]
    * Trois colobbe    [X X X] or [O O O]
    * Deux diagonals   [X X X] or [O O O]
    :param grille: la matrice de la grille
    :param joueur: un humain ou le bot
    :return: Vraie si un joeuur gagne
    
    À modifier si SIZE > 3
    """
    
    etat_victoire = [
        [grille[0][0], grille[0][1], grille[0][2]],
        [grille[1][0], grille[1][1], grille[1][2]],
        [grille[2][0], grille[2][1], grille[2][2]],
        [grille[0][0], grille[1][0], grille[2][0]],
        [grille[0][1], grille[1][1], grille[2][1]],
        [grille[0][2], grille[1][2], grille[2][2]],
        [grille[0][0], grille[1][1], grille[2][2]],
        [grille[2][0], grille[1][1], grille[0][2]],
    ]
    
    return [joueur,joueur,joueur] in etat_victoire
    
def est_grille_complet(grille):
    """
    Fonction pour tester si la grille est pleine,
    c'est à dire que les joueurs ne peuvent plus placer des pions
    :param grille: matrice de la grille
    :return: Vraie si la grille est pleine
    """
    i,j=0,0
    plein = True    
    while i< cf.SIZE and plein:
        if grille[i][j] == 0: # dès qu'on trouve un zéro, la grille n'est plus pleine
            plein = False
        
        j+=1
        
        if j ==3:
            i+=1
            j=0
            
    return plein 
          
def mouvement_valide(grille,x, y):
    """
    Un mouvement est valide si la cellule choisie est vide
    :param grille: la matrice de la grille
    :param x: ligne X
    :param y: colonne Y
    :return: Vraie si grille[x][y] est vide (=0)
    """
    if grille[x][y]==0:
        return True
    else:
        return False  
          
def jouer(fen, j1, j2, grille, event, niveau=None):
    """
    Fonction pour joueur. Cette fonction est appelé quand un joueur clique sur la grille
    :param fen: fen où mettre les éléments
    :param j1: objet label du joueur 1
    :param j2: objet label du joueur 2
    :param event: paramètre permettant de récupérer des infos sur clic de la grille
    :param niveau: niveau de difficulté de jouer contre un bot
    """
    
    #recupérer l'objet canevas
    can = fen.winfo_children()[0].winfo_children()[-1]
    
    victoire = False
    
    x, y = event.x, event.y # récupère les coordonnées du clique sur la grille (canevasà
    
    #Tester si le clique est dans la grille
    if cf.MARGIN < x < (cf.WIDTH-cf.MARGIN) and cf.MARGIN < y < (cf.HEIGHT-cf.MARGIN):
        i,j = (y-cf.MARGIN)//cf.SIDE, (x-cf.MARGIN)//cf.SIDE # récupère le numéro de ligne et de colonne
        
        
        
        if mouvement_valide(grille,i, j):
            
            if cf.TOUR == -1:
                db.dessiner_x(can,j,i)
                gagnant = "Joueur 1"
                
                if niveau == None:
                    j2["relief"] = "raised"
                    j1["relief"] = "sunken"
                    j2["bg"] = "blue"
                    j1["bg"] = "gray"
            else:
                if j2["text"] == "Joueur 2 (0)":
                    db.dessiner_rond(can,j,i)
                    gagnant = "Joueur 2"
                    j2["relief"] = "sunken"
                    j1["relief"] = "raised"
                    j2["bg"] = "gray"
                    j1["bg"] = "red"
            
            grille[i][j] = cf.TOUR
            victoire = check_vainqueur(grille, cf.TOUR)
            
            ##########La partie BOT############
            """Cette partie s'execute quand c'est vs. Bot, juste après le joueur 1
            La seul évènement attendu est le clic du joueur 1.
            Donc après que le joueur 1 ait placé son pion, le bot place aussi le sien sans attendre
            """
            if niveau!=None and not victoire and not est_grille_complet(grille):
                cf.TOUR = -cf.TOUR #On change vers le Bot
                i,j = bt.bot_joue(grille, niveau)
                db.dessiner_rond(can,j,i)
                gagnant = "L'ordi"
                
                grille[i][j] = cf.TOUR
                victoire = check_vainqueur(grille, cf.TOUR)
            
            ###################################
            cf.TOUR = -cf.TOUR #On change de joueur
            
            if victoire:
                ms.afficher_victoire(fen, gagnant)
            else:
                if est_grille_complet(grille):
                    ms.affiche_fin(fen)
                
            
            
