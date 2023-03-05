import csv
import pandas as pd
from Paradigme_stroop import stroop
import tkinter as tk
from Enregistre_answer import enregistrer_donnees
from Analyse_donnees import val_manquantes, recodage, afficher_resultats, score, statistiques
import os
import re
from Test_statistiques import Analyse_result, enregistrer_dans_pdf, Resultat, Graphique

# Fonction pour vérifier les entrées utilisateur
def check_inputs_donnees():
    # Récupérer les valeurs entrées par l'utilisateur
    nom_val = nom.get()
    age_val = age.get()
    sexe_val = sexe.get()
    id_val = id_participant.get()

    # Vérifier si l'âge est un nombre
    if not re.match("^[0-9]+$", age_val):
        error_label.config(text="L'âge doit être un nombre")
        return
    
    # Vérifier si le sexe est "M" ou "F"
    if sexe_val not in ["M", "F"]:
        error_label.config(text="Le sexe doit être 'M' ou 'F'")
        return
    
    # Vérifier si l'ID est un nombre
    if not re.match("^[0-9]+$", id_val):
        error_label.config(text="L'ID doit être un nombre")
        return

    # Si toutes les vérifications sont passées, afficher les valeurs entrées
    error_label.config(text="")
    print("Nom:", nom_val)
    print("Âge:", age_val)
    print("Sexe:", sexe_val)
    print("ID participant:", id_val)
    root.withdraw() # masquer la fenêtre principale
    show_experiment_information_window() # afficher la fenêtre d'expérience

# Créer la fenêtre principale
root = tk.Tk()

# Définir la taille de la fenêtre pour qu'elle prenne tout l'écran
largeur_ecran = root.winfo_screenwidth()
hauteur_ecran = root.winfo_screenheight()
root.geometry(f"{largeur_ecran}x{hauteur_ecran}")

# Ajouter des étiquettes pour indiquer ce qu'il faut saisir dans chaque case
nom_label = tk.Label(root, text="Nom:")
nom_label.pack(padx=20, pady=10)
nom_entry = tk.Entry(root)
nom_entry.pack(padx=20, pady=10)
nom = nom_entry

age_label = tk.Label(root, text="Âge:")
age_label.pack(padx=20, pady=10)
age_entry = tk.Entry(root)
age_entry.pack(padx=20, pady=10)
age = age_entry

sexe_label = tk.Label(root, text="Sexe (M ou F):")
sexe_label.pack(padx=20, pady=10)
sexe_entry = tk.Entry(root)
sexe_entry.pack(padx=20, pady=10)
sexe = sexe_entry

id_label = tk.Label(root, text="ID Participant:")
id_label.pack(padx=20, pady=10)
id_entry = tk.Entry(root)
id_entry.pack(padx=20, pady=10)
id_participant = id_entry

# Ajouter un bouton pour continuer
continue_button = tk.Button(root, text="Continuer", command=lambda: check_inputs_donnees())
continue_button.pack(padx=20, pady=20)

# Ajouter une étiquette pour afficher les messages d'erreur
error_label = tk.Label(root, fg="red")
error_label.pack(padx=20, pady=10)

# Fonction pour vérifier que toutes les données ont été saisies
def check_inputs():
    if nom_entry.get() and age_entry.get() and sexe_entry.get() and id_entry.get():
        # Toutes les données ont été saisies, masquer la fenêtre principale et afficher la fenêtre d'expérience
        root.withdraw()
        show_experiment_information_window()
    else:
        # Afficher un message d'erreur si des données sont manquantes
        error_message = "Veuillez remplir tous les champs avant de continuer."
        error_label.config(text=error_message)

def start_experiment_task():
   # On lance la tâche de Stroop
    answer, couleurs, liste_mots, temps_reponse, iteration = stroop(10)
    # On enregistre les données de la tâche de Stroop
    enregistrer_donnees(answer, couleurs, liste_mots, temps_reponse, nom_entry, sexe_entry, age_entry, id_entry, iteration)
    # Spécifier le nom du dossier et le chemin d'accès pour l'enregistrement du fichier individuel
    dossier = os.path.join(os.environ['HOME'], 'Desktop', 'Stroop_test', 'Info_participant')
    filename = os.path.join(dossier, "Info_participant_" + id_entry.get() + ".csv")

    # Enregistrer les données dans le fichier CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nom', 'Âge', 'Sexe', 'ID Participant'])
        writer.writerow([nom_entry.get(), age_entry.get(), sexe_entry.get(), id_entry.get()])

    root.destroy()

# Fonction pour afficher les informations de l'expérience
def show_experiment_information_window():
    def start_experiment(event):
        experiment_info_window.destroy()
        start_experiment_task()

    experiment_info = """
    Expérience de Stroop

    Dans cette expérience, vous allez voir des mots de couleurs affichés à l'écran.
    Votre tâche est de dire la couleur de l'encre du mot aussi rapidement que possible,
    en ignorant le mot lui-même. Par exemple, si vous voyez le mot "rouge" écrit en vert,
    vous devez dire "vert".

    Appuyez sur la touche espace pour commencer l'expérience.

    Bonne chance!
    """
    experiment_info_window = tk.Toplevel()
    experiment_info_window.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    experiment_info_window.title("Expérience de Stroop")
    experiment_info_label = tk.Label(experiment_info_window, text=experiment_info, font=("Arial", 24))
    experiment_info_label.pack(padx=20, pady=20)
    
    # Ajouter une liaison de clavier pour écouter l'appui sur la touche espace
    experiment_info_window.bind("<space>", start_experiment)

# Lancer la fenêtre principale
root.mainloop()
statistiques(id_participant)
Analyse_result()

