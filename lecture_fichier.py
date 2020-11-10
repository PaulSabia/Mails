class Fichier:
    def __init__(self, nom_fichier):
        self.file = open(nom_fichier, 'r')
        print(f'{nom_fichier} ouvert en lecture')

    
    def recup(self):    
        liste = []
        lignes = self.file.readlines()
        for ligne in lignes:
            liste.append(ligne.rstrip())
        return liste

    def fermeture(self):
        self.file.close()
        print(f'Fichier fermé !')




