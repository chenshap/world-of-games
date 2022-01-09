import random
import time
from Live import BaseGame
from Utils import clear

class MemoryGame(BaseGame):
    def __init__(self, difficulty):
        super().__init__(difficulty, 'MemoryGame')

    def generate_sequence(self):
        gen_lis = []
        while len(gen_lis) < self.difficulty:
            gen_lis.append(random.randint(1, 101))
        return gen_lis

    @staticmethod
    def convert_to_list(user_input):
        return user_input.split()

    def compare_guess(self):
        if self.guess == self.result:
            self.win = True

    def play(self):
        self.result = self.generate_sequence()
        enter_game = input("please try to remember the sequence of numbers,"
                           " they will be displayed only for 0.7 sec, press ENTER to start: ")
        while enter_game != "":
            enter_game = input("welcome to the Memory Game, please try to remember the sequence of numbers,"
                               " they will be displayed only for 0.7 sec, press ENTER to start: ")
        print(self.result)
        time.sleep(0.7)
        clear()
        user_input = input(f"what was the sequence that was just displayed (numbers between 1 to 101)"
                           f" Enter elements of a list separated by comma : ")
        self.guess = list(map(int, user_input.strip().split(',')))[:self.difficulty]

        self.compare_guess()

        self.print_result()
        return self.win
