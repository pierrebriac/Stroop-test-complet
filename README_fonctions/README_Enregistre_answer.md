# README (English)
## Data Saving and Storage

This code allows for the saving and storage of data collected during the Stroop test using Python's Pandas library. The data is saved both globally and for each individual participant. The data is stored in CSV files and includes information such as the participant's age, gender, ID, response times, and answers.
## Requirements

This code requires Python's Pandas library to be installed. This can be installed using pip:

pip install pandas

## Usage

To use the code, call the enregistrer_donnees(answer, couleurs, liste_mots, temps_reponse, nom, sexe_entry, age_entry, id_entry, iteration) function and pass in the relevant arguments. The function saves the data to a CSV file in two places: a global file that contains all participants' data, and an individual file for the current participant. The function also creates the CSV files if they do not already exist. For example:

import pandas as pd
from data_storage import enregistrer_donnees

id_participant = 1
answer = ['r', 'b', 'v']
couleurs = ['red', 'blue', 'green']
liste_mots = ['Rouge', 'Bleu', 'Vert']
temps_reponse = [0.6, 0.5, 0.7]
nom = "John Doe"
sexe_entry = "M"
age_entry = 30
iteration = [1, 2, 3]

enregistrer_donnees(answer, couleurs, liste_mots, temps_reponse, nom, sexe_entry, age_entry, id_participant, iteration)

This will save the participant's data to both the global file and an individual file named "Donnees_participant_1.csv".

# README (Français)
## Enregistrement et stockage des données

Ce code permet l'enregistrement et le stockage des données collectées lors de la tâche de Stroop en utilisant la bibliothèque Pandas de Python. Les données sont enregistrées à la fois globalement et pour chaque participant individuel. Les données sont stockées dans des fichiers CSV et comprennent des informations telles que l'âge, le genre, l'ID du participant, les temps de réponse et les réponses.
## Exigences

Ce code nécessite que la bibliothèque Pandas de Python soit installée. Elle peut être installée en utilisant pip :

pip install pandas

Utilisation

Pour utiliser le code, appelez la fonction enregistrer_donnees(answer, couleurs, liste_mots, temps_reponse, nom, sexe_entry, age_entry, id_entry, iteration) et passez les arguments pertinents. La fonction enregistre les données dans un fichier CSV à deux endroits : un fichier global qui contient les données de tous les participants, et un fichier individuel pour le participant actuel. La fonction crée également les fichiers CSV s'ils n'existent pas déjà. Par exemple :

import pandas as pd
from data_storage import enregistrer_donnees

id_participant = 1
answer = ['r', 'b', 'v']
couleurs = ['red', 'blue', 'green']
liste_mots = ['Rouge', 'Bleu', 'Vert']
temps_reponse = [0.6, 0.5, 0.7]
nom = "John Doe"
sexe_entry = "M"
age_entry = 30
iteration = [1, 2, 3]

enregistrer_donnees(answer, couleurs, liste_mots, temps_reponse, nom, sexe_entry, age_entry, id_participant, iteration)

Cela enregistrera les données du participant à la fois dans le fichier global et dans un fichier individuel nommé "Donnees_participant_1.csv".
