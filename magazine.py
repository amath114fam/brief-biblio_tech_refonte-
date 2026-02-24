from document import Document


class Magazine(Document):
    def emprunter(self):
        if not self.est_disponible():
            raise ValueError("Document déjà emprunté")

        self.changer_disponibilite(False)

    def retourner(self):
        if self.est_disponible():
            raise ValueError("Document déjà disponible")

        self.changer_disponibilite(True)