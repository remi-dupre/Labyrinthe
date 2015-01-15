from game import *
from random import randint

joueurs += [ ["Daniel", 0, []] ]
joueurs += [ ["Kouby", 0, []] ]
joueurs += [ ["Whoping", 0, []] ]


commencer(7, NOMBRE_TOTAL_OBJECTIFS)

Objectifs=list(range(NOMBRE_TOTAL_OBJECTIFS))

TirageObjectifs=Objectifs[:]
for i in range(NOMBRE_OBJECTIFS_JOUEUR):
    for k in range(len(joueurs)):
        al=randint(0,len(TirageObjectifs)-1)
        joueurs[k][JOUEUR_OBJECTIFS]+=[TirageObjectifs[al]]
        del(TirageObjectifs[al])
        
        
joueurs += [ ["Daniel", 0, []] ]
joueurs += [ ["Kouby", 0, []] ]
joueurs += [ ["Whoping", 0, []] ]

commencer(7, 25)
debugerCarte()