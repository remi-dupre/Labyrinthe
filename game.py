# coding=utf-8
"""Les fonctions de gestion du jeu"""

from terrain import *

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
    for hauteur in range(0, int(taille/2), 2): # Une ligne sur deux
        for orientation in range(4) : # On fait le tour du plateau
            for x in range(0, taille - 2*hauteur, 2) :
                if( carte[case(x, hauteur)] == [] ) :
                    carte[case(x, hauteur)] = [ [False, True, True, True], False, [] ]
            tournerCarte()