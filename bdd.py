import mysql.connector as mysqlpyth

class MySQL:
    def __init__(self, nom_table, db):
        self.tables = nom_table
        self.db = mysqlpyth.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'root',
            port = 8081,
            db = self.tables
        )
        print("Connexion réussi !")

    def deconnexion(self):
        self.db.close
        print('Connexion terminé !')


    def recuperer(self):
        cursor = self.db.cursor(buffered=True)
        query ='SELECT id_apprenant, prenom_apprenant, nom_apprenant FROM apprenants'
        cursor.execute(query)
        
        liste = []
        for ident, prenom, nom in cursor :
            apprenant = [ident, prenom, nom]
            liste.append(apprenant)
        return liste

    def crea_colonne(self):
        cursor = self.db.cursor(buffered=True)
        query = 'ALTER TABLE apprenants ADD COLUMN mail_apprenant VARCHAR(150) NOT NULL'
        cursor.execute(query)

    def inserer(self, liste):
        cursor = self.db.cursor(buffered=True)
        for elem in liste :
            query = f"UPDATE apprenants SET mail_apprenant='{elem[3]}' WHERE id_apprenant={str(elem[0])};"     
            cursor.execute(query)
            self.db.commit()
        return 'Elements insérés !'

