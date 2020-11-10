class Apprenant:
    def __init__(self, liste_apprenants, liste_mails):
        self.liste_apprenants = liste_apprenants
        self.liste_mails = liste_mails

    def association(self):
        for mail in self.liste_mails:
            for apprenant in self.liste_apprenants:
                x = apprenant[2].lower().replace('-','').replace(' ','')
                y = mail.lower().replace('-','').replace(' ','')
                if x[:4] in y :
                    apprenant.append(mail)
                
        return self.liste_apprenants

