from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.__disponible= True
        if titre == "":
            raise ValueError("Format incorrect")
        
        if auteur == "":
            raise ValueError("Format incorrect")
        
    def est_disponible(self):
        return self.__disponible

    def changer_disponibilite(self, valeur):
        self.__disponible = valeur

    @abstractmethod
    def emprunter(self):
        pass

    @abstractmethod
    def retourner(self):
        pass

class Livre(Document):
    def emprunter(self):
        if not self.est_disponible():
            raise ValueError("Document déjà emprunté")

        self.changer_disponibilite(False)

    def retourner(self):
        if self.est_disponible():
            raise ValueError("Document déjà disponible")
        self.changer_disponibilite(True)

class Magazine(Document):
    def emprunter(self):
        if not self.est_disponible():
            raise ValueError("Document déjà emprunté")

        self.changer_disponibilite(False)

    def retourner(self):
        if self.est_disponible():
            raise ValueError("Document déjà disponible")

        self.changer_disponibilite(True)

class Adherant:
    def __init__(self, nom):
        self.nom = nom
        self.liste_emprunt = []

    def listes_emprunt(self):
        if not self.liste_emprunt:
            print("La liste des emprunts est vide")
        else:
            for element in self.liste_emprunt:
                print(f"Nom : {element["membre"]} | Livre : {element["titre"]} ")



class Bibliothecaire:
    def __init__(self):
        self.liste_livre = []
        self.liste_membre = []

    def ajouter_livre(self, Livre):
        self.liste_livre.append(Livre)
        print("*" * 10)
        print("Livre ajouté avec succès")

    def trouver_livre(self, titre):
        for livre in self.liste_livre:
            if livre.titre == titre:
                return livre
        raise ValueError("Livre introuvable")


    def inscrire_membre(self, Adherant):
        self.liste_membre.append(Adherant)
        print("*" * 10)
        print("Membre inscrit avec succès")
    
    def trouver_membre(self, nom):
        if not nom.isalpha():
            raise ValueError("Format incorrect")
        for membre in self.liste_membre:
            if membre.nom == nom:
                return membre
        raise ValueError("Membre introuvable")
        
    
    def valider_pret(self, nom_membre, titre_livre):
        if titre_livre == "":
            raise ValueError("Format incorrect")
        
        if nom_membre == "":
            raise ValueError("Format incorrect")
        
        livre = self.trouver_livre(titre_livre)
        membre = self.trouver_membre(nom_membre)
        livre.emprunter()
        dic = {
            "titre" : livre.titre,
            "membre" : membre.nom,
        }
        membre.liste_emprunt.append(dic)
        print(f"Le livre {dic['titre']} a été prếté à {dic["membre"]} avec succès")

    def retourner_livre(self, titre):
        livre = self.trouver_livre(titre)
        livre.retourner()
        print("Document retourné")


class Menu:
    def __init__(self):
        self.bibliothécaire = Bibliothecaire()

    def lancer(self):
        while True:
            print("=================================")
            print("GESTION BIBLIOTHÈQUE")
            print("=================================")
            print("1. Ajouter un Document")
            print("2. Inscrire un membre")
            print("3. Trouver un document")
            print("4. Trouver un adhérent")
            print("5. Valider un prêt")
            print("6. Lister les emprunts")
            print("7. Retourner un livre")
            print("8. Quitter")
            print("-----------------------------------")

            choix = input("Choisis un numéro : ")
            print("*" * 10)
            try:
                match choix:
                    case "1":
                        titre = input("Titre : ").strip()
                        auteur = input("Auteur : ").strip()
                        livre = Livre(titre, auteur)
                        self.bibliothécaire.ajouter_livre(livre)
                    case "2":
                        nom = input("Nom : ").strip()
                        membre = Adherant(nom)
                        self.bibliothécaire.inscrire_membre(membre)
                    case "3":
                        titre = input("Titre : ").strip()
                        print("*" * 10)
                        livree = self.bibliothécaire.trouver_livre(titre)
                        print(f"Livre : {livree.titre}")

                    case "4":
                        nom = input("Nom : ").strip()
                        membree = self.bibliothécaire.trouver_membre(nom)
                        print("*" * 10)
                        print(f"Membre : {membree.nom}")
                    case "5":
                        nom_membre = input("Nom membre : ").strip()
                        titre_livre = input("Titre livre : ").strip()
                        self.bibliothécaire.valider_pret(nom_membre, titre_livre)
                    case "6":
                        nom = input("Nom : ").strip()
                        membre = self.bibliothécaire.trouver_membre(nom)
                        membre.listes_emprunt()
                    case "7":
                        titrelivre = input("Titre livre : ").strip()
                        self.bibliothécaire.retourner_livre(titrelivre)
                    case _:
                        exit()
            except Exception as e:
                print(f"Erreur : {e}")

menu = Menu()
menu.lancer()



                



    


    
       

        