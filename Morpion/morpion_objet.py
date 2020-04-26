# Modification par Fabien le 08/02/2020
import random as rd

compteJoueur = 0 # va servir a affecter un numero derriere chaque joueur pour les differencier
def incremente_joueur():
    global compteJoueur # explique qu'on se referre à la variable globale, sinon on ne peut la modifier depuis une methode
    compteJoueur += 1

class joueur:
    def __init__(self, typeDeJoueur, jeton):
        if typeDeJoueur not in ["humain", "ordinateur"]:
            print ("Erreur: impossible de créer le joueur ni ""humain"" ni ""ordinateur"".")
            return
        else:
            incremente_joueur()
            self.typeDeJoueur = typeDeJoueur
            self.jeton = jeton
            self.nom = typeDeJoueur + str(compteJoueur)


""" question1)
créer une classe morpion() et sa fonction init qui définit l'état initial du plateau de jeu.
On notera le plateau par une liste, emplie initialement de zéros 3*3. La classe doit prendre
en argument le nom du joueur qui commence ("humain" ou "ordinateur").
"""
class morpion:
    """Classe définissant l'état initial du plateau de jeu par :
    -   le type de plateau, ici 3*3
    -   les joueurs
    """
    def __init__(self, premierJoueur, deuxiemeJoueur):
        self.initialiser_plateau()
        self.joueurs = [joueur(premierJoueur, 1), joueur(deuxiemeJoueur, -1)]

    def initialiser_plateau(self):
        self.plateau = [[0,0,0],[0,0,0],[0,0,0]]

    def afficher_plateau(self):
        """ question2)
        écrire une fonction afficher_plateau() qui permet d'afficher le plateau ligne par ligne avec des 
        jetons à la place des 1 et -1, et rien à la place des 0.
        """
        for i in range(3):
            ligne = []
            for j in range(3):
                if self.plateau[i][j]==1:
                    ligne.append("X")
                elif self.plateau[i][j]==-1:
                    ligne.append("O")
                elif self.plateau[i][j]==0:
                    ligne.append(" ")
            print(ligne)

    """ question3)
    écrire une fonction joueur_humain() qui vous permet via input() de dire où vous voulez jouer
    en numéro de ligne et de colonne. Cette fonction doit gérer le fait que vous n'avez le droit de 
    jouer que dans une case vide.
    """
    def jouer_humain(self, jeton):
        # choix de la ligne et vérification de son existence
        print("choisissez la ligne   (0, 1 ou 2): ")
        ligne=int(input())
        if ligne>2 or ligne<0:
            print("les lignes existantes sont entres 0 et 2")
            self.jouer_humain(jeton)
        # choix de la colonne et vérification de son existence
        print("choisissez la colonne (0, 1 ou 2): ")
        colonne=int(input())
        if colonne>2 or colonne<0:
            print("les colonnes existantes sont entres 0 et 2")
            self.jouer_humain(jeton)
        #vérification case vide
        if self.plateau[ligne][colonne] != 0:
            print("il faut jouer dans une case vide")
            self.jouer_humain(jeton)
        #la case se remplit
        else:
            self.plateau[ligne][colonne] = jeton
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
    def jouer_aleatoire(self, jeton):
        L = self.trouver_cases_vides()
        (i,j) = rd.choice(L)
        self.plateau[i][j] = jeton
        self.afficher_plateau()

    def jouer_uncoup(self, indiceJoueur):
        print(self.joueurs[indiceJoueur].nom + " joue:")
        if self.joueurs[indiceJoueur].typeDeJoueur == "humain":
            self.jouer_humain(self.joueurs[indiceJoueur].jeton)
        else:
            self.jouer_aleatoire(self.joueurs[indiceJoueur].jeton)

    """question6)
    ecrire une fonction partie_gagnee() qui renvoie le joueur gagnant : None, "humain", 
    ou "ordinateur", en fonction des règles du jeu du morpion.
    """
    def partie_gagnee(self):
        resultat = 99
        if self.plateau[0][0]==1 and self.plateau[0][1]==1 and self.plateau[0][2]==1:
            resultat=0
        if self.plateau[1][0]==1 and self.plateau[1][1]==1 and self.plateau[1][2]==1:
            resultat=0
        if self.plateau[2][0]==1 and self.plateau[2][1]==1 and self.plateau[2][2]==1:
            resultat=0
        if self.plateau[0][0]==1 and self.plateau[1][0]==1 and self.plateau[2][0]==1:
            resultat=0
        if self.plateau[0][1]==1 and self.plateau[1][1]==1 and self.plateau[2][1]==1:
            resultat=0
        if self.plateau[0][2]==1 and self.plateau[1][2]==1 and self.plateau[2][2]==1:
            resultat=0
        if self.plateau[0][0]==1 and self.plateau[1][1]==1 and self.plateau[2][2]==1:
            resultat=0
        if self.plateau[0][2]==1 and self.plateau[1][1]==1 and self.plateau[2][0]==1:
            resultat=0
        if self.plateau[0][0]==-1 and self.plateau[0][1]==-1 and self.plateau[0][2]==-1:
            resultat=1
        if self.plateau[1][0]==-1 and self.plateau[1][1]==-1 and self.plateau[1][2]==-1:
            resultat=1
        if self.plateau[2][0]==-1 and self.plateau[2][1]==-1 and self.plateau[2][2]==-1:
            resultat=1
        if self.plateau[0][0]==-1 and self.plateau[1][0]==-1 and self.plateau[2][0]==-1:
            resultat=1
        if self.plateau[0][1]==-1 and self.plateau[1][1]==-1 and self.plateau[2][1]==-1:
            resultat=1
        if self.plateau[0][2]==-1 and self.plateau[1][2]==-1 and self.plateau[2][2]==-1:
            resultat=1
        if self.plateau[0][0]==-1 and self.plateau[1][1]==-1 and self.plateau[2][2]==-1:
            resultat=1
        if self.plateau[0][2]==-1 and self.plateau[1][1]==-1 and self.plateau[2][0]==-1:
            resultat=1
        if resultat in [0, 1]:
            return resultat
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
        while self.partie_gagnee() != 0 or self.partie_gagnee() != 1 or self.partie_gagnee() != None:
            for i in range(9):
                self.jouer_uncoup(i%2)
                if self.partie_gagnee() in [0, 1]:
                    print(self.joueurs[self.partie_gagnee()].nom + " remporte la partie.")
                    return
            print("Match nul, pas de gagnant")
            return
        
partie = morpion("ordinateur", "ordinateur")
print('*************** PREMIERE PARTIE *****************')
partie.jouer()
partie.initialiser_plateau()
print('*************** DEUXIEME PARTIE *****************')
partie.jouer()


