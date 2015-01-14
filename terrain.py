# coding=utf-8
"""Opérations sur le terrain"""

from numpy import sqrt


carte = [] # Infos sur les cases du jeu
CASE_OUVERTURES , CASE_OBJECTIF , CASE_JOUEURS =  0,1,2

# Liste contenant les informations des taille**2 cases
# carte[l*taille + c] : case à la ligne l et colone c
#  - carte[case][CASE_OUVERTURES] dans le sens trigo, en partant du haut, une liste de booléen, True correspond à une ouverture
#  - carte[case][CASE_OBJECTIF] : l'ID de l'objectif sur la case, -1 s'il n'y en a pas
#  - carte[case][CASE_JOUEURS] : liste des joueurs sur la case


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
