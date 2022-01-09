
class BaseGame:
    def __init__(self, difficulty, game_name):
        self.difficulty = difficulty
        self.game_name = game_name
        self.result = None
        self.guess = None
        self.win = False

    def welcome_game(self):
        print("Welcome to the", self.game_name)

    def play(self):
        pass

    def compare_guess(self):
        pass

    def print_result(self):
        print(f"Your guess was {self.guess} while the result was {self.result}")
        if self.win is True:
            print(f"Congratulations, you won the {self.game_name}")
        elif self.win is False:
            print(f"Such a shame, you lost the {self.game_name}")








