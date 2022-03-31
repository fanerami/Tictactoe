from tkinter import messagebox
import lib.fenetre as F
import lib.fonctions as fb
import lib.config as cf

def afficher_victoire(fen, message):
    """
    Fonction pour afficher le vainqeur
    """
    
    messagebox.showinfo("Fini", message+" a gagné!!!")
    F.fenetre_principale(fen,fb.initialiser_grille(cf.SIZE))
    
    
def affiche_fin(fen):
    """
    Fonction pour afficher un message s'il n'y a auccin vainqueur
    """
    messagebox.showinfo("Fini", "Dommage, le jeu est fini\n Personne n'a gagné!!!")
    F.fenetre_principale(fen,fb.initialiser_grille(cf.SIZE))
