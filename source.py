# Bienvenue dans le Livre programmé dont vous êtes le Héro Développeur
# coding:utf-8
# https://trello.com/b/4L1gpwt1/chroniques
# Procédural


class LivreSource:
    contenu_page = "Il était une fois votre histoire. "

    def __init__(self, c_chapitre, c_page, c_contenu):
        print("")
        self.chapitre = c_chapitre
        self.page = c_page
        self.contenu = c_contenu

    def ecrire(cls, nouveau_paragraphe):
        LivreSource.contenu_page = LivreSource.contenu_page + nouveau_paragraphe
        print(LivreSource.contenu_page)

    ecrire = classmethod(ecrire)

print("Lancement du Programme")
