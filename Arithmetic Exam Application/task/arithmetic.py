# write your code here
from random import randint, choice
import os


class Calculator:
    def __init__(self):
        self.difficulty = None
        self.level_descriptions = ["simple operations with numbers 2-9", "integral squares of 11-29"]
        self.choose_difficulty()
        self.task_generator = Calculator.TaskGenerator()
        self.user_answer = None
        self.correct_result = None
        self.correct_answers = 0
        self.exam()
        self.give_mark()
        self.save_result()

    def choose_difficulty(self):
        print("Which level do you want? Enter a number:")
        print(f"1 - {self.level_descriptions[0]}")
        print(f"2 - {self.level_descriptions[1]}")
        while True:
            try:
                self.difficulty = int(input())
                if self.difficulty in [1, 2]:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Incorrect format.")
                continue

    def get_input(self):
        while True:
            try:
                self.user_answer = int(input())
                break
            except ValueError:
                print("Incorrect format.")
                continue

    def calculate(self):
        self.correct_result = eval(self.task_generator.task)

    def evaluate_answer(self):
        if self.user_answer == self.correct_result:
            self.correct_answers += 1
            print("Right!")
        else:
            print("Wrong!")

    def exam(self):
        for i in range(5):
            self.task_generator.generate(self.difficulty)
            self.get_input()
            self.calculate()
            self.evaluate_answer()

    def give_mark(self):
        print(f"Your mark is {self.correct_answers}/5.")

    def save_result(self):
        answer = input("Would you like to save your result to the file? Enter yes or no.")
        if answer in ["yes", "YES", "y", "Yes"]:
            user_name = input("What is your name?")
            to_write = f"{user_name} {self.correct_answers}/5 in level {self.difficulty} ({self.level_descriptions[self.difficulty - 1]})"
            if os.path.isfile("results.txt"):
                with open("results.txt", "a") as file:
                    file.write(to_write)
            else:
                with open("results.txt", "w") as file:
                    file.write(to_write)
            print('The results are saved in "results.txt".')
        else:
            exit()

    class TaskGenerator:
        def __init__(self):
            self.operands = []
            self.operator = ""
            self.task = ""

        def generate(self, difficulty):
            if difficulty == 1:
                self.task = f'{randint(2, 9)} {choice("+-*")} {randint(2, 9)}'
                print(self.task)
            elif difficulty == 2:
                self.task = f'{randint(11, 29)} ** 2'
                print(self.task[:2])


calculator = Calculator()
