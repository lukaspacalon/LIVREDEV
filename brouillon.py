# Bienvenue dans le Livre programmé dont vous êtes le Héro Développeur
# coding:utf-8
# https://trello.com/b/4L1gpwt1/chroniques
# Procédural

import inspect
import joueur

class Objet:
    def __init__(self, nom, valeur, quantite=1):
        self.nom = nom
        self.brut = nom.strip().lower()
        self.quantite = quantite

        self.valeur = valeur
        self.valeurTotal = quantite * valeur

    def recalc(self):
        self.valeurTotal = self.quantite * self.valeur

    def examiner():
        print("{}, {} deniers".format(self.nom, self.valeur))

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
    def __init__(self, nom, valeur, tissu, quantite=1):
        self.nom = nom
        self.valeur = valeur
        self.tissu = tissu
        self.brut = nom.strip().lower()
        self.quantite = quantite

    def porter(self, nom):
        print("Vous portez : {}".format(self.nom))

class Nourriture(Objet):
    def __init__(self, nom, valeur, calorie, quantite=1):
        self.nom = nom
        self.valeur = valeur
        self.calorie = calorie
        self.brut = nom.strip().lower()
        self.quantite = quantite

    def examiner():
        print("{}",format(self.calorie))

    def manger(self):
        print("vous mangez : {}".format(self.nom))
        sac_joueur.retirer(self)


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

    def Lire(livre):
        print(livre)

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







sac_joueur = Contenant("sac joueur")

o1_denier = Objet("Deniers", 1, 50)
o2_choppe_de_bois = Objet("Choppe de bois", 10)
d1_bandage = Divers_utilisable("Bandage", 5)

h1_habit_de_lin = Habit("Habit de lin", 40, "lin")
h2_chaussure_de_cuir = Habit("Chaussure de cuir", 80, "cuir")
l1_carte_tarik = Livre("Carte du village de Tarik", 5, 6, 160, "village et les alentours")
n1_bout_de_pain = Nourriture("Bout de pain", 2, 265)
n2_pomme = Nourriture("Pomme", 0.5, 52)
n3_poire = Nourriture("Poire", 0.5, 52)


sac_joueur.ajouter(d1_bandage)
sac_joueur.ajouter(o2_choppe_de_bois)
sac_joueur.ajouter(o1_denier)
sac_joueur.ajouter(o1_denier)
sac_joueur.ajouter(h1_habit_de_lin)
sac_joueur.ajouter(h2_chaussure_de_cuir)
sac_joueur.ajouter(l1_carte_tarik)
sac_joueur.ajouter(n1_bout_de_pain)
sac_joueur.ajouter(n2_pomme)
sac_joueur.ajouter(n2_pomme)


inventaire_initial = [h1_habit_de_lin.__dict__, h2_chaussure_de_cuir.__dict__, l1_carte_tarik.__dict__, n1_bout_de_pain.__dict__, n2_pomme.__dict__]



print("\n")
print("###################inventaire_initial")
for i, k in enumerate(inventaire_initial):
    print(i, k)

print("\n")
print("###################inspect_sac_joueur")
#print(sac_joueur.inside)
for i, k in enumerate(inspect.getmembers(sac_joueur, predicate=inspect.ismethod)):
    print(i, k)
#print(inspect.getmembers(sac_joueur, predicate=inspect.ismethod))

print("\n")
print("###################sac_joueur.inside")
#print(sac_joueur.inside[o1_denier])
for i, k in enumerate(sac_joueur.inside):
    print(i, k)

print("\n")
print("###################sac_joueur.__getitem__(n2_pomme).__dict__")
print(sac_joueur.__getitem__(n2_pomme).__dict__)
#for i, k in enumerate(sac_joueur.inside):
#    print(i[0])

print("\n")
print("###################enumerate(sac_joueur.__getitem__(n2_pomme).__dict__):")
#print(sac_joueur.inside[o1_denier])
for i, k in enumerate(sac_joueur.__getitem__(n2_pomme).__dict__):
    print(i, k)
#print(sac_joueur.__dict__)

print("\n")
print("###################sac_joueur.__contains__(n2_pomme)")
#print(sac_joueur.inside[o1_denier])
print(sac_joueur.__contains__(n2_pomme))

print("\n")
print("###################sac_joueur.__contains__(n3_poire)")
#print(sac_joueur.inside[o1_denier])
print(sac_joueur.__contains__(n3_poire))

print("\n")
print("###################sac_joueur.__len__(n2_pomme)")
#print(sac_joueur.inside[o1_denier])
print(sac_joueur.__len__(n2_pomme))


#print("\n")
#print("###################sac_joueur.__setitem__(n2_pomme, 5)")
#print(sac_joueur.inside[o1_denier])
#"print(sac_joueur.__setitem__(n2_pomme, 5))

print("\n")
print("###################sac_joueur.__getitem__(n2_pomme).__dict__")
print(sac_joueur.__getitem__(n2_pomme).__dict__)
#for i, k in enumerate(sac_joueur.inside):
#    print(i[0])

print("\n")
print("###################inspectOBJET_d1_bandage")
#print(sac_joueur.inside)
for i, k in enumerate(inspect.getmembers(d1_bandage, predicate=inspect.ismethod)):
    print(i, k)
#print(inspect.getmembers(sac_joueur, predicate=inspect.ismethod))

print("\n")
print("###################inspectNOURRITURE_n2_pomme")
#print(sac_joueur.inside)
for i, k in enumerate(inspect.getmembers(n2_pomme, predicate=inspect.ismethod)):
    print(i, k)
#print(inspect.getmembers(sac_joueur, predicate=inspect.ismethod))

print("\n")
print("###################inspectLIVRE_l1_carte_tarik")
#print(sac_joueur.inside)
for i, k in enumerate(inspect.getmembers(l1_carte_tarik, predicate=inspect.ismethod)):
    print(i, k)
#print(inspect.getmembers(sac_joueur, predicate=inspect.ismethod))

print("\n")
print("###################inspectHABIT_h1_habit_de_lin")
#print(sac_joueur.inside)
for i, k in enumerate(inspect.getmembers(h1_habit_de_lin, predicate=inspect.ismethod)):
    print(i, k)

print("\n")
print("###################inspectDIVERSUTILISABLE_d1_bandage")
#print(sac_joueur.inside)
for i, k in enumerate(inspect.getmembers(d1_bandage, predicate=inspect.ismethod)):
    print(i, k)
#print(inspect.getmembers(sac_joueur, predicate=inspect.ismethod))


print("\n")
print("###################sac_joueur.inside")
#print(sac_joueur.inside[o1_denier])
print(sac_joueur[o1_denier].__dict__)

print("###################sac_joueur.inside.keys()")
print(sac_joueur.inside.keys())
for key in sac_joueur.inside.keys():
    print(key)


print("\n")
print("###################sac_joueur.inside.items()")
for i, k in enumerate(sac_joueur.inside.items()):
    print(i, k)

print("\n")
print("###################sac_joueur.inside.items()")
for i, (k, v) in enumerate(sac_joueur.inside.items()):
    print("index: {}, key: {}, value: {}".format(i, k, v))
print(enumerate(sac_joueur.inside.items()))


print("\n")
print("###################sac_joueur.inside.items()")
for index, item in enumerate(sac_joueur.inside.items(), start=0):   # Python indexes start at zero
    print(index, item)
print('there were {0} items printed'.format(index))

print("\n")
print("###################TABLEAU")
print(sac_joueur.inside)
print("###################TABLEAU")
for i, k in enumerate(sac_joueur.inside.items()):
    liste1 = [k]
    print(liste1[0])
print("###################FIN")
print("\n")

# Python3 code to demonstrate
# to get index and value
# using naive method

# initializing list
test_list = [1, 4, 5, 6, 7]
# Printing list
print ("Original list is : " + str(test_list))
# using naive method to
# get index and value
print ("List index-value are : ")
for i in range(len(test_list)):
    print (i, end = " ")
    print (test_list[i])
print (test_list[0])

print("###################SUITE")
numbers = {'first':0, 'second':1, 'third':3}
print(tuple(numbers.items())[1][0])

print("\n")
print("###################RECUP_PAR_INDICE_DOUBLE")
indice_exam = input("> ")
indice_exam = int(indice_exam)
print(tuple(sac_joueur.inside.items())[indice_exam][1])
print("\n")
print(tuple(sac_joueur.inside.items())[indice_exam][1].__dict__)
print("\n")
#print(tuple(sac_joueur.inside.items())[indice_exam][1].__dict__[valeur])
print("###################RECUP_PAR_INDICE_SIMPLE")
print(tuple(sac_joueur.inside.items())[indice_exam])
print("\n")
print("###################_____>>>>> AFFICHER")
print(tuple(sac_joueur.inside.items())[indice_exam][1].__dict__)
print("\n")
for i, k in enumerate(inspect.getmembers(tuple(sac_joueur.inside.items())[indice_exam][1], predicate=inspect.ismethod)):
    print(i, k)

print("\n")
print("###################_____>>>>> OBJET A SELECTIONNER")
print(tuple(sac_joueur.inside.items())[indice_exam][1])
print(n3_poire)


inventaire_ouvert = True
while inventaire_ouvert:
    print("\n")
    print("###################")
    for i, k in enumerate(sac_joueur.inside):
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
            print(tuple(sac_joueur.inside.items())[indice_inventaire][1].__dict__)
            print("\n")
            for i, k in enumerate(inspect.getmembers(tuple(sac_joueur.inside.items())[indice_inventaire][1], predicate=inspect.ismethod)):
                print(i, k)
            objet_examen = True
            while objet_examen:
                action_objet = input("" + tuple(sac_joueur.inside.items())[indice_inventaire][0] + " >")
                if action_objet == "manger":
                    #print("vous mangez : " + tuple(sac_joueur.inside.items())[indice_inventaire][0])
                    indice_nourriture = tuple(sac_joueur.inside.items())[indice_inventaire][1]
                    Nourriture.manger(indice_nourriture)
                else:
                    objet_examen = False
            #print(joueur.mon_joueur.inventaire_joueur[indice_inventaire])
            #objet.Habit.porter(objet.h1_habit_de_lin, joueur.mon_joueur.nom)
            #print(getattr(objet.h1_habit_de_lin, "nom"))
            #inspect.getmembers(objet.Habit, predicate=inspect.ismethod)
        except IndexError:
            print("Vous n'avez pas plus d'objet à examiner")
        if indice_inventaire in ['carte', 'map']:
            print(bibliotheque.carte_tarik["plan"]["plan"])
    except ValueError:
        inventaire_ouvert = False





#print("\n")
#print("###################")
#print(sac_joueur[denier].__dict__)
#print(sac_joueur[choppe_de_bois].__dict__)
#print(sac_joueur[bandage].__dict__)

#print("\n")
#print("###################")
#acheter(choppe_de_bois)
#print(sac_joueur[denier].__dict__)
#print(sac_joueur[choppe_de_bois].__dict__)
#print(sac_joueur[bandage].__dict__)

#print("\n")
#print("###################")
#vendre(choppe_de_bois)
#print(sac_joueur[denier].__dict__)
#print(sac_joueur[choppe_de_bois].__dict__)
#print(sac_joueur[bandage].__dict__)



#print("\n")
#print("###################")
#for i, k in sac_joueur.__dict__.items():
#    print(i, k)


#print("\n")
#print("###################")
#sac_joueur.__iter__()
#for i, k in sac_joueur.inside.items():
#    print(i, k)


#print("\n")
#print("###################")
#print(sac_joueur[denier])
#print(sac_joueur[denier].__dict__)

#for i, k in sac_joueur.__dict__.items():
#    print(i, k)

#for liste_inventaire in sac_joueur.__dict__:
#    print(liste_inventaire)

'''
h1 = Habit("Habit de lin", 40, "lin")
h2 = Habit("Chaussure en daim", 80, "daim")
l1 = Livre("Carte du village de Tarik", 160, "village et les alentours")
n1 = Nourriture("Bout de pain", 2, 265)
n2 = Nourriture("Pomme", 0.5, 52)
'''
