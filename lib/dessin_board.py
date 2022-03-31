import lib.config as cf

def dessiner_x(can,i,j):
    """
    Fonction pour dessiner dans le canevas la croix en rougne.
    """
    x0 = cf.MARGIN + i*cf.SIDE
    y0 = cf.MARGIN + j*cf.SIDE
    x1 = x0+cf.SIDE
    y1 = y0+cf.SIDE
    can.create_line(x0, y0, x1, y1, width=2, fill="red")
    y0,y1= y1,y0
    can.create_line(x0, y0, x1, y1, width=2, fill="red")
    #print(x0,y0,x1,y1)

def dessiner_rond(can,i,j):
    """
    Fonction pour dessiner dans le canevas le rond bleu
    """
    x0 = cf.MARGIN + i*cf.SIDE
    y0 = cf.MARGIN + j*cf.SIDE
    x1 = x0+cf.SIDE
    y1 = y0+cf.SIDE 
    can.create_oval(x0, y0, x1, y1, outline="blue")
    
    
def dessiner_grille(can):
    
    """
    Fonction pour dessiner la grille dans le canevas.
    """
    
    for i in range(4):
        x0 = cf.MARGIN + i*cf.SIDE
        y0 = cf.MARGIN
        x1 = cf.MARGIN + i*cf.SIDE
        y1 = cf.MARGIN + 3* cf.SIDE
        
        can.create_line(x0, y0, x1, y1, width=2, fill="black")
        
        
        x0 = cf.MARGIN 
        y0 = cf.MARGIN + i*cf.SIDE
        x1 = cf.MARGIN + 3*cf.SIDE
        y1 = cf.MARGIN + i* cf.SIDE
        
        can.create_line(x0, y0, x1, y1, width=2, fill="black")

