# README (English)
## Stroop Test Analysis

This code provides basic analysis of data collected from the Stroop test using Python's Pandas library. The Stroop test is a classic psychological experiment that measures the ability of an individual to inhibit automatic responses and to perform a task that requires attention and cognitive control. In this implementation, the user performs the Stroop task and their responses are recorded. The code analyzes the data to determine the percentage of correct responses, response times, and missing data. The data is then visualized using Seaborn.

## Requirements

This code requires Python's Pandas and Seaborn libraries to be installed. These can be installed using pip:

pip install pandas
pip install seaborn

## Usage

To use the code, call the statistiques(id_participant) function and pass in the participant's ID as an argument. The function reads in the participant's data and the global data and performs analysis on the participant's responses. The function also generates visualizations of the missing data using Seaborn's heatmap function. The results are printed to the console. For example:

python

import pandas as pd
import seaborn as sns
from stroop_analysis import statistiques

id_participant = 1
statistiques(id_participant)

This will analyze the data for participant 1 and generate a visualization of the missing data using Seaborn.

# README (Français)
## Analyse de la tâche de Stroop

Ce code fournit une analyse de base des données collectées à partir de la tâche de Stroop en utilisant la bibliothèque Pandas de Python. La tâche de Stroop est une expérience psychologique classique qui mesure la capacité d'un individu à inhiber des réponses automatiques et à effectuer une tâche qui nécessite de l'attention et du contrôle cognitif. Dans cette implémentation, l'utilisateur effectue la tâche de Stroop et ses réponses sont enregistrées. Le code analyse les données pour déterminer le pourcentage de réponses correctes, les temps de réponse et les données manquantes. Les données sont ensuite visualisées à l'aide de Seaborn.

## Exigences

Ce code nécessite que les bibliothèques Pandas et Seaborn de Python soient installées. Elles peuvent être installées en utilisant pip :

pip install pandas
pip install seaborn

## Utilisation

Pour utiliser le code, appelez la fonction statistiques(id_participant) et passez l'identifiant du participant en argument. La fonction lit les données du participant et les données globales et effectue une analyse des réponses du participant. La fonction génère également des visualisations des données manquantes à l'aide de la fonction heatmap de Seaborn. Les résultats sont imprimés dans la console. Par exemple :

python

import pandas as pd
import seaborn as sns
from stroop_analysis import statistiques

id_participant = 1
statistiques(id_participant)

Cela analysera les données du participant 1 et générera une visualisation des données manquantes à l'aide de Seaborn.
