from abc import ABC, abstractmethod
class Document(ABC):
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.__disponible= True
        if titre == "":
            raise ValueError("Le titre ne peut pas être vide")
        
        if auteur == "":
            raise ValueError("L'auteur ne peut pas être vide")
        
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