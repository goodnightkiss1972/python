import random as rnd

rnd.seed("123")

# distances chez nous "Mercure":0.4, "Venus":0.7, "Terre":1, "Mars":1.5, "Jupiter":5.2, "Saturne":9.5, "Uranus":19.6, "Neptune":30

# dictionnaires universels
dico_Etoiles = {"Naine Brune": 1, "Naine Rouge": 2, "Naine Jaune": 3, "Geante Rouge": 4, "Geante Bleue": 5, "Supergeante Rouge": 6}
def rechercher_dico_Etoiles_par_valeur(p_recherche):
    for cle, valeur in dico_Etoiles.items():
        if p_recherche == valeur:
            return cle
    return "Etoile de type inconnu..."

dico_Planetes = {"Tellurique": 1, "Gazeuze": 2}
def rechercher_dico_Planetes_par_valeur(p_recherche):
    for cle, valeur in dico_Planetes.items():
        if p_recherche == valeur:
            return cle
    return "Planete de type inconnu..."

class etoile():
    def __init__(self):
        self.typeEtoile = self.initialiser_type_etoile()
        self.masseEtoile = self.initialiser_masse_etoile()

    def initialiser_type_etoile(self):
        # tirage selon la suite de fibonacci
        tirage_type_etoile = [6, 5, 5, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0]
        return(tirage_type_etoile[rnd.randint(0, len(tirage_type_etoile)-1)])

    def initialiser_masse_etoile(self):
        # tirage de la masse exprimee en masse solaire en fonction du type de l'etoile
        if self.typeEtoile == 1:
            return(rnd.randint(1, 7)/100)
        if self.typeEtoile == 2:
            return(rnd.randint(8, 30)/100)
        if self.typeEtoile == 3:
            return(rnd.randint(40, 250)/100)
        if self.typeEtoile == 4:
            return(rnd.randint(250, 1800)/100)
        if self.typeEtoile == 5:
            return(rnd.randint(1800, 2000)/100)
        if self.typeEtoile == 6:
            return(rnd.randint(2000, 4000)/100)

    def afficher_etoile(self):
        print("Etoile de type " + str(self.typeEtoile) + " (" + rechercher_dico_Etoiles_par_valeur(self.typeEtoile) + ") masse : " + str(self.masseEtoile) + " ms.")

class planete():
    def __init__(self, distanceEtoile, typePlanete):
        self.distanceEtoile = distanceEtoile
        self.typePlanete = typePlanete
        self.massePlanete = self.choisir_masse_planete()
    
    def choisir_masse_planete(self):
        if self.typePlanete == 1:
            return(rnd.randint(3, 250)/100)
        if self.typePlanete == 2:
            return(rnd.randint(1000, 40000)/100)

    def afficher_planete(self):
        print("Planete de type " + str(self.typePlanete) + " (" + rechercher_dico_Planetes_par_valeur(self.typePlanete) + ") Distance : " + str(self.distanceEtoile) + " ua, Masse : " + str(self.massePlanete) + " mt.")

class systeme():
    def __init__(self, identifiant):
        self.identifiant = identifiant
        self.etoiles = []
        self.initialiser_etoiles()
        self.rayon = self.calculer_rayon_systeme()
        self.planetes = []
        self.initialiser_planetes()

    def initialiser_etoiles(self):
        for i in range(rnd.randint(1, 2)): # une ou deux etoiles par systeme pas plus
            self.etoiles.append(etoile())

    def calculer_rayon_systeme(self):
        r = 0
        for i in range(len(self.etoiles)):
            r = r + self.etoiles[i].masseEtoile
        return int(rnd.randint(100, 180) * r)
    
    def initialiser_planetes(self):
        nb_telluriques = rnd.randint(1, 7)
        for i in range(nb_telluriques):
            self.planetes.append(planete(rnd.randint(500, int(1000 * self.rayon /3)) / 1000, 1))
        nb_gazeuzes = rnd.randint(0, 5)
        for i in range(nb_gazeuzes):
            self.planetes.append(planete(rnd.randint(int(1000 * self.rayon / 2), int(1000 * self.rayon)) / 1000, 2))
    
    def afficher_systeme(self):
        print()
        print("Systeme id: " + str(self.identifiant) + " de rayon " + str(self.rayon) + " ua.")
        for i in range(len(self.etoiles)):
            self.etoiles[i].afficher_etoile()
        print("Planetes:")
        for i in range(len(self.planetes)):
            self.planetes[i].afficher_planete()

mesSystemes = []
for i in range(3):
    mesSystemes.append(systeme(i))
    mesSystemes[i].afficher_systeme()

