
# Bienvenue dans le Livre programmé dont vous êtes le Héro Développeur
# coding:utf-8
# https://trello.com/b/4L1gpwt1/chroniques

import source
import personnage
import bibliotheque
import joueur
import objet
import lieu

import cmd
import textwrap
import sys
import os
import sched, time
import random
import pickle
import inspect

#print(objet.sac_joueur[denier].__dict__)

page1 = source.LivreSource(1, 1, "Il était une fois...")
print ("Chapitre {}".format(page1.chapitre))
print ("Page {} :".format(page1.page))
print ("\n   {}".format(source.LivreSource.contenu_page))

#### Title Screen ####
def title_screen_selection():
    option = input("> ")
    if option.lower() in ['jouer', 'nouvelle partie']:
        config_jeu()
    elif option.lower() == "":
        title_screen_selection()
    elif option.lower() == ("charger"):
        charger_jeu()
        for liste_inventaire in joueur.mon_joueur.inventaire_joueur:
                print(liste_inventaire)
    elif option.lower() == ("aide"):
        aide_menu()
    elif option.lower() in ['quitter', 'exit', 'quit', 'close', 'q']:
        sys.exit()
    while option.lower() not in ['', 'quit', 'exit', 'close', 'nouvelle partie','charger', 'aide', 'quitter', 'jouer']:
        print("Cette commande n'est pas valide.")
        option = input("> ")
        if option.lower() in ['jouer', 'nouvelle partie']:
            config_jeu()
        elif option.lower() == "":
            title_screen_selection()
        elif option.lower() == ("charger"):
            charger_jeu()
        elif option.lower() == ("aide"):
            aide_menu()
        elif option.lower() in ['quitter', 'exit', 'quit', 'close', 'q']:
            sys.exit()

def title_screen():
    #os.system('cls')
    print("####################################")
    print('utilisez ces commandes : jouer (nouvelle partie), charger, aide, quitter')
    print("####################################")
    title_screen_selection()

def aide_menu():
    print("####################################")
    print('utilisez haut, bas, gauche, droite pour bouger')
    print("####################################")
    title_screen_selection()


def joueur_sauvegarder(action):
    joueur.mon_joueur.quisuisje()
    print("Comment voulez-les vous nommer votre sauvegarde ?")
    sauvegarde_nom = input("> ")
    if sauvegarde_nom.lower() in ['quitter', 'exit', 'quit', 'close', 'q']:
        sys.exit()
    sauvegarde_nom = sauvegarde_nom + ".data"
    with open("sauvegardes/"+ sauvegarde_nom, "wb") as fic_sauvegarde:
        record = pickle.Pickler(fic_sauvegarde)
        record.dump(joueur.mon_joueur)

def charger_jeu():
    afficher_sauvegarde()
    print("Quel partie voulez-vous charger ?")
    sauvegarde_charger = input("> ")
    if sauvegarde_charger.lower() in ['quitter', 'exit', 'quit', 'close', 'q']:
        sys.exit()
    with open("sauvegardes/"+ sauvegarde_charger, "rb") as fic_sauvegarde:
        get_record = pickle.Unpickler(fic_sauvegarde)
        joueur.mon_joueur = get_record.load()
    joueur.mon_joueur.quisuisje()
    main_jeu_loop()

def afficher_sauvegarde():
    contenu_dossier = os.listdir(r'C:\Users\lukas\Desktop\LivreDev\sauvegardes')
    print(contenu_dossier)

#### MAP ####


#-----------------
#|a1F|a2F|a3F|a4F|
#-----------------
#|b1F|b2F|b3T|b4F|
#-----------------
#|c1P|c2V|c3P|c4P|
#-----------------
#|d1P|d2P|d3P|d4V|
#-----------------

nom = "nom"
description = "description"
examination = "examiner"
resolution = False
haut = 'haut', 'nord'
bas = 'bas', 'sud'
gauche = 'gauche', 'Ouest'
droite = 'droite', 'Est'

resolution_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False,
                }

carte = {
"a1": {
                nom: "Forêt de Hautefeuille",
                description: "Vous êtes dans la Forêt de Hautefeuille, de nombreux arbres vous entourent",
                examination: "examiner",
                resolution: False,
                haut: "",
                bas: "b1",
                gauche: "",
                droite: "a2",
},
"a2": {
                nom: "Forêt de Hautefeuille",
                description: "Vous êtes dans la Forêt de Hautefeuille, de nombreux arbres vous entourent",
                examination: "examiner",
                resolution: False,
                haut: "",
                bas: "b2",
                gauche: "a1",
                droite: "a3",
},
"a3": {
                nom: "Forêt de Hautefeuille",
                description: "Vous êtes dans la Forêt de Hautefeuille, de nombreux arbres vous entourent",
                examination: "examiner",
                resolution: False,
                haut: "",
                bas: "b3",
                gauche: "a2",
                droite: "a4",
},
"a4": {
                nom: "Forêt de Hautefeuille",
                description: "Vous êtes dans la Forêt de Hautefeuille, de nombreux arbres vous entourent",
                examination: "examiner",
                resolution: False,
                haut: "",
                bas: "b4",
                gauche: "a3",
                droite: "",
},
"b1": {
                nom: "Forêt de Hautefeuille",
                description: "Vous êtes dans la Forêt de Hautefeuille, de nombreux arbres vous entourent",
                examination: "examiner",
                resolution: False,
                haut: "a1",
                bas: "c1",
                gauche: "",
                droite: "b2",
},
"b2": {
                nom: "Forêt de Hautefeuille",
                description: "Vous êtes dans la Forêt de Hautefeuille, de nombreux arbres vous entourent",
                examination: "examiner",
                resolution: False,
                haut: "a2",
                bas: "c2",
                gauche: "b1",
                droite: "b3",
},
"b3": {
                nom: "Vieille Tour",
                description: "Vous voyez une vielle tour au loin. Quand vous entrez dedans, elle semble abandonnée",
                examination: "examiner",
                resolution: False,
                haut: "a3",
                bas: "c3",
                gauche: "b2",
                droite: "b4",
},
"b4": {
                nom: "Forêt de Hautefeuille",
                description: "Vous êtes dans la Forêt de Hautefeuille, de nombreux arbres vous entourent",
                examination: "examiner",
                resolution: False,
                haut: "a4",
                bas: "c4",
                gauche: "b3",
                droite: "",
},
"c1": {
                nom: "Prairie de l'aude",
                description: "Vous êtes dans une grande prairie verdoyante.",
                examination: "examiner",
                resolution: False,
                haut: "b1",
                bas: "d1",
                gauche: "",
                droite: "c2",
},
"c2": {
                nom: "Village de Tarik",
                description: "Vous entre dans le village de Tarik, quelques maisons, queqlues huttes et une petite église composent ce lieu calme et paisible",
                examination: "examiner",
                resolution: False,
                haut: "b2",
                bas: "d2",
                gauche: "c1",
                droite: "c3",
},
"c3": {
                nom: "Prairie de l'aude",
                description: "Vous êtes dans une grande prairie verdoyante.",
                examination: "examiner",
                resolution: False,
                haut: "b3",
                bas: "d3",
                gauche: "c2",
                droite: "c4",
},
"c4": {
                nom: "Prairie de l'aude",
                description: "Vous êtes dans une grande prairie verdoyante.",
                examination: "examiner",
                resolution: False,
                haut: "b4",
                bas: "d4",
                gauche: "c3",
                droite: "",
},
"d1": {
                nom: "Prairie de l'aude",
                description: "Vous êtes dans une grande prairie verdoyante.",
                examination: "examiner",
                resolution: False,
                haut: "c1",
                bas: "",
                gauche: "",
                droite: "d2",
},
"d2": {
                nom: "Prairie de l'aude",
                description: "Vous êtes dans une grande prairie verdoyante.",
                examination: "examiner",
                resolution: False,
                haut: "c2",
                bas: "",
                gauche: "d1",
                droite: "d3",
},
"d3": {
                nom: "Prairie de l'aude",
                description: "Vous êtes dans une grande prairie verdoyante.",
                examination: "examiner",
                resolution: False,
                haut: "c3",
                bas: "",
                gauche: "d2",
                droite: "d4",
},
"d4": {
                nom: "Village du linceul",
                description: "Vous entrez dans le village du linceul, de vielles maisons de pierres, quelques fermes composent ce lieu pittoresque",
                examination: "examiner",
                resolution: False,
                haut: "c4",
                bas: "",
                gauche: "d3",
                droite: "",
}
}

def print_localisation():
    print('\n' + ('#' * (4 + len(joueur.mon_joueur.localisation))))
    print('#' + joueur.mon_joueur.localisation.upper() + '#')
    print('#' + carte[joueur.mon_joueur.localisation][description] + '#')
    print('\n' + ('#' * (4 + len(joueur.mon_joueur.localisation))))



def prompt():
    my = None
    while True:
        action = input("> ")
        if my == None:
            my = joueur.MyThread()
        #else:
        #    print("Thread is already started.")
        acceptable_actions = ['q', 'quit', 'exit', 'close', 'inventaire', '', 'sauvegarder', 'bouger', 'travel', 'walk', 'quitter', 'examiner', 'interact', 'look', 'moi', 'quisuisje']
        while action.lower() not in acceptable_actions:
            print('Action inconnue, essayez à nouveau ! (Tu peux faire ces actions : bouger, examiner, sauvegarder , inventaire, moi)\n')
            action = input("> ")
        if action.lower() in ['quitter', 'exit', 'quit', 'close', 'q']:
            sys.exit()
        elif action.lower() in ['bouger', 'travel', 'walk']:
            joueur_bouger(action.lower())
        elif action.lower() == '':
            prompt()
        elif action.lower() in ['examiner', 'interact', 'look']:
            joueur_examiner(action.lower())
        elif action.lower() in ['quisuisje', 'moi']:
            joueur_quisuisje(action.lower())
        elif action.lower() in ['sauvegarder']:
            joueur_sauvegarder(action.lower())
        elif action.lower() in ['inventaire']:
            joueur_inventaire(action.lower())


def joueur_bouger(monAction):
    ask = "Ou veux tu aller ?\n"
    dest = input(ask)
    if dest in ['haut', 'nord']:
        destination = carte[joueur.mon_joueur.localisation][haut]
        gestion_mouvement(destination)
    elif dest in ['gauche', 'Ouest']:
        destination = carte[joueur.mon_joueur.localisation][gauche]
        gestion_mouvement(destination)
    elif dest in ['Est', 'droite']:
        destination = carte[joueur.mon_joueur.localisation][droite]
        gestion_mouvement(destination)
    elif dest in ['sud', 'bas']:
        destination = carte[joueur.mon_joueur.localisation][bas]
        gestion_mouvement(destination)

def gestion_mouvement(destination):
    print("\n" + "Vous avez bouger en " + destination + ".")
    joueur.mon_joueur.localisation = destination
    print_localisation()

def joueur_examiner(action):
    print_localisation()
    if carte[joueur.mon_joueur.localisation][resolution]:
        print("Vous avez déjà examiner l'endroit")
    else:
        print("you can trigger a puzzle here")

def joueur_quisuisje(action):
    joueur.mon_joueur.quisuisje()

def joueur_inventaire(action):
    #for i,e in enumerate(joueur.mon_joueur.inventaire_joueur):
    #    print(i,e)




    inventaire_ouvert = True
    while inventaire_ouvert:
        print("\n")
        print("###################")
        for i, k in enumerate(objet.sac_joueur.inside):
            print(i, k)
        print("Quel objet de votre inventaire voulez-vous examiner ?")
        try:
            indice_inventaire = int(input("inventaire > "))
            if indice_inventaire in ['quitter', 'exit', 'quit', 'close', 'q']:
                inventaire_ouvert = False
            if indice_inventaire == "":
                continue
            result = isinstance(indice_inventaire, int)
            indice_inventaire = int(indice_inventaire)
            try:
                #objet.sac_joueur.inside[0].items()
                print("\n")
                print(tuple(objet.sac_joueur.inside.items())[indice_inventaire][0])
                print("\n")
                for i, k in enumerate(inspect.getmembers(tuple(objet.sac_joueur.inside.items())[indice_inventaire][1], predicate=inspect.ismethod)):
                    print(i, k)
                objet_examen = True
                while objet_examen:
                    action_objet = input("" + tuple(objet.sac_joueur.inside.items())[indice_inventaire][0] + " >")
                    if action_objet == "manger":
                        #print("vous mangez : " + tuple(objet.sac_joueur.inside.items())[indice_inventaire][0])
                        objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1]
                        objet.Nourriture.manger(objet_a_lindice)
                    elif action_objet == "jeter":
                        objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1]
                        objet.Objet.jeter(objet_a_lindice)
                    elif action_objet == "examiner":
                        objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1]
                        objet.Objet.examiner(objet_a_lindice)
                    elif action_objet == "lire":
                        objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1]
                        objet.Livre.lire(objet_a_lindice)
                    elif action_objet == "porter":
                        objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1]
                        objet.Habit.porter(objet_a_lindice)
                    elif action_objet == "enlever":
                        objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1]
                        objet.Habit.enlever(objet_a_lindice)
                    elif action_objet == "boire":
                        objet_a_lindice = tuple(objet.sac_joueur.inside.items())[indice_inventaire][1]
                        objet.Boisson.boire(objet_a_lindice)

                        #print(objet_a_lindice.__dict__["contenu"])
                        #print(bibliotheque.carte_tarik["plan"]["plan"])
                    else:
                        objet_examen = False
                #print(joueur.mon_joueur.inventaire_joueur[indice_inventaire])
                #objet.Habit.porter(objet.h1_habit_de_lin, joueur.mon_joueur.nom)
                #print(getattr(objet.h1_habit_de_lin, "nom"))
                #inspect.getmembers(objet.Habit, predicate=inspect.ismethod)
            except IndexError:
                print("Vous n'avez pas plus d'objet à examiner")
            #except TypeError:
            #    print("Vous ne pouvez qu'entrer des chiffres")

            if indice_inventaire in ['carte', 'map']:
                print(bibliotheque.carte_tarik["plan"]["plan"])
        except ValueError:
            print("Vous ne pouvez qu'entrer des chiffres")
            inventaire_ouvert = False






#### jeu FUNCIONALITY ####


def main_jeu_loop():
    while joueur.mon_joueur.mort is False:
        prompt()
    # Here handle if puzzle resolution, boss defeated, explored everything, etc...

def config_jeu():
    #os.system('cls')

    #nom
    qqq = "Fermier de Tarik dit : Hey! Reveille toi ! Tu peux pas rester ici ! C'est mon champs, je dois défricher avant l'arrivee du maire de Tarik ! C'est quoi ton nom au "
    question1 = "juste ? \n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.0001)
    joueur_nom = input("> ")
    joueur.mon_joueur.nom = joueur_nom

    #race HANDLING
    qqq2 = "par contre dis moi... tu as une drôle de tête.. De quel race es-tu ? (tu peux être un humain, un elfe ou un nain) "
    question2 = "Fermier de Tarik dit : Très bien " + joueur_nom + ", \n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.0001)
    joueur_race = input("> ")
    valid_races = ['humain', 'elfe', 'nain', '']
    if joueur_race.lower() in valid_races:
        joueur.mon_joueur.race = joueur_race
        print(joueur_nom + " dit : Je suis un " + joueur_race + "\n")
    while joueur_race.lower() not in valid_races:
        joueur_race = input("> ")
        if joueur_race.lower() in valid_races:
            print(joueur_nom + " dit : Je suis un " + joueur_race + "\n")

    #joueur STAT
    if joueur.mon_joueur.race == 'humain':
        joueur.mon_joueur.hp = 120
        joueur.mon_joueur.mp = 20
    elif joueur.mon_joueur.race == 'elfe':
        joueur.mon_joueur.hp = 40
        joueur.mon_joueur.mp = 120
    elif joueur.mon_joueur.race == 'nain':
        joueur.mon_joueur.hp = 60
        joueur.mon_joueur.mp = 60

    #INTRO
    qqq3 = "Fermier de Tarik dit : Hum... Je n'aime pas les gens de votre race dans le coin. " + joueur_nom + " le... " + joueur_race + " je vous conseille de déguerpir au plus vite avant l'arrivé des chevaliers.\n Fermier de Tarik s'en v"
    question3 = "a... "
    reponsehumain = "Fermier de Tarik dit : Ok bon... " + joueur_nom + " l'" + joueur_race + " je vous conseille de déguerpir au plus vite avant l'arrivé des chevaliers.\n Fermier de Tarik s'en va... "
    if joueur_race == "humain":
        for character in reponsehumain:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.0001)
    else:
        for character in question3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.0001)

    speech1 = "L'aventure commence !"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.0001)

    #os.system('cls')
    print(" C'est parti !")
    main_jeu_loop()

title_screen()
