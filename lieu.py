# Bienvenue dans le Livre programmé dont vous êtes le Héro Développeur
# coding:utf-8
# https://trello.com/b/4L1gpwt1/chroniques
# Procédural



class Village:
    villages_decouverts = 0
    def __init__(self, emplacement, nom_village, nombre_habitant):
        self.emplacement = emplacement
        self.nom = nom_village
        self.hab = nombre_habitant
        print("Découverte d'un village", self)
        Village.villages_decouverts +=1

class Foret:
    forets_decouvertes = 0
    def __init__(self, emplacement, nom_foret, taille_foret):
        self.emplacement = emplacement
        self.nom = nom_foret
        self.taille = taille_foret
        print("Découverte d'une Forêt", self)
        Foret.forets_decouvertes +=1

class Prairie:
    prairies_decouvertes = 0
    def __init__(self, emplacement, nom_foret, taille_foret):
        self.emplacement = emplacement
        self.nom = nom_foret
        self.taille = taille_foret
        print("Découverte d'une Prairie", self)
        Prairie.prairies_decouvertes +=1

v1 = Village("b1", "Tarik", 500)
#print ("nom de v1 -> {}".format(v1.nom))
#print ("Nombre d'habitant de {} -> {} habitants".format(v1.nom, v1.taille))

f1 = Foret("a1", "Forêt de Hautefeuille", 500)
#print ("nom de v1 -> {}".format(f1.nom))
#print ("Nombre de km² de la {} -> {} km²".format(f1.nom, f1.taille))

pr1 = Prairie("b2", "Prairie de L'aude", 100)
#print ("nom de v1 -> {}".format(pr1.nom))
#print ("Nombre de km² de la {} -> {} km²".format(pr1.nom, pr1.taille))

#print("Village découvert : {}".format(Village.villages_decouverts))
#print("Foret découverte : {}".format(Foret.forets_decouvertes))
#print("Prairie découverte : {}".format(Prairie.prairies_decouvertes))
