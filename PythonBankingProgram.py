print("Python Banking Program\n", "********************")

# FUNCTIONS
def show_balance(balance): # 1 PARAMETER
    print(f"Your balance is : $ {balance:.2f} ")

def deposit():
    amount = float(input("Enter an amount to be deposited: ")) # LOCAL VARIABLE & TYPECAST THE STRING

    if amount < 0:
        print("\033[1;31m", "That is not a valid amount!", "\033[0m")
        return 0
    else:
        return amount

def withdraw(balance): # 1 PARAMETER
    amount = float(input("Enter amount to be withdrawn: ")) # LOCAL VARIABLE & TYPECAST THE STRING

    if amount > balance:
        print("Insufficient funds!")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount


#MAIN FUNCTION
def main():
    balance = 0 #  VARIABLE
    is_running = True # VARIABLE

    while is_running:
        print("******************")
        print("Banking Program")
        print("1. Show Balance")
        print("2. Make A Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("******************")
        choice = input("Enter your choice (1-4): ") # VARIABLE

        if choice == '1': #STRING DATA TYPE
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("\033[1;31m", "That is not a valid choice! 😭", "\033[0m")

    print("Thank you for choosing Python Banking Program! Have a great day 🌞")


# DUNDER MAIN:  It Allows You to Execute Code When the File Runs as a Script,
# BUT Not When It’s Imported as a Module
if __name__ == '__main__':
    main()
