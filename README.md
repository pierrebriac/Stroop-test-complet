# README (EN)
## Stroop Test

This code implements the Stroop test, a psychological task designed to measure cognitive control and selective attention. In this test, participants are presented with words printed in different ink colors, and they have to name the word while ignoring the color of the ink.
The code is written in Python and uses the following libraries:

- csv
- pandas
- tkinter
- os
- re
- numpy
- random
- time
- pygame
- seaborn
- matplotlib
- scipy
- fdpf

## Usage

Once the file has been downloaded, it must be placed on the desktop and named Stroop_test
To use the Stroop test, run the Python script Stroop_test.py. A window will appear asking for the participant's information (name, age, sex, and ID). After filling out the information, click the "Continue" button to start the test.

The Stroop test consists of 10 trials, and the participant's answers and response times are recorded in a CSV file. The file is saved in a folder named "Stroop_test" on the participant's desktop.

After completing the test, the code generates a PDF report that includes the participant's score, statistics, and a graph of the response times. The report is saved in the same folder as the CSV file.

There is already a file with data that is not confidential (personal data) as well as files created by the code as an example. You can remove them to run the code.

# Statistics
To start the analysis of the results just call python main_stats.py in the terminal.
Regarding statistics, there is a comparison of the participant to the rest of the group, an analysis of missing data. There are also two t-tests to find out if the participants differed by gender on the response time and percent correct variables.

We then look at whether there is a correlation between percentages of correct answers and speed of responding, and between age and percentage of correct answers.

The statistics are saved in PDF format whether it is the graphs or the results of the statistical tests.

# README (FR)
## Test de Stroop

Ce code implémente le test de Stroop, une tâche psychologique conçue pour mesurer le contrôle cognitif et l'attention sélective. Dans ce test, les participants voient des mots imprimés dans différentes couleurs d'encre et doivent nommer le mot affiché tout en ignorant la couleur de l'encre.

Le code est écrit en Python et utilise les bibliothèques suivantes :

- csv
- pandas
- tkinter
- os
- re
- numpy
- random
- time
- pygame
- seaborn
- matplotlib
- scipy
- fdpf

## Utilisation

Une fois le dossier téléchargé il faut le déposer sur le bureau et le nommer Stroop_test.
Pour utiliser le test de Stroop, exécutez le script Python Stroop_test.py. Une fenêtre apparaîtra demandant les informations du participant (nom, âge, sexe et ID). Après avoir rempli les informations, cliquez sur le bouton "Continuer" pour commencer le test.

Le test de Stroop se compose de 10 épreuves, et les réponses et les temps de réponse du participant sont enregistrés dans un fichier CSV. Le fichier est enregistré dans un dossier nommé "Stroop_test" sur le bureau du participant.
Il y a déjà un fichier avec des données qui ne sont pas confidentielles (données personnelles) ainsi que des fichiers créés par le code à titre d'exemple. Vous pouvez les supprimer pour lancer le code.

# Statistiques 
Pour lancer l'analyse des résultats il suffit d'appeler python main_stats.py dans le terminal.

Concernant les statistiques, il y a une comparaison du participant au reste du groupe, une analyse des données manquantes. Il y a aussi deux tests t pour savoir si les participants diffèrent en fonction du sexe sur les variables temps de réponse et pourcentage de bonne réponse.

On regarde ensuite s'il y a une corrélation entre pourcentages de bonnes réponses et rapidité à répondre, et entre âge et pourcentage de bonnes réponses.

Les statistiques sont enregistrées en format PDF que ce soit les graphiques ou les résultats des tests statistiques.
