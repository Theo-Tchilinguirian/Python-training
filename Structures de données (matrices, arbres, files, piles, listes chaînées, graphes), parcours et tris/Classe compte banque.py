class Compte:
    def __init__(self, idNumber, nomPrenom, solde):
        self.numeroCompte = idNumber
        self.nom = nomPrenom
        self.solde = solde

    def verser(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if self.solde < -500 and self.solde - montant >= -500:
            print("Impossible d'effectuer l'opération. Solde insuffisante")
        else:
            self.solde -= montant

    def virerVers(self, montant, destination):
        if not self.solde < -500 and self.solde - montant >= -500:  # On ne peut virer de l'argent si on a moins de -500 euros ou si la solde - le montant n'est pas inférieur à -500
            self.solde -= montant
            destination.solde += montant

    def agiosCompte(self):
        if self.verifier():
            agios = self.solde*-1*0.04  # L'agios est le montant à retirer du compte (4% de la solde si elle est inférieur à -500)
            self.solde -= agios

    def verifier(self):
        return self.solde <= 0

    def afficherInfosCompte(self):
        if self.verifier():
            self.agiosCompte()
        print("Compte numéro:", self.numeroCompte,
              "\nNom et prénom:", self.nom,
              "\nSolde:", self.solde,
              "\nSauf erreur ou omission\n",
              10*"-")


bourvil = Compte(11, " bourvil Martin", 5000)
bourvil.verser(1500)
bourvil.retirer(7000)
bourvil.afficherInfosCompte()

cholet = Compte(12, "Cholet Claude", 6300)
cholet.virerVers(600, bourvil)
bourvil.afficherInfosCompte()

cholet.afficherInfosCompte()

cholet.retirer(6000)
cholet.afficherInfosCompte()

cholet.verser(1000)
cholet.afficherInfosCompte()