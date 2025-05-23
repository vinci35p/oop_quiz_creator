import sys
import time
import random
import os
from colorama import Fore

# Class to execute the quiz from the collected quiz file
class QuizExecutor:
    def __init__(self, filename="quiz_text"):
        self.filename = filename
        self.questions = self.read_txt_file()


    def read_txt_file(self):
        if not os.path.exists(self.filename):
            print(Fore.RED + f"Quiz file '{self.filename}' not found.")
            return []

        with open(self.filename, "r") as collected_file:
            file_txt = collected_file.read().strip()

        solo_quests = file_txt.split("\n\n")
        question_list = []

        for solo_quest in solo_quests:
            lines = solo_quest.strip().split("\n")
            if len(lines) >= 6:
                quest_part = lines[0]
                choices_part = lines[1:5]
                answer_part = lines[5]
                answer_key = answer_part.split(":")[-1].strip()
                question_list.append({
                    "question": quest_part,
                    "choices": choices_part,
                    "answer": answer_key
                })

        return question_list

    # Print the questions randomly then let the user answer every rambled question
    def execute_quiz(self, question_list):
        if not self.questions:
            print(Fore.RED + "No questions available. Please create some first.")
            return

        score = 0
        total = len(self.questions)
        quiz = random.sample(self.questions, total)

        for num, question in enumerate(quiz, 1):
            print(f"\n{question['question']}")
            for choice in question['choices']:
                print(choice)

            while True:
                user_ans = input("Enter your answer (A, B, C, or D): ").strip().upper()
                if user_ans in ['A', 'B', 'C', 'D']:
                    break
                else:
                    print("Invalid input. Please enter a viable answer (A, B, C, or D).")

            if user_ans == question["answer"]:
                self.loading_animation_right_answer()
                score += 1

            else:
                self.loading_animation_wrong_answer()

        print(Fore.LIGHTYELLOW_EX + f"\nYou got {score} out of {total}.\n")

    def delete_quiz_file(self):
        try:
            os.remove(self.filename)
            print(f"\nQuiz file '{self.filename}' has been deleted.\n")
        except FileNotFoundError:
            print(f"\nQuiz file '{self.filename}' not found, there's nothing to delete.\n")

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
        print(Fore.YELLOW + "\nYou didn't get it... Keep it up!")
        print()
