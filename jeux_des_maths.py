import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10

BONNE_REPONSE = 0

DEPART_QUESTION = 1
NOMBRE_QUESTION = 11
#ATTENTION 
# ici notre variable "NOMBRE_QUESTION" nous devons ajouter +1 si on veut avoir 
# le bon nombre de question car on commence à UN et non à ZERO.
# Exemple : pour 4 questions voulu on placera le nombre 5.

def poser_une_question():
    global DEPART_QUESTION
    global BONNE_REPONSE
    
    while not DEPART_QUESTION == NOMBRE_QUESTION:
        a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
        b = random.randint(NOMBRE_MIN, NOMBRE_MAX) 
        o = random.randint(0, 1)
        
        operateur = '*'
        if o == 1:
            operateur = '+'

        print(f"Question n°{DEPART_QUESTION}/{NOMBRE_QUESTION-1}")
        print("")
        reponse_str = input(f"-------------> Calculer {a} {operateur} {b} = ")
        print('')
        reponse_int = int(reponse_str)
        calcul = a*b
        if o == 1:
            calcul = a+b
        if  calcul == reponse_int:
            print("Bonne Réponse")
            print("")
            DEPART_QUESTION = DEPART_QUESTION +1
            BONNE_REPONSE = BONNE_REPONSE +1
        else:
            print("Mauvaise Réponse")
            print("")
            DEPART_QUESTION = DEPART_QUESTION +1
            
    print(f"Vous avez eu {BONNE_REPONSE} de bonnes réponses sur {DEPART_QUESTION-1}")
    
    if BONNE_REPONSE == DEPART_QUESTION-1:
        print("Excelent")
    elif BONNE_REPONSE == 0:
        print("Mauvais")
    else:
        print("peux mieux faire")
        
    print(f"Votre moyenne est de {int((BONNE_REPONSE / (NOMBRE_QUESTION - 1)) * 20)}/20")

    
poser_une_question()