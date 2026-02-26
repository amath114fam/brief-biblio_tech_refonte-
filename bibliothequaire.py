from db import get_connexion


class Bibliothecaire:
    def ajout_adherant(self, adherant):
        connection = get_connexion()
        cursor = connection.cursor()
        query = "INSERT INTO adherant (nom) VALUES (%s)"
        cursor.execute(query, (adherant.nom,))
        connection.commit()
        cursor.close()
        connection.close()
        print(f"{adherant.nom} a été ajouté avec succès")

    def ajouter_document(self, document, type_doc):
        """Ajoute un livre OU un magazine — une seule méthode."""
        if type_doc not in ("livre", "magazine"):
            raise ValueError("type_doc doit être 'livre' ou 'magazine'")

        connection = get_connexion()
        cursor = connection.cursor()
        query = f"INSERT INTO {type_doc} (titre, auteur, disponible) VALUES (%s, %s, %s)"
        cursor.execute(query, (document.titre, document.auteur, True))
        connection.commit()
        cursor.close()
        connection.close()
        print(f"Le {document.titre} de {document.auteur} a été ajouté")

    

    def trouver_document(self, titre, type_doc):
        """
        Cherche un livre OU un magazine par titre.
        Retourne un dict {"titre": ..., "id": ..., "disponible": ...} ou None.
        """
        if type_doc.lower() not in ("livre", "magazine"):
            raise ValueError("type_doc doit être 'livre' ou 'magazine'")

        connection = get_connexion()
        cursor = connection.cursor()
        try:
            query = f"SELECT id, titre, auteur, disponible FROM {type_doc} WHERE LOWER(titre) = %s"
            cursor.execute(query, (titre.lower(),))
            row = cursor.fetchone()
            if row is None:
                print(f"Ce {type_doc} n'existe pas")
                return None
            id_doc, titre_doc, auteur, disponible = row
            print(f"Livre : {titre_doc}, Auteur : {auteur}")
            return {"id": id_doc, "titre": titre_doc, "auteur" :auteur, "disponible": disponible}
        except Exception as e:
            print(f"Erreur lors de la recherche : {e}")
            return None
        finally:
            cursor.close()
            connection.close()

    def trouver_membre(self, nom):
        """Retourne un dict {"id": ..., "nom": ...} ou None."""
        connection = get_connexion()
        cursor = connection.cursor()
        try:
            query = "SELECT id, nom FROM adherant WHERE LOWER(nom) = %s"
            cursor.execute(query, (nom.lower(),))
            row = cursor.fetchone()
            if row is None:
                print("Ce membre n'existe pas")
                return None
            id_membre, nom_membre = row
            return {"id": id_membre, "nom": nom_membre}
        except Exception as e:
            print(f"Erreur lors de la recherche : {e}")
            return None
        finally:
            cursor.close()
            connection.close()

    def emprunter_document(self, nom_membre, titre, type_doc):
        
        if not titre or not titre.strip():
            raise ValueError("Le titre ne peut pas être vide")
        if not nom_membre or not nom_membre.strip():
            raise ValueError("Le nom du membre ne peut pas être vide")
        if type_doc.lower() not in ("livre", "magazine"):
            raise ValueError("type_doc doit être 'livre' ou 'magazine'")

        #Récupérer le document et le membre
        document = self.trouver_document(titre, type_doc)
        membre   = self.trouver_membre(nom_membre)

        if document is None:
            raise ValueError(f"Le {type_doc} {titre} est introuvable")
        if membre is None:
            raise ValueError(f"Le membre {nom_membre} est introuvable")

        #Vérifier la disponibilité
        if not document["disponible"]:
            raise ValueError(f"Le {type_doc} {titre} est déjà emprunté")

        #Mettre à jour disponible → False + enregistrer l'emprunt
        connection = get_connexion()
        cursor = connection.cursor()

        cursor.execute(
            f"UPDATE {type_doc} SET disponible = %s WHERE id = %s",
            (False, document["id"])
        )
        cursor.execute(
                """INSERT INTO emprunt (document_id, type_document, adherant_id, titre, auteur) 
                VALUES (%s, %s, %s, %s, %s)""",
                (document["id"], type_doc, membre["id"], document["titre"], document["auteur"])
            )

        connection.commit()
        cursor.close()
        connection.close()

        print(f"{document['titre']} a été prêté à {membre['nom']} avec succès")


    def retourner_document(self, titre, type_doc):
       
        if not titre or not titre.strip():
            raise ValueError("Le titre ne peut pas être vide")
        if type_doc not in ("livre", "magazine"):
            raise ValueError("type_doc doit être 'livre' ou 'magazine'")

        document = self.trouver_document(titre, type_doc)
        if document is None:
            raise ValueError(f"Le {type_doc} {titre} est introuvable")

        if document["disponible"]:
            raise ValueError(f"Le {type_doc} {titre} est déjà disponible")

        connection = get_connexion()
        cursor = connection.cursor()

        cursor.execute(
            f"UPDATE {type_doc} SET disponible = %s WHERE id = %s",
            (True, document["id"])
        )
        connection.commit()
        cursor.close()
        connection.close()

        print(f"{document['titre']} a été retourné avec succès")

    def liste_emprunt(self):
        connection = get_connexion()
        cursor = connection.cursor()
    
        query = """
            SELECT
                a.nom,
                e.titre,
                e.auteur,
                e.type_document
            FROM emprunt e
            JOIN adherant a ON e.adherant_id = a.id
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        for nom, titre, auteur, type_doc in rows:
            print(f"Nom : {nom} | Type de document : {type_doc} | Titre : {titre} | Auteur : {auteur}")

        cursor.close()
        connection.close()
    def liste_membre(self):
        connection = get_connexion()
        cursor = connection.cursor()
        query = """
            select * from adherant
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(f"{row[0]}. {row[1]}")

    def emprunt_membre(self, id_adherant):
        connection = get_connexion()
        cursor = connection.cursor()
        query = """
            SELECT 
                a.nom,
                e.titre,
                e.auteur,
                e.type_document
            FROM emprunt e
            JOIN adherant a ON e.adherant_id = a.id
            WHERE e.adherant_id = %s
        """
        cursor.execute(query, (id_adherant, ))
        rows = cursor.fetchall()
        for row in rows:
            print(f"Nom : {row[0]} - Titre : {row[1]} - Auteur : {row[2]} - Type : {row[3]}")
