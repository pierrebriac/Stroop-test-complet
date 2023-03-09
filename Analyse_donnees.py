import matplotlib.pyplot as plt
import seaborn as sns
import os
import csv
import pandas as pd

def val_manquantes(data, id_participant, loc_glob):
    # On regarde les données manquantes
    missing_values = data.isnull().sum()
    missing_values_df = pd.DataFrame(missing_values, columns=['Nombre de valeurs manquantes'])
    missing_values_df['Nom de la variable'] = missing_values_df.index
    missing_values_df.to_csv('Missing_values.csv', index=False)

    # Visualisation des valeurs manquantes à l'aide de la méthode heatmap de seaborn
    sns.heatmap(data.isnull(), cbar=False, cmap='plasma')
    if loc_glob == "loc":
        plt.title('Heatmap des valeurs manquantes du participant ' + str(id_participant))
    else:
        plt.title("Heatmap des valeurs manquantes de l'ensemble des données")
    plt.show()
    plt.show()
    plt.close()

def recodage(data_participant, name, data_global):
    data_participant['Couleurs'] = data_participant['Couleurs'].replace({'blue': "Bleu", 'red': "Rouge", 'green': "Vert"})
    data_participant['Reponses'] = data_participant['Reponses'].replace({'b': "Bleu", 'r': "Rouge", 'v': "Vert"})
    dossier = os.path.join(os.environ['HOME'], 'Desktop', 'Stroop_test', 'Resultat_individuel')
    filename = os.path.join(dossier, name)
    data_participant.to_csv(filename, index=False)

    data_global['Couleur du mot'] = data_global['Couleur du mot'].replace({'blue': "Bleu", 'red': "Rouge", 'green': "Vert"})
    data_global['Reponse'] = data_global['Reponse'].replace({'b': "Bleu", 'r': "Rouge", 'v': "Vert"})
    data_global.to_csv('Global.csv', index=False)

def afficher_resultats(pourcentage_global, pourcentage_utilisateur, mean_groupe, mean_parti):
    print(f"Pourcentage de bonnes réponses globales : {pourcentage_global:.2f}%")
    print(f"Temps moyen de réponse du groupe : {mean_groupe:.2f} secondes")
    print(f"Pourcentage de bonnes réponses de l'utilisateur : {pourcentage_utilisateur:.2f}%")
    print(f"Temps moyen de réponse de l'utilisateur : {mean_parti:.2f} secondes")

def score(data_participant, data_global): 
    # Résultats globaux
    Liste_mot_glob = data_global["Mot"]
    Liste_rep_glob = data_global["Reponse"]

    # Résultats individuels
    Liste_mot_part = data_participant["Liste de mots"]
    Liste_rep_part = data_participant["Reponses"]

    # Compter le nombre de correspondances entre les deux listes
    nb_bonnes_reponses = 0
    for i in range(len(Liste_mot_glob)):
        if Liste_mot_glob[i] == Liste_rep_glob[i]:
            nb_bonnes_reponses += 1

    # Calculer le pourcentage de bonnes réponses
    pourcentage_bonnes_reponses_glob = nb_bonnes_reponses / len(Liste_mot_glob) * 100

    # Compter le nombre de correspondances entre les deux listes
    nb_bonnes_reponses_uti = 0
    for i in range(len(Liste_mot_part)):
        if Liste_mot_part[i] == Liste_rep_part[i]:
            nb_bonnes_reponses_uti += 1

    # Calculer le pourcentage de bonnes réponses
    pourcentage_bonnes_reponses_parti = nb_bonnes_reponses_uti / len(Liste_mot_part) * 100

    # Temps moyen de réponse du groupe
    mean_groupe = data_global["Temps de reponse"].mean()
    # Temps moyen de réponse du participant
    mean_parti = data_participant["Temps de reponse"].mean()
    afficher_resultats(pourcentage_bonnes_reponses_glob, pourcentage_bonnes_reponses_parti, mean_groupe, mean_parti)

def statistiques(id_participant):
    # Importer mon data frame global
    data_global = pd.read_csv("Global.csv")

    # Ouvrir data frame du participant
    dossier = os.path.join(os.environ['HOME'], 'Desktop', 'Stroop_test', 'Resultat_individuel')
    filename = os.path.join(dossier, "Donnees_participant_" + str(id_participant) + ".csv")
    name = "Donnees_participant_" + str(id_participant) + ".csv"

    data_participant = pd.read_csv(filename)
    recodage(data_participant, name, data_global)
    score(data_participant, data_global)
    val_manquantes(data_participant, id_participant, "loc")
    val_manquantes(data_global, id_participant, "glob")
