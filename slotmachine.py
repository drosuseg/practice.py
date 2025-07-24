import random

def spin_row():
    symbols = ['🍒','🍉', '🍌', '🍋', '🙉','⭐']

    results = []
    for symbol in range(3):
       results.append(random.choice(symbols))
    return results

def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def get_payout(row,bet):
   if row [0] == row [1] == row[2]:
    if row [0] == '🍒':
       return bet * 3
    elif row [0] == '🍉':
       return bet * 4
    elif row [0] == '🍌':
       return bet * 5
    elif row [0] == '🍋':
       return bet * 6
    elif row [0] == '🙉':
       return bet * 7
    elif row [0] == '⭐':
       return bet * 8
   return 0

is_running = True 

def main():
    balance = 100

    print("+++++++++++++++++++++++++++")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍌 🍋 🙉 ⭐")
    print("++++++++++++++++++++++++++")

    while balance > 0 :
     print(f"Current balance: {balance}")
     bet = input("Place your bet amount: ")

     if not bet.isdigit():
      print("Pls enter a valid number.")
      continue

     bet = int(bet)

     if bet >= balance:
        print("Insufficient funds")
        continue
     
     if bet <= 0:
        print("Bet must be a greater than 0")

     balance -= bet

     row = spin_row()
     print("Spinning...")
     print_row(row)
    
     payout = get_payout(row,bet)
     if payout > 0:
      print(f"You won {payout}")
     else:
      print("Sorry, you lost this round")
        
     balance += payout

     while True: 
        play_again = input("Do you want to play again (Y/N): ").strip().upper()

        if play_again == 'Y':
            break 
        elif play_again == 'N':
            print("Thanks for playing! Goodbye.")
            return
        else:
            print("Invalid input. Please enter Y or N.")

print("\nGame over! Your final balance is: {balance}.")

if __name__ == '__main__':
 main()