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

# Function that let users choose to add or create new set of questions

# __QUIZ_GENERATOR__