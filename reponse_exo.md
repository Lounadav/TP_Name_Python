Exo1 : 
L'écran affichera uniquement : Module chargé.

Ce message s'affiche car Python exécute tout le code global lors de l'importation.

La ligne "programme principal" ne s'affiche pas car la condition if __name__ == "__main__": est fausse quand le fichier est importé.

Exo2 :

L'écran affiche 1 car Python exécute le code d'un module une seule fois, lors du tout premier import.

Le deuxième import est ignoré (Python utilise le module déjà en mémoire), donc x n'est pas incrémenté de nouveau.git

Exo 3 :

Q1 affiche A, C, B (tout s'exécute) ; Q2 affiche A, B (le bloc if est ignoré lors de l'import).

Q3 affiche aussi A, B, car le second import ne ré-exécute pas le code (le module est déjà chargé).

Exo4:

Question 1 (python a.py)

A1, A3 (A1 : code global, A3 : bloc if __name__ car exécuté directement)

Question 2 (python b.py)

B1, A1, B3, B2, A2 (B1 : code global de b, A1 : import de a, B3 : bloc if __name__ de b, B2/A2 : appel de la fonction g)

Question 3 (import b puis b.g())

B1, A1, B2, A2 (B1/A1 s'affichent à l'import, B2/A2 s'affichent à l'appel manuel de la fonction g)
