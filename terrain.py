# coding=utf-8
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


def coordonneesCase(case) :
    '''Retourne les coordonnées d'une case
    Entrée :
        - case : le numéro de case
    Sortie :
        - x
        - y '''
    
    x = case % taille()
    y = case // taille()
    return x,y


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


def casesAdjacentes(case) :
    '''Retourne les cases adjacentes d'une case
    Entrée :
        - case : la case centrale
    Sortie :
        - listeCases : les cases adjacentes '''
        
    listeCases = []
    x,y = coordonneesCase(case)
    for dif in [-1, 1, taille(), -taille()] :
        caseProche = case + dif
        xp,yp = coordonneesCase(caseProche)
        if abs(xp-x) + abs(yp-y) == 1 and caseProche >= 0 : # Une sorte de xor
            listeCases += [caseProche]
    return listeCases


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
    

## Debugage de la map en console
    
    
def debugerCarte() :
    '''Affiche la carte en ascii dans la console
    Retours : juste un affichage console'''
    
    def formeAscii(case) :
        '''Donne la forme en ascii d'une case
        Entrée : la case dont on veut la forme
        Sortie : trois chaines de 3 caractères, correspondantes à 3 lignes'''
        
        if case == [] :
            return [ "   ", "   ", "   " ]
        
        croix = '+'
        ligne = '─'
        colone = 'ǀ'
        
        sortie = 3*[[]]
        for i in range(3) :
            sortie[i] = 3*[" "]
        
        sortie[0][1] = colone if case[CASE_OUVERTURES][0] else " "
        sortie[1][0] = ligne  if case[CASE_OUVERTURES][1] else " "
        sortie[2][1] = colone  if case[CASE_OUVERTURES][2] else " "
        sortie[1][2] = ligne if case[CASE_OUVERTURES][3] else " "
        
        sortie[1][1] = croix
        
        #todo: afficher tous les joueurs
        sortie[0][0] = str(case[CASE_JOUEURS][0]) if len(case[CASE_JOUEURS]) >= 1 else " "
        
        return [ "".join(sortie[0]), "".join(sortie[1]), "".join(sortie[2]) ]
        
        
    for ligne in range(taille()) :
        arrayLigne = 3*[""]
        for colone in range(taille()) :
            for i in range(3) :
                arrayLigne[i] += " " + formeAscii(carte[case(colone, ligne)])[i]
        print('\n'.join(arrayLigne))