from tkinter import *
from PIL import Image, ImageTk

from terrain import *
from game import *

CANVAS_SIZE = 400 # taille de la fenetre

PATERN = [ [True, True, False, True],   # Les patern de case correspondant aux images enregistrées
           [False, True, False, True],
           [True, False, False, True] ]
           
saveImgs = []


def lancerInterface() :
    """Ouvre la fenetre pour lancer la partie"""
    refreshJeu()
    fenJeu.mainloop()


def imageCase(case, idCase=-1) :
    """Génère l'image de la case donnée en argument
    Entrées :
        - case : l'array décrivant la case
        - idCase (facultatif) : l'identifiant de la case sur le plateau
    Sortie :
        - L'image au format PIL"""
        
    caseType = [ PATERN[typeCase(case)], -1, [] ]
    image = Image.open("img/patern/" + str(typeCase(case)) + ".png")
    
    while caseType[CASE_OUVERTURES] != case[CASE_OUVERTURES] :
        tournerCase(caseType) #todo: si ca bug ca peut etre là
        image = image.rotate(90)
    
    return image


def typeCase(case) :
    """Retourne le patern correspondant à la case
    Entrée :
        case : l'array descriptif de la case
    Sortie :
        l'index du patern associé dans PATERN"""
        
    idPatern = -1
    for i in range(4) :
        tournerCase(case)
        for pat in range(len(PATERN)) :
            if case[CASE_OUVERTURES] == PATERN[pat] :
                idPatern = pat
    return idPatern
    
    
def caseClic(event, case) :
    if etatJeu[JEU_ETAPE] == ETAPE_PIECE :
        insererPiece(case)
    elif etatJeu[JEU_ETAPE] == ETAPE_BOUGER :
        bougerJoueur(case)
        
    refreshJeu()
    

def refreshJeu() :
    """ """ #todo: specifs
    
    global saveImgs
    
    tailleCase = CANVAS_SIZE//taille()
    
    # Affichage de la grille
    for x in range(taille()) :
        for y in range(taille()) :
            idCase = case(x, y)
            img = imageCase(carte[idCase], idCase)
            img = img.resize((tailleCase, tailleCase))
            img = ImageTk.PhotoImage(img) # Conversion pour tkinter
            affichageTerrain.create_image((x*tailleCase+35, y*tailleCase+35), image=img, tag="-"+str(idCase))
            affichageTerrain.tag_bind("-"+str(idCase), "<Button-1>", lambda event,case=idCase : caseClic(event, case)) # L'astuce du campeur
            saveImgs += [img] # Il faut garder l'image en mémoire, j'ai rien trouvé d'autre
        
    # Affichage de la case libre
    img = imageCase(caseDispo)
    img = img.resize((tailleCase, tailleCase))
    img = ImageTk.PhotoImage(img)
    caseLibre.configure(image=img)
    caseLibre.image = img # Plus propre pour garder en memoire
    
    textEtat = "Tour " + str(etatJeu[JEU_TOUR]) + " , " + str(joueurs[etatJeu[JEU_JOUEUR]][JOUEUR_NOM])
    labelEtat.configure(text = textEtat)
    fenJeu.title("Labyrinthe | " + textEtat)


def tournerCaseDispo() :
    """Fait roter la case hors-jeu, et rafraichis l'affichage"""
    tournerCase(caseDispo)
    refreshJeu()
    print(caseDispo)


fenJeu=Tk()

affichageTerrain = Canvas(fenJeu, bg='dark grey', width=CANVAS_SIZE, height=CANVAS_SIZE)
affichageTerrain.pack()

caseLibre = Label(fenJeu)
caseLibre.pack(side=RIGHT)

tourner=Button(fenJeu, text='Rotation',width=10,command=tournerCaseDispo)
tourner.pack(side=BOTTOM)

labelEtat=Label(fenJeu, text="",width=50, fg='Black')
labelEtat.pack(side=BOTTOM)