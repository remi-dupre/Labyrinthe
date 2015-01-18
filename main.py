from game import *
from settings import *
from random import randint


for i in settingsNoms():
    if i!=0:
        joueurs += [ [i, 0, []] ]

commencer(7, NOMBRE_TOTAL_OBJECTIFS)

Objectifs=list(range(NOMBRE_TOTAL_OBJECTIFS))

TirageObjectifs=Objectifs[:]
for i in range(NOMBRE_OBJECTIFS_JOUEUR):
    for k in range(len(joueurs)):
        al=randint(0,len(TirageObjectifs)-1)
        joueurs[k][JOUEUR_OBJECTIFS]+=[TirageObjectifs[al]]
        del(TirageObjectifs[al])
        
        

debugerCarte()