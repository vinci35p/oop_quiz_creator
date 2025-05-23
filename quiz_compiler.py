import sys
import time
from colorama import Fore

# Class to compile the quiz from user
class QuizCompiler:
    def __init__(self, filename="quiz_text", datafile="collected_data.txt"):
        self.filename = filename
        self.datafile = datafile
        self.question_num = self.starting_num() + 1
        self.file = open(self.filename, "a")

    # Numbering of questions
    def starting_num(self):
        try:
            with open(self.datafile, "r") as collected_data_file:
                lines = collected_data_file.readlines()
                return sum(1 for line in lines if line.startswith("Question: " or line[0].isdigit()))
        except FileNotFoundError:
            return 0

    # Input question
    def question(self):
        return input(Fore.CYAN + "\nEnter your preferred question: ")

    # Input choices
    def quest_choices(self):
        choices = {}
        for letter in ['A', 'B', 'C', 'D']:
            choices[letter] = input(Fore.BLUE + f"Enter choice {letter} : ")

        return choices

    # Input correct answer
    def answer(self):
        user_ans = str(
            input(Fore.LIGHTBLUE_EX + "\nEnter the correct answer (A,B,C,D) from provided question: ")).upper()
        while user_ans not in ["A", "B", "C", "D"]:
            user_ans = input(Fore.RED + "Invalid input. Please enter A, B, C, or D: ").upper()

        return user_ans

    # Loading text after questions, choices and answers are inputted
    def loading_animation(self):
        print(Fore.LIGHTRED_EX + "Saving your question", end='')
        for _ in range(3):
            sys.stdout.write(Fore.RED + ".")
            sys.stdout.flush()
            time.sleep(0.75)
        print(Fore.YELLOW + "\nSaved successfully! Check your text file to see your inputted values.")
        print()

    def run(self):
        while True:
            print(Fore.LIGHTYELLOW_EX + "Enter your question!")
            while True:
                choice = str(input(Fore.YELLOW + "Enter '7' to exit. Enter '1' to continue: "))
                if choice in ['1', '7']:
                    break

                else:
                    print(Fore.RED + "Invalid input. Enter just number '1' to continue, and '7' to exit\n")

            if choice == '1':
                questions = self.question()
                choices = self.quest_choices()
                answers = self.answer()

                self.loading_animation()

                self.file.write(f"{self.question_num}. Question: {questions}\n")
                for letter in ['A', 'B', 'C', 'D']:
                    self.file.write(f"{letter}. {choices[letter]}\n")
                self.file.write(f"Correct Answer: {answers}\n\n")

                self.question_num += 1

            elif choice == '7':
                print(Fore.MAGENTA + "Exiting, have a nice day!\n")
                self.file.close()
                break


