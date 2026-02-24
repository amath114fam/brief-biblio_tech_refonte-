

class Adherant:
    def __init__(self, nom):
        self.nom = nom
        self.liste_emprunt = []

    def listes_emprunt(self):
        if not self.liste_emprunt:
            print("La liste des emprunts est vide")
        else:
            for element in self.liste_emprunt:
                print(f"Nom : {element["membre"]} | Document : {element["titre"]} | {element["types"]}")
