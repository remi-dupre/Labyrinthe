## DM IPT 2 - Rémi, Jules, Lucas - Labyrinthe

# * Gestion de la partie (2 personne) = { Fonctions sur l'état du jeu ; Dynamiques du jeu }
# * Interface (1 personne)
# 
# A décider avant de commencer :
#  - Permettre une taille réglable de la grille (pas trop dur à prioris, et puis ca apprend à pas HARDCODER
#  - Gérer plusieurs modes de jeu (plutot dur et une des variantes est plus adapté au jeu sur un seul ordi)
#     --> De toutes facons il faut fixer une variante ou non
#
# On pourrait essayer de gérer les parties en réseau en définitive

## Gestion de la partie
# Fonctions de retours sur l'état du jeu (--> Lucas ?)
#  - Savoir le joueur en cours, la phase de jeu
#  - Connaitre la disposition du terrain + savoir les cases où un joueur peut aller (surement des fonctions communes avec la partie qui suit)
#  - Positions des joueurs
#  - Objectif recherché 
#
# Dynamiques de jeu
#  - Répartition des éléments du jeu
#  - Commandes des joueurs :
#    . Fonctions du genre : déplacer son pion / insérer un bout de labyrinthe
#    . Empêcher les actions interdites
#  - Donner la raison de l'interdiction
#  - Gestion des rotations de phases de jeu / de tours

## Fonctions un peu générales (en gros si quelqu'un need il code)
# Donner la rotation d'une pièce (le sens trigo, toujours le sens trigo ...)
# Obtenir une case par ses coordonnées
# Toutes les fonctions dont on a besoins au fur et a mesure

## Gestion de l'interface
# Préparatifs :
#  - Définir les joueurs
#  - Choisir une taille de terrain
# En phase de jeu :
#  - Le terrain avec la position des joueurs, des objectifs.
#  - Les objectifs à collecter du joueur actuel, un indicateur s'il est choppé (en fait ca dépend des règles)
#  - Les objectifs trouvés des autres joueurs
#  - Orienter la pièce, la placer
# Et puis c'est aussi celui qui gère ca qui doit activer les fonctions déclanchant les différentes phases de jeu


## Le jeu (#TamerMathieu)
# Après une rapide analyse de l'original non piraté on a :
# 15 cases lignes, 6 cases a trois entrées toutes occupées par un objectif et 13 cases en coin dont 6 occupées par un objectif
# Les cases fixes sont toutes occupées par un objectif et sont toutes des cases à trois entrées
# Les coins sont des coins .... coincoincoin

## Structures de données
# Pour le stockage du terrain autant faire un truc du type leekwars avec un tableau de 49 et une structure du genre
# case[ ligne*7 + colone ] = [
#   CASE_OUVERTURES = [ haut, gauche, bas, droite ], # Des booléens, et le sens trigo ca fait scientifique et tout
#   CASE_OBJECTIFS = objectif, # Un int qui correspond à l'ID de l'objectif (un ID reservé pour pas d'objectif)
#   CASE_JOUEURS = [] # La liste des joueurs qui sont sur la case
# ]