"""Opérations sur le terrain"""

from numpy import sqrt


carte = []# Infos sur les cases du jeu

CASE_OUVERTURES = 0
CASE_OBJECTIF = 1
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
    


def casesAdjacentes(case) :
    '''Retourne les cases adjacentes d'une case où il est possible de se rendre 
    Entrée :
        - case : la case centrale
    Sortie :
        - listeCases : les cases adjacentes accessibles'''
        
    listeCases = []
    x,y = coordonneesCase(case)
    for dif in [[-1,1,3], [1,3,1], [taille(),2,0], [-taille(),0,2]] :
        caseProche = case + dif[0]
        xp,yp = coordonneesCase(caseProche)
        if abs(xp-x) + abs(yp-y) == 1 and caseProche >= 0 and caseProche<taille()**2: # Une sorte de xor
            if carte[caseProche][CASE_OUVERTURES][dif[2]] and carte[case][CASE_OUVERTURES][dif[1]]:
                listeCases += [caseProche]
    return listeCases

    
    
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


def positionJoueur(joueur):
    '''Renvoie la case associée à un joueur donné (en donnant le numéro du joueur)'''
    for i in range(len(carte)):
        case=carte[i]
        for k in case[CASE_JOUEURS]:
            if joueur==k:
                return i
    return None
    

##Jules

from tkinter import *

Terrain=Tk()

zone_dessin = Canvas(Terrain, bg='dark grey', width=660, height=660)
zone_dessin.pack()
zone_dessin.create_rectangle(50,50,610,610)
for k in range(1,7):                                                       #En gros ici on crée le quadrillage
    zone_dessin.create_line(50+80*k,50,50+80*k,610)
    zone_dessin.create_line(50,50+80*k,610,50+80*k)
bou1=Button(Terrain,text='Quitter',width=10,command=Terrain.destroy)          #J'ai juste crée un boutton Quitter parce que j'ai pas trop d'autre idées
bou1.pack(side=BOTTOM)
text=Label(Terrain, text= "Tour 2 : Joueur 1",width=50, fg='Black')
text.pack()                                                                #Exemple de texte pour le tour/tout ça par contre j'ai beau chercher je trouve pas commencer aggrandir la police ><

Terrain.mainloop()

def InterfaceGlobale (tour,javant,nbjoueurs):
    text=Label(Terrain, text="Tour tour : Joueur (1+javant)%nbjoueurs",fg="black") 
    text.pack()