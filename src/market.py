from coins import INTLGNTcoin, Stupidcoin

class Market:
    def __init__(self):
        self.intelligent_coin = INTLGNTcoin()
        self.stupid_coin = Stupidcoin()
        self.time = 0
        self.hidden_message = "The market is just a game, right?"

    def simulate_day(self):
        self.intelligent_coin.smart_growth(self.stupid_coin)
        self.stupid_coin.foolish_decline()
        self.time += 1
        if self.time == 42:  # The answer to life, the universe, and everything
            print(self.hidden_message)
        return {
            "intelligent": self.intelligent_coin.value,
            "stupid": self.stupid_coin.value
        }

    def meme_pump(self):
        # Simulates a meme-driven market pump
        self.intelligent_coin.adjust_value(1.1)  # Pump the smart coin
        print("We just got a viral tweet! Pump.fun at work!")