"""Opérations sur le terrain"""

from numpy import sqrt


carte = []# Infos sur les cases du jeu

CASE_OUVERTURES = 0
CASE_OBJECTIFS = 1
CASE_JOUEURS = 2


def case(x, y) :
    '''Retourne le numéro de la case correspondant aux coordonnées (x,y)
    x et y sont compris entre 0 et "Largeur map"-1'''
    return x + y*taille()


def tournerCase(case, nombre=1) :
    '''Fait tourner une case dans le sens trigonométrique
    Entrées :
        - case : La case à faire tourner
        - nombre (facultatif) : le nombre de rotations à effectuer, entre 1 et 4
    Sortie :
        - La case donnée en entrée est modifiée
        - Retourne la case modifiée '''
        
    case[CASE_OUVERTURES] = case[CASE_OUVERTURES][-nombre:] + case[CASE_OUVERTURES][:-nombre]
    return case


def tournerCarte() :
    '''Effectue une rotation de la carte dans le sens trigonométrique
    Retour : 
        - La carte est modifiée
        - Retourne la carte modifiée '''
    
    nouvelleCarte = []
    for case in carte :
        if case != [] : # Si la carte n'est pas initialisée, il reste des cases vides
            tournerCase(case) # On fait tourner toutes les cases
    for ligne in range(taille()) :
        nouvelleCarte += carte[taille()-ligne-1 :: taille()]
        
    carte[:] = nouvelleCarte
    return carte
    
    
def taille() :
    '''Retourne la largeur/hauteur du jeu'''
    return int(sqrt(len(carte)))