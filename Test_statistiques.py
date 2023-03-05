import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from fpdf import FPDF

def Analyse_result():
    # Lire le fichier CSV dans un dataframe
    data = pd.read_csv('Global.csv')

    # Remplacer les valeurs "F" et "M" dans la colonne "Genre" par 0 et 1, respectivement
    data['Genre'].replace({'F': 0, 'M': 1}, inplace=True)
    # Enregistrer les modifications dans le fichier CSV
    data.to_csv('Global.csv', index=False)
    data = pd.read_csv('Global.csv')
    
    # Calculer le pourcentage de bonnes réponses pour chaque participant
    data['PctCorrect'] = data.groupby('ID')['Reponse'].transform(lambda x: (x == data.loc[x.index, 'Mot']).sum() / len(x) * 100)

    # Effectuer le test de Student pour comparer les temps de réponse entre les hommes et les femmes
    time_male = data.loc[data['Genre'] == 1, 'Temps de reponse']
    time_female = data.loc[data['Genre'] == 0, 'Temps de reponse']
    t_time, p_time_sex = stats.ttest_ind(time_male, time_female)

    # Effectuer le test de Student pour comparer les pourcentages de bonnes réponses entre les hommes et les femmes
    pct_male = data.loc[data['Genre'] == 1, 'PctCorrect']
    pct_female = data.loc[data['Genre'] == 0, 'PctCorrect']
    t_pct, p_pct = stats.ttest_ind(pct_male, pct_female)

    # Calculer la corrélation entre l'âge et le pourcentage de bonnes réponses
    corr, p_age = stats.pearsonr(data['Age'], data['PctCorrect'])

    # Calculer la corrélation entre le pourcentage de bonnes réponses et la vitesse de réponse
    corr_pct_time, p_time = stats.pearsonr(data['PctCorrect'], data['Temps de reponse'])
    texte = Resultat(t_time, p_time_sex, t_pct, p_pct, corr, p_age, corr_pct_time, p_time)
    Graphique(data)
    enregistrer_dans_pdf(texte)


def enregistrer_dans_pdf(texte):
    # Créer un nouveau document PDF
    pdf = FPDF()
    pdf.add_page()

    # Définir la police et la taille de la police
    pdf.set_font("Arial", size=12)

    # Écrire le texte dans le document PDF
    pdf.multi_cell(0, 10, txt=texte)

    # Enregistrer le document PDF dans un fichier
    nom_fichier = "Statistiques.pdf"
    pdf.output(nom_fichier)

def Resultat(t_time, p_time_sex, t_pct, p_pct, corr, p_age, corr_pct_time, p_time):
    resultat_texte = ''
    resultat_texte += 'Test de Student pour les temps de réponse:\n'
    resultat_texte += '  t-value: ' + str(t_time) + '\n'
    resultat_texte += '  p-value: ' + str(p_time_sex) + '\n'
    resultat_texte += 'Test de Student pour les pourcentages de bonnes réponses:\n'
    resultat_texte += '  t-value: ' + str(t_pct) + '\n'
    resultat_texte += '  p-value: ' + str(p_pct) + '\n'
    resultat_texte += 'La corrélation entre l\'âge et le pourcentage de bonnes réponses est de : ' + str(corr) + '\n'
    resultat_texte += 'La p-value de la corrélation est de : ' + str(p_age) + '\n'
    resultat_texte += 'La corrélation entre le pourcentage de bonnes réponses et la vitesse de réponse est de : ' + str(corr_pct_time) + '\n'
    resultat_texte += 'La p-value de la corrélation est de : ' + str(p_time) + '\n'
    print(resultat_texte)
    return resultat_texte


def Graphique(data):
    visualisations = [
        {'type': 'boxplot', 'x': 'Genre', 'y': 'Temps de reponse', 'xlabel': 'Sexe', 'ylabel': 'Temps de réponse', 'titre': 'Comparaison des temps de réponse entre les hommes et les femmes', 'fichier': 'Graphique_temps_sexe.pdf'},
        {'type': 'boxplot', 'x': 'Genre', 'y': 'PctCorrect', 'xlabel': 'Sexe', 'ylabel': 'Pourcentage de bonnes réponses', 'titre': 'Comparaison des pourcentages de bonnes réponses entre les hommes et les femmes', 'fichier': 'Graphique_pctcorrect_sexe.pdf'},
        {'type': 'regplot', 'x': 'Age', 'y': 'PctCorrect', 'xlabel': 'Age', 'ylabel': 'Pourcentage de bonnes réponses', 'titre': 'Relation entre l\'âge et le pourcentage de bonnes réponses', 'fichier': 'Graphique_age_pctcorrect.pdf'},
        {'type': 'regplot', 'x': 'Temps de reponse', 'y': 'PctCorrect', 'xlabel': 'Temps de reponse', 'ylabel': 'Pourcentage de bonnes réponses', 'titre': 'Relation entre le temps de réponse et le pourcentage de bonnes réponses', 'fichier': 'Graphique_temps_pctcorrect.pdf'}
    ]
    for v in visualisations:
        plt.figure()
        if v['type'] == 'boxplot':
            sns.boxplot(x=v['x'], y=v['y'], data=data)
        elif v['type'] == 'regplot':
            sns.regplot(x=data[v['x']], y=data[v['y']])
        plt.xlabel(v['xlabel'])
        plt.ylabel(v['ylabel'])
        plt.title(v['titre'])
        plt.savefig(v['fichier'], format='pdf')
        plt.show()





