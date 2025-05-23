from quiz_compiler import QuizCompiler
from quiz_executor import QuizExecutor

# ---- MAIN QUIZ ----
file = 'quiz_txt'

quiz_questions = read_txt_file(file)

while True:
    print(Fore.CYAN + "Welcome to your own quiz creator!\n")
    while True:
        user_decision = str(input(Fore.LIGHTBLUE_EX + "Enter '1' if you want to create a new set of questionnaires, '2' if you just want "
                              "to add questions, and '3' if you don't want to continue: "))

        if user_decision in ['1', '2', '3']:
            break

        else:
            print(Fore.RED + "Invalid input. Enter just '1', '2' or '3'.")

    if user_decision == '1':
        delete_quiz_file(file)
        compiler_quiz()

    if user_decision == '2':
        compiler_quiz()

    if user_decision == '3':
        break

while True:
    print(Fore.YELLOW + "\nDo you like to take the quiz now?")

    while True:
        user_choice = str(input(Fore.LIGHTRED_EX + "Enter your choice (Y/N): ")).strip().upper()

        if user_choice in ['Y','N']:
            break
        else:
            print(Fore.RED + "Invalid input, enter 'Y' or 'N'.")

    if user_choice == 'Y':
        quiz_questions = read_txt_file(file)
        if not quiz_questions:
            print(Fore.MAGENTA + "No quiz questions found. Please create questions first.")
            break
        else:
            retry = 'Y'
            while retry == 'Y':
                execute_quiz(quiz_questions)
                while True:
                    retry = str(input(Fore.GREEN + "Do you want to take the quiz again? (Y/N): "))
                    if retry in ['Y', 'N']:
                        break
                    else:
                        print(Fore.RED + "Invalid input. Enter 'Y' or 'N'.")
            print(Fore.GREEN + "Returning to main query.")


    if user_choice == 'N':
        print(Fore.LIGHTGREEN_EX + "\nExiting, have a nice day!")
        break
