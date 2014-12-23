# coding=utf-8
"""Les fonctions de gestion du jeu"""

from terrain import *
from random import randint

joueurs = [] # Infos sur les joueurs
caseDispo = [] # La carte hors du terrain

def commencer(nbJoueurs=4, taille=7) :
    '''Initialise ou réinitialise le jeu.
    Entrées :
        - nbJoueurs : nombre de joueurs (compris entre 2 et 4)
        - taille : largeur/hauteur de la map (doit être impair)'''
    
    carte[:] = [ [] ] * (taille**2)
    joueurs[:] = [0] * nbJoueurs
    
    # Placement des coins et des joueurs
    for joueur in range(4) :
         # Définis le coins / les spawn
        horizontal = joueur%2
        vertical = (joueur+(joueur//2))%2
        caseJoueur = case( horizontal*(taille-1) , vertical*(taille-1) )
        
        infosCase = [0]*3
        infosCase[CASE_OUVERTURES] = [bool(vertical), bool(horizontal), not(vertical), not(horizontal)]
        infosCase[CASE_OBJECTIFS] = False
        if joueur < nbJoueurs : # Si tous les joueurs ne sont pas placés, on en place un
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
                    carte[case(x, hauteur)] = [ [False, True, True, True], False, [] ]
            tournerCarte()
            
    # Répartition des autres cases
    nbPieces = compterPieces()
    listePieces = nbPieces[0]*[[False, True, False, True]] + nbPieces[1]*[[False, False, True, True]] + nbPieces[2]*[[True, True, False, True]]
    for pos in range(taille**2) :
        if carte[pos] == [] :
            i = randint(0, len(listePieces))-1
            piece = [ listePieces[i], False, [] ]
            tournerCase(piece, randint(1,4))
            del listePieces[i]
            carte[pos] = piece
    caseDispo = listePieces[0]


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
    
