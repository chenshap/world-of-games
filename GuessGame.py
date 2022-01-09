import random
from Live import BaseGame

class GuessGame(BaseGame):
    def __init__(self, difficulty):
        super().__init__(difficulty, 'GuessGame')

    def generate_number(self):
        self.result = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        self.guess = input(f"please choose a number between 1 to {self.difficulty}: ")
        while self.guess.isdigit() is False or int(self.guess) < 1 or int(self.guess) > self.difficulty:
            self.guess = input(f"please choose a number between 1 to {self.difficulty}: ")
        return int(self.guess)

    def compare_guess(self):
        if self.guess == self.result:
            self.win = True

    def play(self):
        self.get_guess_from_user()
        self.generate_number()
        self.compare_guess()
        self.print_result()
        return self.win

