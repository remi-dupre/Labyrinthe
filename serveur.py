# coding=utf-8
"""Gestion du serveur"""

import socket
import select

SERVEUR_PORT = 1337
clients_connectes = []

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(('', SERVEUR_PORT))

def lancerServeur() :
    ''' Lance une partie en mode serveur '''
    
    tours = 0
    
    serveur.listen(5)
    while True :
        connexions_demandees, wlist, xlist = select.select([serveur], [], [], 0.05)
        for connexion in connexions_demandees:
            connexion_avec_client, infos_connexion = connexion.accept()
            clients_connectes.append(connexion_avec_client)
