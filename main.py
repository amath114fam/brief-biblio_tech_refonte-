from bibliothequaire import Bibliothecaire
from livre import Livre
from magazine import Magazine
from adherant import Adherant

class Menu:
    def __init__(self):
        self.bibliothécaire = Bibliothecaire()

    def lancer(self):
        while True:
            print("=================================")
            print("GESTION BIBLIOTHÈQUE")
            print("=================================")
            print("1. Ajouter un Livre")
            print("2. Ajouter un magazine")
            print("3. Inscrire un membre")
            print("4. Trouver un document")
            print("5. Trouver un adhérent")
            print("6. Valider un prêt")
            print("7. Lister les emprunts")
            print("8. Retourner un livre")
            print("9. liste des livres")
            print("10. liste des magazines")
            print("11. Quitter")
            print("-----------------------------------")

            choix = input("Choisis un numéro : ")
            print("*" * 10)
            try:
                match choix:
                    case "1":
                        titre = input("Titre : ").strip()
                        auteur = input("Auteur : ").strip()
                        type_l = input("Type : ").strip()
                        livre = Livre(titre, auteur, type_l)
                        self.bibliothécaire.ajouter_livre(livre)
                    case "2":
                        titre = input("Titre : ").strip()
                        auteur = input("Auteur : ").strip()
                        type_m = input("Type : ").strip()
                        magazine = Magazine(titre, auteur, type_m)
                        self.bibliothécaire.ajouter_magazine(magazine)
                    case "3":
                        nom = input("Nom : ").strip()
                        membre = Adherant(nom)
                        self.bibliothécaire.inscrire_membre(membre)
                    case "4":
                        titre = input("Titre : ").strip()
                        print("*" * 10)
                        livree = self.bibliothécaire.trouver_livre(titre)
                        print(f"Livre : {livree.titre}")

                    case "5":
                        nom = input("Nom : ").strip()
                        membree = self.bibliothécaire.trouver_membre(nom)
                        print("*" * 10)
                        print(f"Membre : {membree.nom}")
                    case "6":
                        nom_membre = input("Nom membre : ").strip()
                        titre_livre = input("Titre livre : ").strip()
                        self.bibliothécaire.valider_pret(nom_membre, titre_livre)
                    case "7":
                        nom = input("Nom : ").strip()
                        membre = self.bibliothécaire.trouver_membre(nom)
                        membre.listes_emprunt()
                    case "8":
                        titrelivre = input("Titre livre : ").strip()
                        self.bibliothécaire.retourner_livre(titrelivre)
                    case "9":
                        self.bibliothécaire.listes_livres()
                    case "10":
                        self.bibliothécaire.listes_magazines()
                    case _:
                        exit()
            except Exception as e:
                print(f"Erreur : {e}")

menu = Menu()
menu.lancer()



                



    


    
       

        