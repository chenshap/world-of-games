from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRoulleteGame
from GuessGame import GuessGame
from Score import add_score
from MainScores import app
def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG) \n"
           f"Here you can find many cool games to play")


def load_game():
    choosen_game = input("Please choose a game to play:\n"
                         "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n"
                         "2. Guess Game - guess a number and see if you choose like the computer \n"
                         "3. Currency Roulette - try and guess the value of random amount of USD in ILS\n"
                         "please choose a game from 1 to 3: ")
    while choosen_game.isdigit() is False or int(choosen_game) < 1 or int(choosen_game) > 3:
        choosen_game = input("Please choose a game to play:\n"
                             "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n"
                             "2. Guess Game - guess a number and see if you choose like the computer \n"
                             "3. Currency Roulette - try and guess the value of random amount of USD in ILS\n"
                             "please choose a game from 1 to 3: ")
    difficulty = input("Please choose game difficulty from 1 to 5: ")
    while difficulty.isdigit() is False or int(difficulty) < 1 or int(difficulty) > 5:
        difficulty = input("Please choose game difficulty from 1 to 5: ")
    difficulty = int(difficulty)
    choosen_game = int(choosen_game)
    if choosen_game == 1:
        game =  MemoryGame(difficulty)
    elif choosen_game == 2:
        game =  GuessGame(difficulty)
    elif choosen_game == 3:
        game =  CurrencyRoulleteGame(difficulty)
    game.welcome_game()
    win = game.play()
    if win is True:
        add_score(difficulty)
        app.run()



if __name__ == '__main__':
    welcome("Guy")
    game = load_game()



