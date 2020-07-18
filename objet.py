# Bienvenue dans le Livre programmé dont vous êtes le Héro Développeur
# coding:utf-8
# https://trello.com/b/4L1gpwt1/chroniques
# Procédural

import inspect
import joueur
import bibliotheque
import time, sched

class Objet:
    def __init__(self, nom, valeur, quantite=1):
        self.nom = nom
        self.brut = nom.strip().lower()
        self.quantite = quantite

        self.valeur = valeur
        self.valeurTotal = quantite * valeur

    def recalc(self):
        self.valeurTotal = self.quantite * self.valeur

    def examiner(self):
        print(self.__dict__)

    def jeter(self):
        print("vous jetez : {}".format(self.nom))
        sac_joueur.retirer(self)

class Contenant:
    def __init__(self, nom):
        self.nom = nom
        self.inside = {}

    def __iter__(self):
        return iter(self.inside.objets())

    def __len__(self, objet):
        return len(self.inside)

    def __contains__(self, objet):
        return objet.brut in self.inside

    def __getitem__(self, objet):
        return self.inside[objet.brut]

    def __setitem__(self, objet, valeur):
        self.inside[objet.brut] = valeur
        return self[objet]

    def ajouter(self, objet, quantite=1):
        if quantite < 0:
            raise ValueError("Quantite negative, utilisez retirer() plutot")

        if objet in self:
            self[objet].quantite += quantite
            self[objet].recalc()
        else:
            self[objet] = objet

    def retirer(self, objet, quantite=1):
        if objet not in self:
            raise KeyError("L'objet n'est pas dans le contenant")
        if quantite < 0:
            raise ValueError("Quantite negative, utilisez ajouter() plutot")

        if self[objet].quantite <= quantite:
            del self.inside[objet.brut]
        else:
            self[objet].quantite -= quantite
            self[objet].recalc()

def acheter(*objets):
    for objet in objets:
        if objet.valeur > sac_joueur[denier].quantite:
            print("Vous n'avez pas assez d'argent !")
            print("Revenez quand vous aurez {0} plus de deniers").format(objet.valeur - sac_joueur[denier].quantite)
        else:
            sac_joueur.retirer(denier, objet.valeur)
            sac_joueur.ajouter(objet)
            print("Vous avez acheté : '{0}'".format(objet.nom))

def vendre(*objets):
    for objet in objets:
        sac_joueur.ajouter(denier, objet.valeur)
        sac_joueur.retirer(objet)
        print("Vous avez vendu : '{0}'".format(objet.nom))


class Habit(Objet):
    def __init__(self, nom, valeur, tissu, emplacement, port, quantite=1):
        self.nom = nom
        self.valeur = valeur
        self.tissu = tissu
        self.brut = nom.strip().lower()
        self.quantite = quantite
        self.emplacement = emplacement
        self.port = port

    def porter(self):
        print("Vous portez : {}".format(self.nom))
        self.port = True

    def enlever(self):
        print("Vous enlevez : {}".format(self.nom))
        self.port = False

class Nourriture(Objet):
    def __init__(self, nom, valeur, calorie, effet, quantite=1):
        self.nom = nom
        self.valeur = valeur
        self.calorie = calorie
        self.brut = nom.strip().lower()
        self.quantite = quantite
        self.effet = effet

    def manger(self):
        print("vous mangez : {}".format(self.nom))
        joueur.mon_joueur.faim = joueur.mon_joueur.faim + self.calorie/20
        sac_joueur.retirer(self)

class Boisson(Objet):
    def __init__(self, nom, valeur, effet, centilitres, contenu, quantite=1):
        self.nom = nom
        self.valeur = valeur
        self.brut = nom.strip().lower()
        self.quantite = quantite
        self.effet = effet
        self.centilitres = centilitres
        self.contenu = contenu

    def examiner(self, centilitres):
        print(self.__dict__)
        print(self.centilitres + " centilitres")

    def boire(self):
        if self.centilitres > 0:
            print("vous buvez 10 centilitres de : {}".format(self.nom))
            joueur.mon_joueur.soif = joueur.mon_joueur.soif + 10
            self.centilitres = self.centilitres - 10
        else:
            print("La boisson est vide !")


class Livre(Objet):

    def __init__(self, nom, valeur, c_chapitre, c_page, c_contenu, quantite=1):
        print("")
        self.nom = nom
        self.valeur = valeur
        self.chapitre = c_chapitre
        self.page = c_page
        self.contenu = c_contenu
        self.brut = nom.strip().lower()
        self.quantite = quantite

    def lire(self):
        print(self.__dict__["contenu"])

    def ecrire(cls, nouveau_paragraphe):
        Livre.contenu = Livre.contenu + nouveau_paragraphe

    ecrire = classmethod(ecrire)

class Divers_utilisable(Objet):
        def __init__(self, nom, valeur, quantite=1):
            self.nom = nom
            self.valeur = valeur
            self.brut = nom.strip().lower()
            self.quantite = quantite

        def utiliser():
            print("vous utilisez : {}".format(self.nom))
            sac_joueur.retirer(self)







sac_joueur = Contenant("sac joueur")

o1_denier = Objet("Deniers", 1, 50)
o2_choppe_de_bois = Objet("Choppe de bois", 10)
d1_bandage = Divers_utilisable("Bandage", 5)
h1_chemise_de_lin = Habit("Chemise de lin", 40, "lin", "torse", True)
h2_chaussure_de_cuir = Habit("Chaussure de cuir", 80, "cuir", "pieds", True)
h3_braies_de_lin = Habit("Braies de lin", 40, "lin", "bas", True)
h4_capuchon = Habit("Capuchon", 20, "chanvre", "tete", False)
l1_carte_tarik = Livre("Carte du village de Tarik", 5, 1, 1, bibliotheque.carte_tarik["plan"]["plan"])
n1_bout_de_pain = Nourriture("Bout de pain", 2, 265, "nourrie")
n2_pomme = Nourriture("Pomme", 0.5, 52, "nourrie")
n3_poire = Nourriture("Poire", 0.5, 52, "nourrie")
b1_gourde = Boisson("Gourde", 0.5, "hydrate", 50, "eau")


sac_joueur.ajouter(d1_bandage)
sac_joueur.ajouter(o2_choppe_de_bois)
sac_joueur.ajouter(o1_denier)
sac_joueur.ajouter(o1_denier)
sac_joueur.ajouter(h1_chemise_de_lin)
sac_joueur.ajouter(h2_chaussure_de_cuir)
sac_joueur.ajouter(h3_braies_de_lin)
sac_joueur.ajouter(l1_carte_tarik)
sac_joueur.ajouter(n1_bout_de_pain)
sac_joueur.ajouter(n2_pomme)
sac_joueur.ajouter(n2_pomme)
sac_joueur.ajouter(h4_capuchon)
sac_joueur.ajouter(b1_gourde)


inventaire_initial = [h1_chemise_de_lin.__dict__, h2_chaussure_de_cuir.__dict__, l1_carte_tarik.__dict__, n1_bout_de_pain.__dict__, n2_pomme.__dict__]


#begin = time.time()
#print("Début")
#time.sleep(5)
#end = time.time()
#print("Fin")
#print(f"Temps exécuté : {end - begin}s")
tps = time.localtime()
print(tps)
