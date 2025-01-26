from coins import INTLGNTcoin, Stupidcoin
from market import Market
import random

def main():
    market = Market()
    days_to_simulate = 30

    for day in range(days_to_simulate):
        market_values = market.simulate_day()
        print(f"Day {day + 1}:")
        print(f"  {market.intelligent_coin.name}: {market_values['intelligent']:.2f}")
        print(f"  {market.stupid_coin.name}: {market_values['stupid']:.2f}")
        if random.random() < 0.1:  # 10% chance of a meme pump event
            market.meme_pump()
        print()

    # Hidden Easter egg - run this on April Fools' Day
    if __name__ == "__main__" and datetime.datetime.now().month == 4 and datetime.datetime.now().day == 1:
        print("April Fools! Your Stupidcoin is now worth... nothing!")

if __name__ == "__main__":
    main()