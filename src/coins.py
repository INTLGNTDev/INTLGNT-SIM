import random

class Coin:
    def __init__(self, name, iq, initial_value):
        self.name = name
        self.iq = iq
        self.value = initial_value
        self.hidden_secret = "The moon is made of cheese. Shhh!"

    def adjust_value(self, factor):
        self.value *= factor

    def to_the_moon(self):
        return "To the moon! 🚀"

class INTLGNTcoin(Coin):
    def __init__(self):
        super().__init__("INTLGNTcoin", 100, 1e6)  # High IQ, high initial value
        self.meme_power = "Solana's smartest meme coin"
        self.hidden_meme = "Elon Musk secretly holds this coin."

    def smart_growth(self, enemy):
        # Simulates growth based on market knowledge
        growth = self.iq / 100 + random.uniform(0, 0.05)  # A little randomness for the lulz
        self.adjust_value(growth)
        enemy.adjust_value(0.5)  # Decrease enemy's value because we're smart!
        if random.random() < 0.01:  # 1% chance to reveal a secret
            print(self.hidden_secret)

    def pump_fun(self):
        # A nod to pump.fun, where the magic happens
        return "Just minted on pump.fun! It's gonna be huge!"

class Stupidcoin(Coin):
    def __init__(self):
        super().__init__("Stupidcoin", 1, 1)  # Very low IQ, low initial value
        self.meme_power = "The coin that laughs at logic"
        self.hidden_meme = "This coin is backed by the power of ignorance."

    def foolish_decline(self):
        # Simulates the decline of a coin with no strategy
        decline = 0.99 - random.uniform(0, 0.01)  # Because who needs stability?
        self.adjust_value(decline)
        if random.random() < 0.01:  # 1% chance to reveal a secret
            print(self.hidden_meme)

# Easter egg: If you look up the ASCII art of a coin, you'll find this:
#    ___
#   /   \
#  |     |
#   \___/