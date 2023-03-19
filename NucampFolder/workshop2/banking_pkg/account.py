

# format currency
def format_currency(bal):
    '''
    format float to currency string
    '''
    return f"${bal:,.2f}"


def show_balance(balance):
    '''Print balance'''

    balance = float(balance)
    format_currency(balance)
    print(f"Your current balance is: ${balance}")


def deposit(balance):
    '''Make a deposit'''

    deposit_amount = input("Enter amount to deposit: ")
    balance = float(deposit_amount) + balance
    show_balance(balance)
    return balance

def withdraw(balance):
    '''Withdraw money'''

    withdraw_amount = input("Enter amount to withdraw: ")
    
    if balance < float(withdraw_amount):

        show_balance(balance)
        print("You have no money!")
        choice = input("Do you want to make a deposit? (Y/N) ").lower()

        if choice == "y":
            return deposit(balance)
            
        else:
            show_balance(balance)
            return balance
    else:
        balance = balance - float(withdraw_amount)
        show_balance(balance)
        return balance

def logout(name):
    '''Logout '''
    
    print(f"Goodbye {name.title()}!")
    quit()








