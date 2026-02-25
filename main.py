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
            print("1. Ajouter un document")
            print("2. Ajouter un adherant")
            print("3. Trouver un document")
            print("4. Trouver un adhérent")
            print("5. Emprunter un document")
            print("6. Retourner un document")
            print("7. Listes emprunts")
            print("0. Quitter")
            print("-----------------------------------")

            choix = input("Choisis un numéro : ")
            print("*" * 10)
            try:
                match choix:
                    case "1":
                        titre = input("Titre : ").strip()
                        auteur = input("Auteur : ").strip()
                        type_l = input("Type : ").strip()
                        livre = Livre(titre, auteur)
                        self.bibliothécaire.ajouter_document(livre, type_l)
                    case "2":
                        nom = input("Nom : ")
                        membr = Adherant(nom)
                        self.bibliothécaire.ajout_adherant(membr)
                    case "3":
                        titre = input("Titre : ").strip()
                        type_doc = input("Type : ").strip()
                        print("*" * 10)
                        self.bibliothécaire.trouver_document(titre, type_doc)
                        # print(f"Livre : {livree.titre}")
                    case "4":
                        nom = input("Nom : ").strip()
                        self.bibliothécaire.trouver_membre(nom)
                    case "5":
                        nom_membre = input("Nom membre : ").strip()
                        titre = input("Titre : ").strip()
                        type_document = input("Type : ").strip()
                        self.bibliothécaire.emprunter_document(nom_membre, titre, type_document)

                    case "6":
                        titre = input("Titre : ").strip()
                        type_d = input("Type_d : ").strip()
                        self.bibliothécaire.retourner_document(titre, type_d)
                        print("*" * 10)
                        # print(f"Membre : {membree.nom}")
                    case "7":
                        self.bibliothécaire.liste_emprunt()
                    case _:
                        exit()
            except Exception as e:
                print(f"Erreur : {e}")

menu = Menu()
menu.lancer()



                



    


    
       

        