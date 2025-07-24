def show_balance():
    print(F"Your balance is : {balance:.2f}")

def deposit():
   amount = float(input("Enter amount deposited: "))

   if amount<0:
       print("Thats not a valid amount")
       return 0
   else:
       return amount
   
def withdraw():
    amount = float(input(f"Enter an amount to withdraw : "))

    if amount > balance:
        print ("Insuficient amount.")
        return 0
    elif amount < 0:
        print("Amount must be greter then zero")
        return 0
    else:
        return amount

balance = 0
is_running = True

while is_running:
    print("==Banking Program==")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter your choice 1 to 4: ")

    if choice == '1':
        show_balance()
    elif choice =='2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Not a valid choice.")

print("Thank you have a nice day")    