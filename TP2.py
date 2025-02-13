"""
TP2 : Gestion d'une base de données d'un hôpital

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
"""

import csv

########################################################################################################## 
# PARTIE 1 : Initialisation des données (2 points)
##########################################################################################################

def load_csv(csv_path):
    """
    Fonction python dont l'objectif est de venir créer un dictionnaire "patients_dict" à partir d'un fichier csv

    Paramètres
    ----------
    csv_path : chaîne de caractères (str)
        Chemin vers le fichier csv (exemple: "/home/data/fichier.csv")
    
    Résultats
    ---------
    patients_dict : dictionnaire python (dict)
        Dictionnaire composé des informations contenues dans le fichier csv
    """
    patients_dict = {}
    
    # TODO : Écrire votre code ici
    with open(csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
           participant_id = row.pop("participant_id")  # Remplacez 'ID' par le nom exact de la colonne d'identifiant dans le CSV
           patients_dict[participant_id] = row 
    return patients_dict
csv_path = "subjects.csv"
patients_dict = load_csv(csv_path)
print(patients_dict["sub-tokyoIngenia04"])   
  
########################################################################################################## 
# PARTIE 2 : Fusion des données (3 points)
########################################################################################################## 

def load_multiple_csv(csv_path1, csv_path2):
    """
    Fonction python dont l'objectif est de venir créer un unique dictionnaire "patients" à partir de deux fichier csv

    Paramètres
    ----------
    csv_path1 : chaîne de caractères (str)
        Chemin vers le premier fichier csv (exemple: "/home/data/fichier1.csv")
    
    csv_path2 : chaîne de caractères (str)
        Chemin vers le second fichier csv (exemple: "/home/data/fichier2.csv")
    
    Résultats
    ---------
    patients_dict : dictionnaire python (dict)
        Dictionnaire composé des informations contenues dans les deux fichier csv SANS DUPLICATIONS
    """
    patients_dict = {}
    def load_csv(csv_path):
        with open(csv_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                participant_id = row.pop("participant_id")  # Remplacez 'ID' par le nom exact de la colonne d'identifiant dans le CSV
                if participant_id:
                  if participant_id not in patients_dict:
                    patients_dict[participant_id] = row 
    load_csv(csv_path1)
    load_csv(csv_path2)
    return patients_dict
    
csv_path1 = "subjects.csv"
csv_path2 = "extra_subjects.csv"


    # Fin du code
patients_dict = load_multiple_csv(csv_path1, csv_path2)
print(patients_dict["sub-sherbrooke06"]) 
########################################################################################################## 
# PARTIE 3 : Changements de convention (4 points)
########################################################################################################## 

def update_convention(old_convention_dict):
    """
    Fonction python dont l'objectif est de mettre à jour la convention d'un dictionnaire. Pour ce faire, un nouveau dictionnaire
    est généré à partir d'un dictionnaire d'entré.

    Paramètres
    ----------
    old_convention_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients" suivant l'ancienne convention
    
    Résultats
    ---------
    new_convention_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients" suivant la nouvelle convention
    """
    new_convention_dict = {}

    # TODO : Écrire votre code ici


    # Fin du code

    return new_convention_dict

########################################################################################################## 
# PARTIE 4 : Recherche de candidats pour une étude (5 points)
########################################################################################################## 

def fetch_candidates(patients_dict):
    """
    Fonction python dont l'objectif est de venir sélectionner des candidats à partir d'un dictionnaire patients et 3 critères:
    - sexe = femme
    - 25 <= âge <= 32
    - taille > 170

    Paramètres
    ----------
    patients_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients"
    
    Résultats
    ---------
    candidates_list : liste python (list)
        Liste composée des `participant_id` de l'ensemble des candidats suivant les critères
    """
    candidates_list = []

    # TODO : Écrire votre code ici


    # Fin du code

    return candidates_list

########################################################################################################## 
# PARTIE 5 : Statistiques (6 points)
########################################################################################################## 

def fetch_statistics(patients_dict):
    """
    Fonction python dont l'objectif est de venir calculer et ranger dans un nouveau dictionnaire "metrics" la moyenne et 
    l'écart type de l'âge, de la taille et de la masse pour chacun des sexes présents dans le dictionnaire "patients_dict".

    Paramètres
    ----------
    patients_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients"
    
    Résultats
    ---------
    metrics : dictionnaire python (dict)
        Dictionnaire à 3 niveaux contenant:
            - au premier niveau: le sexe --> metrics.keys() == ['M', 'F']
            - au deuxième niveau: les métriques --> metrics['M'].keys() == ['age', 'height', 'weight'] et metrics['F'].keys() == ['age', 'height', 'weight']
            - au troisième niveau: la moyenne et l'écart type --> metrics['M']['age'].keys() == ['mean', 'std'] ...
    
    """
    metrics = {'M':{}, 'F':{}}

    # TODO : Écrire votre code ici


    # Fin du code

    return metrics

########################################################################################################## 
# PARTIE 6 : Bonus (+2 points)
########################################################################################################## 

def create_csv(metrics):
    """
    Fonction python dont l'objectif est d'enregister le dictionnaire "metrics" au sein de deux fichier csv appelés
    "F_metrics.csv" et "M_metrics.csv" respectivement pour les deux sexes.

    Paramètres
    ----------
    metrics : dictionnaire python (dict)
        Dictionnaire à 3 niveaux généré lors de la partie 5
    
    Résultats
    ---------
    paths_list : liste python (list)
        Liste contenant les chemins des deux fichiers "F_metrics.csv" et "M_metrics.csv"
    """
    paths_list = []

    # TODO : Écrire votre code ici


    # Fin du code

    return paths_list

########################################################################################################## 
# TESTS : Le code qui suit permet de tester les différentes parties 
########################################################################################################## 

if __name__ == '__main__':
    ######################
    # Tester la partie 1 #
    ######################

    # Initialisation de l'argument
    csv_path = "subjects.csv"

    # Utilisation de la fonction
    patients_dict = load_csv(csv_path)

    # Affichage du résultat
    print("Partie 1: \n\n", patients_dict, "\n")

    ######################
    # Tester la partie 2 #
    ######################

    # Initialisation des arguments
    csv_path1 = "subjects.csv"
    csv_path2 = "extra_subjects.csv"

    # Utilisation de la fonction
    patients_dict_multi = load_multiple_csv(csv_path1=csv_path1, csv_path2=csv_path2)

    # Affichage du résultat
    print("Partie 2: \n\n", patients_dict_multi, "\n")

    ######################
    # Tester la partie 3 #
    ######################

    # Utilisation de la fonction
    new_patients_dict = update_convention(patients_dict)

    # Affichage du résultat
    print("Partie 3: \n\n", patients_dict, "\n")

    ######################
    # Tester la partie 4 #
    ######################

    # Utilisation de la fonction
    patients_list = fetch_candidates(patients_dict)

    # Affichage du résultat
    print("Partie 4: \n\n", patients_list, "\n")

    ######################
    # Tester la partie 5 #
    ######################

    # Utilisation de la fonction
    metrics = fetch_statistics(patients_dict)

    # Affichage du résultat
    print("Partie 5: \n\n", metrics, "\n")

    ######################
    # Tester la partie 6 #
    ######################

    # Initialisation des arguments
    dummy_metrics = {'M':{'age':{'mean':0,'std':0}, 'height':{'mean':0,'std':0}, 'weight':{'mean':0,'std':0}}, 
                     'F':{'age':{'mean':0,'std':0}, 'height':{'mean':0,'std':0}, 'weight':{'mean':0,'std':0}}}
    
    # Utilisation de la fonction
    paths_list = create_csv(metrics)

    # Affichage du résultat
    print("Partie 6: \n\n", paths_list, "\n")

