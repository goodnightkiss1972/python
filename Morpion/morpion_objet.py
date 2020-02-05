import random as rd

""" question1)
créer une classe morpion() et sa fonction init qui définit l'état initial du plateau de jeu.
On notera le plateau par une liste, emplie initialement de zéros 3*3. La classe doit prendre
en argument le nom du joueur qui commence ("humain" ou "ordinateur").
"""

class morpion:
    """Classe définissant l'état initial du plateau de jeu par :
    -   le type de plateau, ici 3*3
    -   le nom de l'utilisateur
    """
    def __init__(self, premierJoueur):
        self.plateau = [[0,0,0],[0,0,0],[0,0,0]]
        if premierJoueur != "humain" and premierJoueur != "ordinateur":
            print("Erreur: impossible de créer le morpion, le joueur qui commence doit etre ""humain"" ou ""ordinateur"".")
            return
        self.premierJoueur = premierJoueur
        if premierJoueur == "humain":
            self.secondJoueur = "ordinateur"
        if premierJoueur == "ordinateur":
            self.secondJoueur = "humain"
       
    """ question2)
    écrire une fonction afficher_plateau() qui permet d'afficher le plateau ligne par ligne avec des 
    croix à la place des -1, des ronds à la place des 1, et rien à la place des 0.
    """
    def afficher_plateau(self):
        print() 
        for i in range(3):
            ligne = []
            for j in range(3):
                if self.plateau[i][j]==1:
                    ligne.append("o")
                elif self.plateau[i][j]==-1:
                    ligne.append("x")
                elif self.plateau[i][j]==0:
                    ligne.append(" ")
            print(ligne)
        print()

    """ question3)
    écrire une fonction joueur_humain() qui vous permet via input() de dire où vous voulez jouer
    en numéro de ligne et de colonne. Cette fonction doit gérer le fait que vous n'avez le droit de 
    jouer que dans une case vide.
    """
    def joueur_humain(self):
        # choix de la ligne et vérification de son existence
        print("choisissez la ligne   (0, 1 ou 2) : ")
        ligne=int(input())
        if ligne>2 or ligne<0:
            print("les lignes existantes sont entre 0 et 2")
            self.joueur_humain()
        # choix de la colonne et vérification de son existence
        print("choisissez la colonne (0, 1 ou 2) : ")
        colonne=int(input())
        if colonne>2 or colonne<0:
            print("les colonnes existantes sont entre 0 et 2.")
            self.joueur_humain()
        #vérification case vide
        if self.plateau[ligne][colonne] != 0:
            print("il faut jouer dans une case vide !")
            self.afficher_plateau()
            self.joueur_humain()
        #la case se remplit
        else:
            self.plateau[ligne][colonne]=1
            self.afficher_plateau()


    """question4)
    écrire une fonction trouver_cases_vides() qui renvoie une liste des indices (lignes, colonnes)
    des cases vides.
    """
    def trouver_cases_vides(self):
        liste_indice_cases_vides=[]
        for i in range(3):
            for j in range(3):
                if self.plateau[i][j]==0:
                    liste_indice_cases_vides.append((i,j))
        return(liste_indice_cases_vides)

    """question5)
    écrire une fonction joueur_aleatoire() qui joue aléatoirement dans une des cases vides.
    """
    def joueur_aleatoire(self):
        L=self.trouver_cases_vides()
        (i,j)=rd.choice(L)
        self.plateau[i][j]=-1
        self.afficher_plateau()

    """question6)
    ecrire une fonction partie_gagnee() qui renvoie le joueur gagnant : None, "humain", 
    ou "ordinateur", en fonction des règles du jeu du morpion.
    """
    def partie_gagnee(self):
        resultat = 0
        if self.plateau[0][0]==1 and self.plateau[0][1]==1 and self.plateau[0][2]==1:
            resultat=1
        if self.plateau[1][0]==1 and self.plateau[1][1]==1 and self.plateau[1][2]==1:
            resultat=1
        if self.plateau[2][0]==1 and self.plateau[2][1]==1 and self.plateau[2][2]==1:
            resultat=1
        if self.plateau[0][0]==1 and self.plateau[1][0]==1 and self.plateau[2][0]==1:
            resultat=1
        if self.plateau[0][1]==1 and self.plateau[1][1]==1 and self.plateau[2][1]==1:
            resultat=1
        if self.plateau[0][2]==1 and self.plateau[1][2]==1 and self.plateau[2][2]==1:
            resultat=1
        if self.plateau[0][0]==1 and self.plateau[1][1]==1 and self.plateau[2][2]==1:
            resultat=1
        if self.plateau[0][2]==1 and self.plateau[1][1]==1 and self.plateau[2][0]==1:
            resultat=1
        if self.plateau[0][0]==-1 and self.plateau[0][1]==-1 and self.plateau[0][2]==-1:
            resultat=2
        if self.plateau[1][0]==-1 and self.plateau[1][1]==-1 and self.plateau[1][2]==-1:
            resultat=2
        if self.plateau[2][0]==-1 and self.plateau[2][1]==-1 and self.plateau[2][2]==-1:
            resultat=2
        if self.plateau[0][0]==-1 and self.plateau[1][0]==-1 and self.plateau[2][0]==-1:
            resultat=2
        if self.plateau[0][1]==-1 and self.plateau[1][1]==-1 and self.plateau[2][1]==-1:
            resultat=2
        if self.plateau[0][2]==-1 and self.plateau[1][2]==-1 and self.plateau[2][2]==-1:
            resultat=2
        if self.plateau[0][0]==-1 and self.plateau[1][1]==-1 and self.plateau[2][2]==-1:
            resultat=2
        if self.plateau[0][2]==-1 and self.plateau[1][1]==-1 and self.plateau[2][0]==-1:
            resultat=2
        if resultat == 1:
            return("humain")
        if resultat == 2:
            return("ordinateur")
        else:
            return None


    """question8)
    mettre tout cela ensemble via une fonction jouer() qui permet effectivement de jouer contre l'ordinateur.
    Et battez-le : c'est très facile contre un joueur aléatoire.
    Idée : il faut une boucle while qui ne se termine que si partie gagnée ou nulle, et trouver d'alterner
    à qui c'est le tour de jouer.
    """

    def jouer(self):
        self.afficher_plateau()
        while self.partie_gagnee() != "humain" or self.partie_gagnee() != "ordinateur" or self.partie_gagnee() != None:
            for i in range(9):
                if (i%2==0):
                    print(self.premierJoueur)
                    if self.premierJoueur == "humain":
                        self.joueur_humain()
                    else:
                        self.joueur_aleatoire()
                if (i%2==1):
                    print(self.secondJoueur)
                    if self.secondJoueur == "humain":
                        self.joueur_humain()
                    else:
                        self.joueur_aleatoire()
                if self.partie_gagnee() == "humain" or self.partie_gagnee() == "ordinateur":
                    print(self.partie_gagnee())
                    print("fin de partie")
                    return
            break
        
test=morpion("humain")
test.jouer()

test2=morpion("ordinateur")
test2.jouer()
