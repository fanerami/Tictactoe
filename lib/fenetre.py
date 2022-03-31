from tkinter import *
import lib.fonctions as fb
import lib.config as cf
import lib.dessin_board as db
import random


def commencer():
    '''Fonction pour démarer le jeu.'''
    
    grille = fb.initialiser_grille(cf.SIZE)
    
    ma_fenetre = Tk()
    
    ma_fenetre.geometry(str(cf.WIDTH+50)+"x"+str(cf.HEIGHT+50))

    ma_fenetre.title("Tic Tac Toe")

    ma_frame = Frame(ma_fenetre)

    fenetre_principale(ma_fenetre,grille)

    ma_fenetre.mainloop()

def fenetre_principale(fen,grille):
    """
    Fonction pour génère le contenu la première
    fenêtre quand le jeu est lancé
    :param fen: fenêtre où mettre les éléments
    :param grille: matrice de la grille
    """
    
    cf.TOUR = cf.HUMAN
    
    frame = fen.winfo_children()[0]
    effacer_contenu_frame(frame)
    
    b_simple = Button(frame, text="vs. Bot", font = 'summer', bd = 3,pady=10, command = lambda:fenetre_bot(fen,grille))
    b_double = Button(frame, text="2 joueurs", font = 'summer', bd = 3,pady=10, command = lambda:fenetre_jeu(fen,grille))
    b_quitter = Button(frame, text="Quitter", font = 'summer', bd = 3,pady=10, command=fen.destroy)

    frame.place(relwidth=0.9, relx=0.5, rely=0.5,anchor= CENTER)
    b_simple.pack(side="top",pady=5, fill=X)
    b_double.pack(side="top",pady=5, fill=X)
    b_quitter.pack(side="top",pady=5, fill=X)    
  
def fenetre_jeu(fen,grille, niveau=None, bot=False):
    '''
    Fontion pour afficher la grille du jeu dans la fenêtre
    :param fen: fenêtre où mettre les éléments
    :param grille: matrice de la grille
    :param niveau: niveau de difficulté de joueur contre un bot
    :param bot: Pour savoir qui commence en premier bot ou joueur. Par défaut False (c'est le joueur qui commence)
    '''  
    frame = fen.winfo_children()[0]

    effacer_contenu_frame(frame)
    
    joueur_1 = Label(frame,text="Joueur 1 (X)",borderwidth=3, relief="raised", padx = 5, pady=5, bg="red")#, bg="white"
    joueur_1.grid(row=0,column=0)
    
    if niveau ==  None:
        # Contre un autre joueur humain
        joueur_2 = Label(frame,text="Joueur 2 (0)",borderwidth=3, relief="sunken", padx = 5, pady=5, bg="gray")#, bg="white"
        joueur_2.grid(row=0,column=1)
        
    else:
        #Si contre bot
        joueur_2 = Label(frame,text="Ordi   (0)",borderwidth=3, relief="sunken", padx = 5, pady=5)#, bg="white"
        joueur_2.grid(row=0,column=1)
        
    b_quit = Button(frame, text="Quitter", pady=5, command=fen.destroy)
    b_quit.grid(row=0,column=2)
    
    can = Canvas(frame, bg="white", width=cf.WIDTH, height = cf.HEIGHT)
    can.grid(row=1,column=0, columnspan=3)
    
    db.dessiner_grille(can)
    
    #si vs bot et que le bot commence. Chosir au hasar l'emplacement du bot
    if bot:
        choix = [x for x in range(cf.SIZE)]
        i = random.choice(choix)
        j = random.choice(choix)
        
        grille[i][j] = cf.COMP
        db.dessiner_rond(can,j,i)

    #appel la fonction jouer quand un joueur clique sur l'évenement
    can.bind("<Button-1>", lambda event:fb.jouer(fen,joueur_1,joueur_2, grille, event,niveau))
    
    
    
   
def fenetre_bot(fen,grille):
    '''
    Fonction pour générer la fenêtre quand l'utilisateur choisi VS. Bot
    :param fen: fenêtre où mettre les éléments
    :param grille: matrice de la grille
    ''' 

    frame = fen.winfo_children()[0]
    effacer_contenu_frame(frame)
    

    b_facile = Button(frame, text="Très facile", font = 'summer', bd = 3,pady=10, command = lambda:choix_commencement(fen,grille,niveau="t_facile"))
    b_moyen = Button(frame, text="Facile", font = 'summer', bd = 3,pady=10, command = lambda:choix_commencement(fen,grille,niveau="facile"))
    b_difficile = Button(frame, text="Moyen", font = 'summer', bd = 3,pady=10, command = lambda:choix_commencement(fen,grille,niveau="moyen"))
    b_invaic = Button(frame, text="Difficile", font = 'summer', bd = 3,pady=10, command = lambda:choix_commencement(fen,grille,niveau="difficile"))
    b_quitter = Button(frame, text="Quitter", font = 'summer', bd = 3,pady=10, command=fen.destroy)

    b_facile.pack(side="top",pady=5, fill=X)
    b_moyen.pack(side="top",pady=5, fill=X)
    b_difficile.pack(side="top",pady=5, fill=X)
    b_invaic.pack(side="top",pady=5, fill=X)
    b_quitter.pack(side="top",pady=5, fill=X)
    
def choix_commencement(fen,grille,niveau="t_facile") :
    '''
    Fontion pour choisr qui commence en premier entre bot et humain
    :param fen: fenêtre où mettre les éléments
    :param grille: matrice de la grille
    :param niveau: niveau de difficulté de joueur contre un bot
    '''
    frame = fen.winfo_children()[0]
    effacer_contenu_frame(frame)
    
    texte = Label(frame,text="Qui commence (cliquez dessus) ?",borderwidth=3, padx = 5, pady=10, bg="white")
    b_joueur = Button(frame, text="Joueur", font = 'summer', bd = 3,pady=10, command = lambda:fenetre_jeu(fen,grille,niveau))
    b_bot = Button(frame, text="Bot", font = 'summer', bd = 3,pady=10, command = lambda:fenetre_jeu(fen,grille,niveau,bot=True))
    texte.pack(side="top",pady=5, fill=X)
    b_joueur.pack(side="top",pady=5, fill=X)
    b_bot.pack(side="top",pady=5, fill=X)
    
def effacer_contenu_frame(frame):
    """
    Fonction pour effacer tout le contenu d'une frame
    
    : param frame: la frame dont le contenu est à effacer
    """
    for widgets in frame.winfo_children():
        widgets.destroy()
