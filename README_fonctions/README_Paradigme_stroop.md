# README (English)
## Stroop Task

This code implements a basic version of the Stroop task using Pygame. The Stroop task is a classic psychological experiment that measures the ability of an individual to inhibit automatic responses and to perform a task that requires attention and cognitive control. In this implementation, the user is presented with words written in different colors and is asked to press a key corresponding to the meaning of the word, not the color of the word. The experiment generates data on the response times and accuracy of the user.

## Usage

To run the Stroop task, simply call the stroop() function and pass in the number of trials that you want to run as an argument. The function returns a tuple of lists containing the user's responses, the colors of the words, the words themselves, the response times, and the iteration number for each trial. For example:


  import stroop

  answer, colors, words, response_times, iteration = stroop(10)

This will run 10 trials of the Stroop task and store the data in the variables answer, colors, words, response_times, and iteration.

# README (Français)
## Tâche de Stroop

Ce code implémente une version de base de la tâche de Stroop en utilisant Pygame. La tâche de Stroop est une expérience psychologique classique qui mesure la capacité d'un individu à inhiber des réponses automatiques et à effectuer une tâche qui nécessite de l'attention et du contrôle cognitif. Dans cette implémentation, l'utilisateur est présenté avec des mots écrits dans différentes couleurs et doit appuyer sur une touche correspondant à la signification du mot, et non pas à la couleur du mot. L'expérience génère des données sur les temps de réponse et l'exactitude de l'utilisateur.

## Utilisation

Pour exécuter la tâche de Stroop, appelez simplement la fonction stroop() et passez le nombre d'essais que vous souhaitez exécuter en tant qu'argument. La fonction renvoie un tuple de listes contenant les réponses de l'utilisateur, les couleurs des mots, les mots eux-mêmes, les temps de réponse et le numéro d'itération pour chaque essai. Par exemple :


  import stroop

  answer, colors, words, response_times, iteration = stroop(10)

Cela exécutera 10 essais de la tâche de Stroop et stockera les données dans les variables answer, colors, words, response_times et iteration.
