import lecture_fichier
import bdd
import apprenant

def main():
    #Instance class Fichier - Ouverture et lecture du fichier .txt :
    mails = lecture_fichier.Fichier('apprenantmail.txt')

    #Les mails sont enregistrés dans une liste :
    liste_mails = mails.recup()

    #Fermeture du fichier .txt :
    mails.fermeture()

    #Instance class MySQL - Connexion a la BDD:
    bd = bdd.MySQL('binomotron','db')

    #Recupère dans une liste les apprenants:
    liste_apprenants = bd.recuperer()

    #Créer une nouvelle colonne 'mail' dans la BDD:
    bd.crea_colonne()

    #Instance class Apprenant - affectation de deux listes:
    apprenants = apprenant.Apprenant(liste_apprenants, liste_mails)

    #Association des mails avec les apprenants :
    liste_mail_apprenant = apprenants.association()
    print(liste_mail_apprenant)

    #Insère les mails dans la BDD
    bd.inserer(liste_mail_apprenant)

    #Deconnexion de la BDD:
    bd.deconnexion()



main()