"""
-------------------------------------------------------------
PGR107 Assignment                                           #
Date: 25.03.2023                                            #
Authors: Jack Xia & Gabriel Berrios                         #
Version 1.0                                                 #
-------------------------------------------------------------
"""

"""
-------------------------------------------------------------------------------------------------
Program description: Presents a menu with 3 choices, quiz,show results and exit.                #
                                                                                                #
Option 1: The quiz results are presented at the end, showing the wrong answers and presenting   #
the solution of the answer.                                                                     #
                                                                                                #
Option 2: show results option stores the results from the first quiz adding a score, if         #
users choose to take the quiz again the results will highlight the highest                      #
score and the number tom times the quiz has been taken. This functionality                      #
lets more users take the same quiz as a small game.                                             #
                                                                                                #
Option 3 exits the program.                                                                     #    
-------------------------------------------------------------------------------------------------
"""


# user checking is the function that runs the program
def user_checkin():
    while True:
        print("-" * 30)
        print("Login to user account")
        usr = input("Enter account name: ")
        password = input("Enter password: ")
        result = login_info(usr, password)

        if result:
            print("[+] Valid Username\n")
            print("Welcome, ", usr.upper())
            handle_menu()
            break
        else:
            print("[-] Invalid username, Try Again\n")


## Login info stores the password in dictionary
def login_info(usr, password):
    user_dict = {
        "PGR107": "Python"
    }
    stored = user_dict.get(usr.upper())
    if stored and stored == password:
        return True
    else:
        return False


# ============================================================================== #
"""
------------------
Menu Function    #
------------------
"""


# Menu options stored in a list
def handle_menu():
    menu_options = [
        "\n" + ("-" * 15),
        "1. Play Quiz",
        "2. Show Results",
        "3. Exit",
        ("-" * 15) + "\n"
    ]

    # List that stores the score.
    scores = []
    while True:
        for opt in menu_options:
            print(opt)
        # choices
        choice = input("Enter your choice: ")

        # choice Play quiz
        if choice == "1":

            print("Info: Press A, B, C or D on your keyboard")
            game_results = handle_quiz()
            if game_results != 0:
                scores.append(game_results)

        # Show results and scores
        elif choice == "2":
            if not scores:
                print("No scores available. Play a round first!\n")
            else:
                print("\nScores:")
                for i, score in enumerate(scores):
                    print(f"Game {i + 1}: {score}")
                print(f"\nHighest score: {max([int(score.split('/')[0]) for score in scores])}/10\n")

        # Exit program
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("\nInvalid choice please try again")


# =========================================================================================================== #

"""
--------------
Quiz function 
--------------
"""


def handle_quiz():
    quiz_set = quiz_repo()
    valid_choices = ['a', 'b', 'c', 'd']
    points = 0
    responses = []
    choices_str = ""

    for quiz in quiz_set:

        for Qid, trivia in quiz.items():
            quiz_id = Qid
            question = trivia['question']
            choices = trivia['choices'].items()
            answer = trivia['answer']

            print("-" * len(question + Qid))
            print(f"{Qid}: {question}")

            for k, v in choices:
                choices_str += f"{k}. {v}\t"
                print(f"\t{k}.\t{v}")

            print("-" * len(question + Qid))

            while True:
                choice = input("Enter your choice: ").strip().lower()

                if choice != "" and choice in valid_choices:
                    if choice == answer:
                        points += 1

                    responses.append({"\r\n" + f'{quiz_id}: ': question,
                                      'Choice: ': choices_str,
                                      'Answer: ': f"Correct, {answer}."
                                      if choice == answer
                                      else f"Wrong, correct answer is {answer}.\nYou Choose {choice}."})

                    choices_str = ""  # empty the placeholder for next question
                    break

                else:
                    print("Invalid choice, please enter a, b, c or d")

    result_points = points
    result_score = f"{result_points}/10"
    print("-" * 80)
    print("QUIZ RESULTS")
    handle_results(responses, result_points, result_score)
    return result_score


# ================================================================================================ #
"""
--------------------------------
Quiz questions stored in a list
--------------------------------
"""


def quiz_repo():
    repo = [
        {"Q1": {'question': "What is the capital of Norway?",
                'choices': {'a': 'Bergen', 'b': 'Oslo', 'c': 'Stavanger', 'd': 'Trondheim'},
                'answer': 'b'}},
        {"Q2": {'question': "What is the currency of Norway?",
                'choices': {'a': 'Euro', 'b': 'Pound', 'c': 'Kroner', 'd': 'Deutsche Mark'},
                'answer': 'c'}},
        {"Q3": {'question': "What is the largest city in Norway?",
                'choices': {'a': 'Oslo', 'b': 'Stavanger', 'c': 'Bergen', 'd': 'Trondheim'},
                'answer': 'a'}},
        {"Q4": {'question': "When is constitution day (the national day) of Norway?",
                'choices': {'a': '27th May', 'b': '17th May', 'c': '17th April', 'd': '27th April'},
                'answer': 'b'}},
        {"Q5": {'question': "What color is the background of the Norwegian flag?",
                'choices': {'a': 'Red', 'b': 'White', 'c': 'Blue', 'd': 'Yellow'},
                'answer': 'a'}},
        {"Q6": {'question': "How many countries does Norway border?",
                'choices': {'a': '1', 'b': '2', 'c': '3', 'd': '4'},
                'answer': 'c'}},
        {"Q7": {'question': "What is the name of the university in Trondheim?",
                'choices': {'a': 'UiS', 'b': 'UiO', 'c': 'NMBU', 'd': 'NTNU'},
                'answer': 'd'}},
        {"Q8": {'question': "How long is the border between Norway and Russia?",
                'choices': {'a': '96 km', 'b': '196 km', 'c': '296 km', 'd': '396 km'},
                'answer': 'b'}},
        {"Q9": {'question': "Where in Norway is Stavanger?",
                'choices': {'a': 'North', 'b': 'South', 'c': 'South-west', 'd': 'South-east'},
                'answer': 'c'}},
        {"Q10": {'question': "From which Norwegian city did the world’s famous composer Edvard Grieg come from?",
                 'choices': {'a': 'Oslo', 'b': 'Bergen', 'c': 'Stavanger', 'd': 'Tromsø'},
                 'answer': 'b'}},
    ]
    return repo


# ================================================================================================================ #
"""
-----------------------------------------------------------
Printing Results after the quiz and quiz score 
which is stored to compare scores after repeating the quiz
-----------------------------------------------------------
"""


def handle_results(results, result_points, result_score):
    if results:
        for result in results:
            for k, v in result.items():
                print(k, v)
        print("-" * 100)
        print("Scores")
        print(f"\r\nYou got {result_points} out of {len(results)} correct\r\n")
        print(f"Score: {result_score}\r\n")


user_checkin()

# =============================== END OF PROGRAM ================================================ #
