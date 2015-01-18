from game import *
from terrain import *

from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFilter
import os.path

CANVAS_SIZE = 500 # taille de la fenetre
TEXTURE = "1"

PATERN = [ [False, False, True, True],   # Les patern de case correspondant aux images enregistrées
           [True, False, True, True],
           [True, False, True, False] ]
           
JOUEUR_COULEURS = [
    (100, 160, 100),
    (120, 100, 160),
    (200, 60, 60),
    (130, 130, 130)
]
           
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
        
    tailleCase = 100
    tailleJoueur = 40
    tailleObjectif = 60
    
    joueur = etatJeu[JEU_JOUEUR]
        
    caseType = [ PATERN[typeCase(case)], -1, [] ]
    image = Image.open("img/patern/" + TEXTURE + "/" + str(typeCase(case)) + ".png")
    image = image.resize((tailleCase,tailleCase))
    
    while caseType[CASE_OUVERTURES] != case[CASE_OUVERTURES] :
        tournerCase(caseType)
        image = image.rotate(90)
    
    # Ajout de l'objectif
    if case[CASE_OBJECTIF] != -1 :
        imgObj = Image.open("img/objectif/" + str(case[CASE_OBJECTIF]) + ".gif")
        imgObj = imgObj.resize((tailleObjectif, tailleObjectif))
        origine = ( tailleCase - tailleObjectif ) // 2
        image.paste(imgObj, (origine, origine), imgObj.convert("RGBA"))
    
    # Ajout des joueurs
    if len(case[CASE_JOUEURS]) == 1 :
        origine = ( tailleCase - tailleJoueur ) // 2
    else :
        origine = tailleCase // 2 -tailleJoueur
    x,y = 0,0
    for joueur in case[CASE_JOUEURS] :
        dessin = ImageDraw.Draw(image)
        xdraw, ydraw = x*tailleJoueur+origine, y*tailleJoueur+origine
        dessin.ellipse((xdraw-10, ydraw-10, xdraw+tailleJoueur+10, ydraw+tailleJoueur+10), fill = JOUEUR_COULEURS[joueur])
        
        imgJ = imageJoueur(joueur).resize((tailleJoueur, tailleJoueur))
        image.paste(imgJ, (x*tailleJoueur+origine, y*tailleJoueur+origine), imgJ.convert("RGBA"))
        x = 1-x if y == 0 else x
        y = 1-y
        
        if joueur == etatJeu[JEU_JOUEUR] :
            imgJ = ImageTk.PhotoImage(imgJ)
            joueurCourrant.configure(image=imgJ)
            joueurCourrant.image = imgJ
    
    # Le truc badass
    if etatJeu[JEU_ETAPE] == ETAPE_BOUGER and idCase != -1 :
        if not(idCase in casesAccessibles(positionJoueur(joueur))) and idCase != -1 :
            image = image.filter(ImageFilter.BLUR)
    elif etatJeu[JEU_ETAPE] == ETAPE_PIECE :
        x,y = coordonneesCase(idCase)
        if not(x%2) and not(y%2) :
            image = image.point(lambda x : x*0.8)
            image = image.filter(ImageFilter.MinFilter)
            
    if case[CASE_OBJECTIF] in joueurs[joueur][JOUEUR_OBJECTIFS] :
        cible = Image.open("img/cible.png").resize((25,25))
        image.paste(cible, (0,0), cible.convert("RGBA"))
    
    return image
    
    
def imageJoueur(joueur) :
    """Donne l'image associée au joueur
    Entrée ;
        - joueur : l'index du joueur
    Sortie :
        - une image au format PIL """
        
    fichierPerso = "img/joueur/" + joueurs[joueur][JOUEUR_NOM] + ".png";
    fichierDefaut = "img/joueur/" + str(joueur) + ".png";
    if os.path.isfile(fichierPerso) :
        return Image.open(fichierPerso).resize((50,50))
    else :
        return Image.open(fichierDefaut).resize((50,50))


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
    """Fonction appelée au clic sur une case
    Entrées :
        - Event (osef)
        - case : le numéro de case correspondante
    Sortie :
        - L'état du jeu probablement modifié"""
    
    if etatJeu[JEU_ETAPE] == ETAPE_PIECE :
        insererPiece(case)
    elif etatJeu[JEU_ETAPE] == ETAPE_BOUGER :
        bougerJoueur(case)
        
    refreshJeu()
    

def refreshJeu() :
    """Rafraichis entièrement l'interface du jeu
    Rechauffe aussi la pièce en créant volontairement des fonctions très lourdes dans le but
        - de faire travailler le processeur
        - d'inciter l'utilisateur a retourner au travail"""
    
    tailleObjectif = 50 # Seulement l'affichage en bas
    
    global saveImgs
    
    tailleCase = CANVAS_SIZE//taille()
    
    # Affichage de la grille
    for x in range(taille()) :
        for y in range(taille()) :
            idCase = case(x, y)
            img = imageCase(carte[idCase], idCase)
            img = img.resize((tailleCase, tailleCase))
            img = ImageTk.PhotoImage(img) # Conversion pour tkinter
            affichageTerrain.create_image(((x+0.5)*tailleCase, (y+0.5)*tailleCase), image=img, tag="-"+str(idCase))
            affichageTerrain.tag_bind("-"+str(idCase), "<Button-1>", lambda event,case=idCase : caseClic(event, case)) # L'astuce du campeur
            saveImgs += [img] # Il faut garder l'image en mémoire, j'ai rien trouvé d'autre
        
    # Affichage de la case libre
    img = imageCase(caseDispo)
    img = img.resize((tailleCase, tailleCase))
    img = ImageTk.PhotoImage(img)
    caseLibre.configure(image=img)
    caseLibre.image = img # Plus propre pour garder en memoire
    
    for i in range(1,4) :
        tournerCase(caseDispo)
        imgCase = imageCase(caseDispo).resize((tailleCase//3, tailleCase//3))
        imgCase = ImageTk.PhotoImage(imgCase)
        choixRotation.create_image((tailleCase/6, (i-0.5)*tailleCase/3), image=imgCase, tag="--"+str(i))
        choixRotation.tag_bind("--"+str(i), "<Button-1>", lambda event,rot=i : tournerCaseDispo(rot))
        saveImgs += [imgCase]
    tournerCase(caseDispo)
    
    # Affichage des objectifs du joueur courrant
    listeObjectifs = joueurs[etatJeu[JEU_JOUEUR]][JOUEUR_OBJECTIFS]
    imgTtObj = Image.new("RGBA", (tailleObjectif*len(listeObjectifs), tailleObjectif))
    for i in range(len(listeObjectifs)) :
        objectif = listeObjectifs[i]
        imgObj = Image.open("img/objectif/" + str(objectif) + ".gif")
        imgTtObj.paste(imgObj, (i*tailleObjectif, 0), imgObj.convert("RGBA") )
    imgTtObj = ImageTk.PhotoImage(imgTtObj)
    objectifsJoueur.configure(image=imgTtObj)
    objectifsJoueur.image = imgTtObj
        
    # Etat du jeu
    textEtat = "Tour " + str(etatJeu[JEU_TOUR]) + " , " + str(joueurs[etatJeu[JEU_JOUEUR]][JOUEUR_NOM])
    labelEtat.configure(text = textEtat)
    fenJeu.title("Labyrinthe | " + textEtat)


def tournerCaseDispo(nombre = 1) :
    """Fait roter la case hors-jeu, et rafraichis l'affichage"""
    tournerCase(caseDispo, nombre)
    refreshJeu()


fenJeu=Tk()

affichageTerrain = Canvas(fenJeu, bg='grey', width=CANVAS_SIZE, height=CANVAS_SIZE)
affichageTerrain.pack()

objectifsJoueur = Label(fenJeu)
objectifsJoueur.pack(side=LEFT)

joueurCourrant = Label(fenJeu)
joueurCourrant.pack(side=RIGHT)

choixRotation = Canvas(fenJeu, bg='grey', width=CANVAS_SIZE//(3*taille()), height=CANVAS_SIZE//taille())
choixRotation.pack(side=RIGHT)

caseLibre = Label(fenJeu)
caseLibre.pack(side=RIGHT)

tourner=Button(fenJeu, text='Rotation',width=10,command=tournerCaseDispo)
tourner.pack(side=BOTTOM)

labelEtat=Label(fenJeu, text="",width=50, fg='Black')
labelEtat.pack(side=BOTTOM)