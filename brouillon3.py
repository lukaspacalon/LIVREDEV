from threading import Thread
import time

import sched
import sys


#inventaire_initial = [objet.h1.__dict__, objet.h2.__dict__, objet.d1.__dict__, objet.n1.__dict__, objet.n2.__dict__]
niveau = 0
#inventaire_initial = [objet.h1_habit_de_lin.__dict__, objet.h2_chaussure_de_cuir.__dict__, objet.l1_carte_tarik.__dict__, objet.n1_bout_de_pain.__dict__, objet.n2_pomme.__dict__]
inventaire_initial = 1

##### joueur config #####
class joueur:
    def __init__(self):
        self.nom = ''
        self.race = ''
        self.hp = 100
        self.mp = 100
        self.statut = []
        self.localisation = 'b2'
        self.mort = False
        self.niveau = niveau
        self.inventaire_joueur = inventaire_initial
        self.faim = 100
        self.soif = 100
        print("Création du Joueur", self)

    def quisuisje(self):
        print("nom : {} niveau : ({})".format(self.nom, self.niveau))
        print("race : {} localisation : ({})".format(self.race, self.localisation))
        print("mort ? {} statut : ({})".format(self.mort, self.statut))
        print("hp : {} mp : {}".format(self.hp, self.mp))
        print("faim : {} % soif : {} %".format(self.faim, self.soif))

    def parler(self, message):
        print("{} a dit : {}".format(self.nom, message))

    def Regarder_inventaire(self):
        print("{}".format(self.inventaire_joueur))

    def Lire(ouvrage):
        print(ouvrage)

mon_joueur = joueur()




class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()

    def run(self):
        while (True):
            self.foo()
            time.sleep(1)

    def foo(self):
        if mon_joueur.faim > -1:
            mon_joueur.faim -= 10
            if mon_joueur.faim <50:
                print("Vous avez faim")
            if mon_joueur.hp <10:
                print("Vous êtes gravement blessé")
            if mon_joueur.faim <0:
                print("Vous êtes mort de faim")
            if mon_joueur.hp <0:
                print("Vous êtes mort de vos blessures")


my = None

while True:
    user_input = input("What do I do ? ")

    if user_input == "s":
        #Will start a threat that prints foo every second.
        if my == None:
            print("Starting thread...")
            my = MyThread()
        else:
            print("Thread is already started.")

    elif user_input == "hello":
        print("Hello !")

    elif user_input == "f":
        mon_joueur.quisuisje()

    else:
        print("This is not a correct command.")


# Bienvenue dans le Livre programmé dont vous êtes le Héro Développeur
# coding:utf-8
# https://trello.com/b/4L1gpwt1/chroniques
# Procédural
