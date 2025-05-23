import sys
import time
import random
import os
from colorama import Fore

class QuizExecutor:
    def __init__(self):

    def execute_quiz(self, question_list): # Print the questions randomly then let the user answer every rambled question
        score = 0
        total = len(question_list)
        quiz = random.sample(question_list, total)

        for num, question_list in enumerate(quiz, 1):
            print(f"\n{question_list['question']}")
            for choice in question_list['choices']:
                print(choice)

            while True:
                user_ans = input("Enter your answer (A, B, C, or D): ").strip().upper()
                if user_ans in ['A', 'B', 'C', 'D']:
                    break
                else:
                    print("Invalid input. Please enter a viable answer (A, B, C, or D).")

            if user_ans == question_list["answer"]:
                self.loading_animation_right_answer()
                score += 1

            else:
                self.loading_animation_wrong_answer()

        print(Fore.LIGHTYELLOW_EX + f"\nYou got {score} out of {total}.\n")

    def delete_quiz_file(self, quiz_txt):
        try:
            os.remove(quiz_txt)
            print(f"\nQuiz file '{quiz_txt}' has been deleted.\n")
        except FileNotFoundError:
            print(f"\nQuiz file '{quiz_txt}' not found, there's nothing to delete.\n")

    def loading_animation_right_answer(self):
        print(Fore.LIGHTRED_EX + "Hmmm", end='')
        for _ in range(3):
            sys.stdout.write(Fore.RED + ".")
            sys.stdout.flush()
            time.sleep(0.75)
        print(Fore.YELLOW + "\nYou got it!")
        print()

    def loading_animation_wrong_answer(self):
        print(Fore.LIGHTRED_EX + "Hmmm", end='')
        for _ in range(3):
            sys.stdout.write(Fore.RED + ".")
            sys.stdout.flush()
            time.sleep(0.75)
        print(Fore.YELLOW + "\nYou didn't got it... Keep it up!")
        print()
