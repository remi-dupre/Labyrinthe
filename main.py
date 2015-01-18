from game import *
from settings import *
from random import randint


for i in settingsNoms():
    if i!=0:
        joueurs += [ [i, 0, []] ]


commencer(7, 24)
debugerCarte()
carte[0][CASE_JOUEURS] += [1]

from interface import *
lancerInterface()
