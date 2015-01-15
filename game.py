"""Les fonctions de gestion du jeu"""

from terrain import *
from random import randint

#Coin des paramètres qui seront plus tard définis dans la fenêtre de paramétrage
NOMBRE_JOUEURS=4
NOMBRE_OBJECTIFS_JOUEUR=3
NOMBRE_TOTAL_OBJECTIFS=24

joueurs = [] # Infos sur les joueurs [ [ NOM , score, objectifs ] ]
JOUEUR_NOM, JOUEUR_SCORE, JOUEUR_OBJECTIFS = 0,1,2

caseDispo = [] # La carte hors jeu

def commencer(taille=7, nbObjectifs=30, gamemode=0) :
    '''Initialise ou réinitialise le jeu.
    Entrées :
        - taille : largeur/hauteur de la map (doit être impair)
        - nbObjectifs : nombre d'objectifs à placer sur la map
        - gamemode : le mode de jeu'''
    
    NOMBRE_TOTAL_OBJECTIFS = nbObjectifs
    nbJoueurs = len(joueurs)
    
    carte[:] = [ [] ] * (taille**2)
    
    # Placement des coins et des joueurs
    for joueur in range(4) :
         # Définis le coins / les spawn
        horizontal = joueur%2
        vertical = (joueur+(joueur//2))%2
        caseJoueur = case( horizontal*(taille-1) , vertical*(taille-1) )
        
        infosCase = [0]*3
        infosCase[CASE_OUVERTURES] = [bool(vertical), bool(horizontal), not(vertical), not(horizontal)]
        infosCase[CASE_OBJECTIF] = -1
        
        if joueur < nbJoueurs : # Si tous les joueurs ne sont pas placés, on en place un
            joueurs[joueur][JOUEUR_SCORE] = 0
            infosCase[CASE_JOUEURS] = [joueur]
        else :
            infosCase[CASE_JOUEURS] = []
        
        carte[caseJoueur] = infosCase
        
    # Placement des autre cases statiques
    hauteurMax = int(taille/2) + int(taille/2)%2 # cas de la case au milieu
    for hauteur in range(0, hauteurMax+1, 2): # Une ligne sur deux
        for orientation in range(4) : # On fait le tour du plateau
            xMax = taille - 2*hauteur*(not hauteur >= hauteurMax)
            for x in range(0, xMax+1, 2) :
                if( carte[case(x, hauteur)] == [] ) :
                    carte[case(x, hauteur)] = [ [False, True, True, True], -1, [] ]
            tournerCarte()
            
    # Répartition des autres cases
    nbPieces = compterPieces()
    listePieces = nbPieces[0]*[[False, True, False, True]] + nbPieces[1]*[[False, False, True, True]] + nbPieces[2]*[[True, True, False, True]]
    for pos in range(taille**2) :
        if carte[pos] == [] :
            i = randint(0, len(listePieces))-1
            piece = [ listePieces[i], -1, [] ]
            tournerCase(piece, randint(1,4))
            del listePieces[i]
            carte[pos] = piece
    caseDispo = listePieces[0]
    
    # Placement des objectifs
    casesLibres = list(range(taille**2))
    for objectif in range(nbObjectifs) :
        i = randint(0, len(casesLibres)-1)
        caseObj = casesLibres[i]
        carte[caseObj][CASE_OBJECTIF] = objectif
        casesLibres.remove(caseObj)


def compterPieces() :
    '''Donne la liste des pièces non-fixes
    Sortie : le nombre de pièce pour chaque type dans une liste :
        - 0 : ligne  [False, True, False, True]
        - 1 : coin   [False, False, True, True]
        - 2 : triple [True, True, False, True] '''
    # Pour un 7x7 : 13 lignes, 15 coins, 6 triples
    
    nbPieces = taille()**2 - int(taille()/2+1)**2 + 1
    lignes = int(0.4 * nbPieces)
    coins = int(0.45 * nbPieces)
    triples = nbPieces -lignes -coins
    
    return [lignes, coins, triples]


def recupObjectif(joueur):
    '''Vérifie si un objectif cherché par le joueur est sur la case où il se trouve
    Dans le cas où il s'y trouve:
        - enlève l'objectif de la liste du joueur
        - incrémente le score du joueur'''
    Joueur = joueurs[joueur]
    case = carte[positionJoueur(joueur)]
    listeObj = Joueur[JOUEUR_OBJECTIFS][:] #On crée une copie pour la boucle for
    for i in range(len(listeObj)):
        objectif = listeObj[i]
        if objectif == case[CASE_OBJECTIF]:
            print("Objectif récupéré!!")
            del(Joueur[JOUEUR_OBJECTIFS][i])
            Joueur[JOUEUR_SCORE]+=1



def casesAccessibles(case):
    '''Renvoie la liste des cases accessibles depuis une case donnée'''
    #On crée une liste pleine de zéros puis on del les 0 à la toute fin
    Case=carte[case]
    Cases=[None]*len(carte)
    Cases[case]=case
    ProvisoireRef=[None]*len(carte)
    ProvisoireRef[case]=case
    fin=False
    while fin==False:
        Provisoire=ProvisoireRef[:]
        for i in Cases:
            if i!=None:
                for k in casesAdjacentes(i):
                    Provisoire[k]=k
        if Provisoire==Cases:
            fin=True
        else:
            for i in Provisoire:
                if i!=None:
                    Cases[i]=i
    for i in range(Cases.count(None)): Cases.remove(None)
    return(Cases)
    

    
    
def bougerJoueur(joueur, case):
    '''Déplace le joueur vers une autre case si ce déplacement est permis
    Pour l'instant, en affichage console, on debug la carte
    On vérifie également s'il y a un objectif récupérable'''
    erreur=True
    for i in casesAccessibles(positionJoueur(joueur)):
        if i==case:
            erreur=False
    if erreur==True: return('Mouvement impossible')
    carte[positionJoueur(joueur)][CASE_JOUEURS].remove(joueur)
    carte[case][CASE_JOUEURS]+=[joueur]
    debugerCarte()
    recupObjectif(joueur)