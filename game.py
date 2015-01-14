"""Les fonctions de gestion du jeu"""

from terrain import *
from random import randint

joueurs = [] # Infos sur les joueurs [ [ NOM , SCORE, OBJECTIFS ] ]
JOUEUR_NOM, JOUEUR_SCORE, JOUEUR_OBJECTIFS = 0,1,2

caseDispo = [] # La carte hors jeu

def commencer(taille=7, nbObjectifs=25, gamemode=0) :
    '''Initialise ou réinitialise le jeu.
    Entrées :
        - taille : largeur/hauteur de la map (doit être impair)
        - nbObjectifs : nombre d'objectifs à placer sur la map
        - gamemode : le mode de jeu'''
    
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
    