import requests
import random
import os
from Live import BaseGame


class CurrencyRoulleteGame(BaseGame):
    def __init__(self, difficulty):
        super().__init__(difficulty, 'CurrencyRoulleteGame')

    def get_money_interval(self, ils):
        self.result = (ils-(5-self.difficulty), ils+(5-self.difficulty))

    @staticmethod
    def get_guess_from_user(usd):
        guess_value = input(f"What do you think is the value of {usd}$ generated to ILS? ")
        while guess_value.isdigit() is False:
            guess_value = input(f"What do you think is the value of {usd}$ generated to ILS? ")
        return guess_value

    def compare_guess(self):
        min_interval, max_interval = self.result
        if min_interval < self.guess < max_interval:
            self.win = True

    def play(self):
        api_key = os.environ['API_KEY']
        currency_api = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
        currency_rate = requests.get(currency_api).json()["conversion_rates"]["ILS"]
        usd = random.randint(1, 100)
        ils = usd*currency_rate
        self.get_money_interval(ils=ils)
        self.guess = float(self.get_guess_from_user(usd))
        self.compare_guess()
        self.print_result()
        return self.win

