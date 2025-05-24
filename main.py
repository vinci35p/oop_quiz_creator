import os
from quiz_compiler import QuizCompiler
from quiz_executor import QuizExecutor
from colorama import Fore

# Class for the main program
class MainQuizTaker:
    def __init__(self, filename="quiz_text"):
        self.filename = filename
        self.compiler = QuizCompiler(filename)
        self.executor = QuizExecutor(filename)

# Function to delete the quiz file
    def delete_quiz_file(self):
        try:
            os.remove(self.filename)
            print(Fore.GREEN + f"Deleted existing quiz file '{self.filename}'.")
        except FileNotFoundError:
            print(Fore.YELLOW + "No existing quiz file to delete.")

# Function that let users choose to add or create new set of questions
    def create_or_add_questions(self, mode):
        if mode == '1':
            self.delete_quiz_file()
            self.compiler = QuizCompiler(self.filename)
        self.compiler.run()

# Function to run and start the main program segment
    def start(self):
        while True:
            print(Fore.CYAN + "Welcome to your own quiz creator!\n")
            user_decision = input(Fore.LIGHTBLUE_EX +
                                  "Enter '1' to create a new quiz, '2' to add questions, or '3' to quit: ")
            if user_decision not in ['1', '2', '3']:
                print(Fore.RED + "Invalid input. Please enter '1', '2', or '3'.")
                continue

            if user_decision == '3':
                print(Fore.LIGHTGREEN_EX + "Goodbye!")
                break

            self.create_or_add_questions(user_decision)

        # After creation or adding, ask if user wants to take the quiz
        while True:
            user_choice = input(Fore.YELLOW + "Would you like to take the quiz now? (Y/N): ").strip().upper()
            if user_choice not in ['Y', 'N']:
                print(Fore.RED + "Invalid input. Enter 'Y' or 'N'.")
                continue

            if user_choice == 'N':
                print(Fore.LIGHTGREEN_EX + "Exiting. Have a nice day!")
                break

            if user_choice == 'Y':
                if not self.executor.questions:
                    print(Fore.MAGENTA + "No quiz questions found. Please create questions first.")
                    break

                while True:
                    self.executor.execute_quiz(self.executor.questions)
                    retry = input(Fore.GREEN + "Do you want to take the quiz again? (Y/N): ").strip().upper()
                    if retry not in ['Y', 'N']:
                        print(Fore.RED + "Invalid input. Enter 'Y' or 'N'.")
                        continue
                    if retry == 'N':
                        print(Fore.GREEN + "Returning to main menu.")
                        break

# __QUIZ_GENERATOR__
if __name__ == "__main__":
    function = MainQuizTaker()
    function.start()