from coins import INTLGNTcoin, Stupidcoin
from market import Market
import random
import time

ascii_logo = r"""
   /$$$$$$ /$$   /$$ /$$$$$$$$ /$$        /$$$$$$  /$$   /$$ /$$$$$$$$                            
  |_  $$_/| $$$ | $$|__  $$__/| $$       /$$__  $$| $$$ | $$|__  $$__/                            
    | $$  | $$$$| $$   | $$   | $$      | $$  \__/| $$$$| $$   | $$                               
    | $$  | $$ $$ $$   | $$   | $$      | $$ /$$$$| $$ $$ $$   | $$                               
    | $$  | $$  $$$$   | $$   | $$      | $$|_  $$| $$  $$$$   | $$                               
    | $$  | $$\  $$$   | $$   | $$      | $$  \ $$| $$\  $$$   | $$                               
   /$$$$$$| $$ \  $$   | $$   | $$$$$$$$|  $$$$$$/| $$ \  $$   | $$                               
  |______/|__/  \__/   |__/   |________/ \______/ |__/  \__/   |__/                               
                                                                                                
                                                                                                
                                                                                                
    /$$$$$$  /$$$$$$ /$$      /$$ /$$   /$$ /$$        /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$$       
   /$$__  $$|_  $$_/| $$$    /$$$| $$  | $$| $$       /$$__  $$|__  $$__//$$__  $$| $$__  $$      
  | $$  \__/  | $$  | $$$$  /$$$$| $$  | $$| $$      | $$  \ $$   | $$  | $$  \ $$| $$  \ $$      
  |  $$$$$$   | $$  | $$ $$/$$ $$| $$  | $$| $$      | $$$$$$$$   | $$  | $$  | $$| $$$$$$$/      
   \____  $$  | $$  | $$  $$$| $$| $$  | $$| $$      | $$__  $$   | $$  | $$  | $$| $$__  $$      
  /$$  \ $$  | $$  | $$\  $ | $$| $$  | $$| $$      | $$  | $$   | $$  | $$  | $$| $$  \ $$      
 |  $$$$$$/ /$$$$$$| $$ \/  | $$|  $$$$$$/| $$$$$$$$| $$  | $$   | $$  |  $$$$$$/| $$  | $$      
  \______/ |______/|__/     |__/ \______/ |________/|__/  |__/   |__/   \______/ |__/  |__/
"""

# List of dramatic, extreme, funny, and random outcomes
easter_egg_messages = [
    "INTLGNTcoin just got listed on Coinbase! 🚀 Moonshot incoming!",
    "Stupidcoin has been declared the official currency of Mars by Elon Musk. Aliens love it!",
    "INTLGNTcoin holders just got airdropped DogeNFTs! Your portfolio is now 100% more memeable!",
    "Oops! Your Stupidcoin investment accidentally funded a crypto pyramid scheme. You're now a 'marketing executive'.",
    "INTLGNTcoin has been forked into SmartestCoin! Your INTLGNTcoin is now worth... 2x more!",
    "A quantum computer just solved blockchain, making all your coins... obsolete.",
    "You've accidentally donated all your INTLGNTcoin to a charity for lost crypto keys. Feel good about it!",
    "Stupidcoin has been accepted as legal tender in the metaverse. You're rich... in virtual reality!",
    "Your INTLGNTcoin wallet was mistaken for a time capsule. Archaeologists are puzzled.",
    "INTLGNTcoin just partnered with NASA for space mining. Your investment is literally out of this world!",
    "Stupidcoin's value increased because everyone thought it was a new slang term for 'cool'.",
    "Your INTLGNTcoin investment has been turned into a movie plot. You're now a Hollywood producer!",
    "A glitch in the matrix made Stupidcoin briefly overtake Bitcoin. You're rich for 15 minutes.",
    "INTLGNTcoin just got used to buy a small country. You're now a geopolitical influencer!",
    "Your Stupidcoin wallet was hacked by a cat. The cat is now a crypto millionaire.",
    "INTLGNTcoin's new whitepaper is written in emoji. Your investment is now more expressive!",
    "Stupidcoin has been adopted as the currency for a new reality TV show. Drama increases its value!",
    "Your INTLGNTcoin investment just funded the world's first AI-run crypto exchange. AI says 'Thank you!'",
    "Stupidcoin's value crashed after a tweet from a famous parrot. Never trust birds with your investments."
]

def main():
    # Print the ASCII logo with a delay for each line
    for line in ascii_logo.split('\n'):
        print(line)
        time.sleep(0.5)  # Adjust this delay as needed

    market = Market()
    days_to_simulate = 7  # Changed to simulate only 7 days

    for day in range(days_to_simulate):
        market_values = market.simulate_day()
        print(f"Day {day + 1}:")
        time.sleep(0.5)  # Small pause after day number
        print(f"  {market.intelligent_coin.name}: {market_values['intelligent']:.2f}")
        time.sleep(0.5)  # Small pause after first coin value
        print(f"  {market.stupid_coin.name}: {market_values['stupid']:.2f}")
        time.sleep(0.5)  # Small pause after second coin value
        if random.random() < 0.3:  # 30% chance of a meme pump event
            market.meme_pump()
        print()
        time.sleep(0.5)  # Small pause after each day's output for readability

    # Random Easter egg message with a slight delay
    if random.random() < 0.6:  # 60% chance to trigger an Easter egg message
        print(random.choice(easter_egg_messages))
        time.sleep(0.5)  # A bit longer pause after the Easter egg message for dramatic effect

if __name__ == "__main__":
    main()