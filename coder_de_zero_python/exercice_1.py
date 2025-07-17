# Creer une classe GestionCptB qui se definit par :
# Un nombre de compte : nCompte
# Un nom de client : nomClient 
# Un solde compte : soldeCompte
# Un constructeur ayant comme parametres : nCompte, nomClient, soldeCompte
# Une methode Versement
# Une methode Retrait
# Une methode affichage info
# SOURCE : https://www.youtube.com/watch?v=YnlaDFJwwKI

class CompteBancaire:
    def __init__(self, numero_compte: str, nom_client: str, solde: float):
        self.numero_compte = numero_compte
        self.nom_client = nom_client
        self.solde = solde
    
    def versement(self, depot: float):
        self.solde += depot
        print(f"Versement de {depot} EUROS effectue.")
        print(f"Le solde du compte {self.numero_compte} est de {self.solde} EUROS.\n")

    def retrait(self, montant: float):
        self.solde -= montant
        print(f"Vous avez retire {montant} EUROS.")
        print(f"Votre solde est de {self.solde} EUROS.\n")

    def consulter_compte(self):
        print(f"Le solde de {self.nom_client} est de {self.solde} euros.\nLe numero de client associe est : {self.numero_compte}\n")

compte_bancaire_clement = CompteBancaire("1111 2222 3333 4444", "GRUET", 100.0)

compte_bancaire_clement.versement(50.50)
compte_bancaire_clement.retrait(50.50)
compte_bancaire_clement.consulter_compte()