ZONE_PLAN_MINI = (-320, -320)  # Coin inférieur gauche de la zone d'affichage du plan
ZONE_PLAN_MAXI = (50, 200)  # Coin supérieur droit de la zone d'affichage du plan
POINT_AFFICHAGE_ANNONCES = (-320, 240)  # Point d'origine de l'affichage des annonces
POINT_AFFICHAGE_INVENTAIRE = (70, 200)  # Point d'origine de l'affichage de l'inventaire

# Les valeurs ci-dessous définissent les couleurs des cases du plan
COULEUR_CASES = 'white'
COULEUR_COULOIR = 'white'
COULEUR_MUR = 'grey'
COULEUR_OBJECTIF = 'yellow'
COULEUR_PORTE = 'orange'
COULEUR_OBJET = 'green'
COULEUR_VUE = 'wheat'
COULEURS = [COULEUR_COULOIR, COULEUR_MUR, COULEUR_OBJECTIF, COULEUR_PORTE, COULEUR_OBJET, COULEUR_VUE]
COULEUR_EXTERIEUR = 'white'

# Couleur et dimension du personnage
COULEUR_PERSONNAGE = 'red'
RATIO_PERSONNAGE = 0.9  # Rapport entre diamètre du personnage et dimension des cases
POSITION_DEPART = (0, 3)  # Porte d'entrée du château

# Désignation des fichiers de données à utiliser
fichier_plan = 'plan_chateau.txt'
fichier_questions = 'dico_portes.txt'
fichier_objets = 'dico_objets.txt'

GAUCHE = (0, -1) # constantes globales décrivant les différents mouvements 
DROITE = (0, 1)
HAUT = (-1, 0)
BAS = (1, 0)

ANNONCES = "annonces" # répété plusieurs fois dans le code --> une constante globale évite les erreurs
HAUTEUR_ZONE_ANNONCES = POINT_AFFICHAGE_ANNONCES[1] - ZONE_PLAN_MAXI[1]
LARGEUR_ZONE_ANNONCES = 600
PADDING_TOP_ANNONCE = 20 # espace entre l'annonce et le bord supérieur de sa zone
PADDING_LEFT_ANNONCE = 5 # espace entre l'annonce et le bord gauche de sa zone
COORDONNEES_DEPART_ANNONCE = POINT_AFFICHAGE_ANNONCES[0] + PADDING_LEFT_ANNONCE, POINT_AFFICHAGE_ANNONCES[1] - PADDING_TOP_ANNONCE

INVENTAIRE = "inventaire" # répété plusieurs fois dans le code --> une constante globale évite les erreurs
TITRE_INVENTAIRE = "Inventaire : "
HAUTEUR_INVENTAIRE = POINT_AFFICHAGE_INVENTAIRE[1] - ZONE_PLAN_MINI[1]
LARGEUR_INVENTAIRE = 300
PAS_INVENTAIRE = 20 # espacement avant chaque ligne de l'inventaire

# correspondance entre valeur de la case et sa signification
COULOIR = 0
MUR = 1  
PORTE = 3
OBJET = 4
ARRIVEE = 2

# différents messages
MESSAGE_PORTE_FERMEE = "Cette porte est fermée."
MESSAGE_PORTE_OUVERTE = "La porte s'ouvre."
TITRE_FENETRE_QUESTION = "Question"
MESSAGE_ARRIVEE = "Bravo ! Vous avez gagné !"
MESSAGE_ECHEC = "Mauvaise réponse."
MESSAGE_OBJET = "Vous avez trouvé "

# Police et tailles d'écriture
COULEUR_ECRITURE = 'black'
POLICE = "Comic Sans MS"
TAILLE_TITRE_INVENTAIRE = 12
TAILLE_OBJET_INVENTAIRE = 10
TAILLE_ANNONCE = 11
TEMPS_OUVERTURE_PORTE = 0.6 # temps de latence entre l'ouverture de la porte et le déplacement du joueur
TEMPS_AVANT_ARRET_PROGRAMME = 3