# Bienvenue dans le Livre programmé dont vous êtes le Héro Développeur
# coding:utf-8
# https://trello.com/b/4L1gpwt1/chroniques
# Procédural


class Personnage:
    personnages_crees = 0
    def __init__(self, c_prenom, c_age, c_race):
        self.prenom = c_prenom
        self.age = c_age
        self.race = c_race
        Personnage.personnages_crees +=1
        print("Decouverte d'un personnage", self)

    def se_deplacer(self, vitesse):
        print("{} se déplace {}".format(self.prenom, vitesse))

    def parler(self, message):
        print("{} a dit : {}".format(self.prenom, message))

class Humain(Personnage):
    """ Les humains constituent la race la plus courante du Vieux Monde
et restent les fondateurs de l’Empire. """

class Nain(Personnage):
    """ Les humains constituent la race la plus courante du Vieux Monde
et restent les fondateurs de l’Empire. """

class Elfe(Personnage):
    """ Les humains constituent la race la plus courante du Vieux Monde
et restent les fondateurs de l’Empire. """

p1 = Personnage("Jojo", 27, "humain")
#print ("prenom de p1 -> {}".format(p1.prenom))
#print ("age de {} -> {} ans".format(p1.prenom, p1.age))

p2 = Personnage("Albert", 32, "nain")
#print ("prenom de p2 -> {}".format(p2.prenom))
#print ("age de {} -> {} ans".format(p2.prenom, p2.age))

p3 = Personnage("Camille", 18, "elfe")
#print ("prenom de p2 -> {}".format(p3.prenom))
#print ("age de {} -> {} ans".format(p3.prenom, p3.age))

#print("Personnage existant : {}".format(Personnage.personnages_crees))
