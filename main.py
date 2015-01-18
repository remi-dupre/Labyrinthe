from game import *
from settings import *
from random import randint


for i in settingsNoms():
    if i!=0:
        joueurs += [ [i, 0, []] ]


commencer(7, 30)
debugerCarte()

from interface import *
lancerInterface()
