from settings import *
from game import *

for i in settingsNoms():
    if i!=0:
        joueurs += [ [i, 0, []] ]
choixMode()
debugerCarte()


from interface import *
lancerInterface()
