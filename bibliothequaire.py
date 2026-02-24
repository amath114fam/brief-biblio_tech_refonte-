


class Bibliothecaire:
    def __init__(self):
        self.liste_livre = []
        self.liste_membre = []

    def ajouter_livre(self, Livre):
        self.liste_livre.append(Livre)
        print("*" * 10)
        print("Livre ajouté avec succès")

    def ajouter_magazine(self, magazine):
        self.liste_livre.append(magazine)
        print("*" * 10)
        print("Magazine ajouté avec succès")

    def trouver_livre(self, titre):
        for livre in self.liste_livre:
            if livre.titre.lower() == titre.lower():
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
            if membre.nom.lower() == nom.lower():
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
            "types"  : livre.types
        }
        membre.liste_emprunt.append(dic)
        print(f"Le livre {dic['titre']} a été prếté à {dic["membre"]} avec succès")

    def retourner_livre(self, titre):
        livre = self.trouver_livre(titre)
        livre.retourner()
        print("Document retourné")

    def listes_livres(self):
        livres_trouves = False
        for doc in self.liste_livre:
            if doc.types.lower() == "livre":
                print(f"Livre : {doc.titre} | Auteur : {doc.auteur}")
                livres_trouves = True

        if not livres_trouves:
            print("Pas de livre disponible")
    
    def listes_magazines(self):
        livres_trouves = False
        for doc in self.liste_livre:
            if doc.types.lower() == "magazine":
                print(f"Magazine : {doc.titre} | Auteur : {doc.auteur}")
                livres_trouves = True
                
        if not livres_trouves:
            print("Pas de Magazine disponible")

