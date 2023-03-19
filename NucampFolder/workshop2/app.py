'''
ATM Project
By Tierry Veras
03/11/2023
'''

from banking_pkg import account

def main():
    '''Main function'''

    print("          === Automated Teller Machine ===          ")
    name = name_func()
    pin = pin_func()
    current_balance = 0
    print(f"{name.title()} has been registered with a starting balance of ${current_balance}")
    login_validation(name,pin)
    menu(current_balance,name)


def atm_menu(name):
    '''ATM Menu'''

    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")




def name_func():
    '''Validates user's name'''    
    while True:
        name = input("Enter name to register: ").lower()
        name_len = len(name)
        if name_len > 10:
            print("The maximum name length is 10 characters.")
            continue
        if name_len <= 0:
            print("Please enter at least one character.")
            continue
        else: 
            return name
             
def pin_func():
    '''Validates user's pin'''

    while True:
        pin = input("Enter PIN: ")
        pin_len = len(pin)
        if pin_len != 4:
            print("PIN must contain 4 number")
            continue
        else:
            return pin
    

 
def login_validation(_name, _pin):
    '''Login function'''

    while True:
        print("\n          === Automated Teller Machine ===          ")
        print("LOGIN")
        name_to_validate = input("Enter name: ").lower()
        pin_to_validate = input("Enter PIN: ")

        if name_to_validate == _name and pin_to_validate == _pin:
            print("Login successful!")
            break
        else:
            print("Invalid credentials!")
            continue

def menu(balance,_name):
    '''User's account menu'''

    while True:
    
        atm_menu(_name.title())
        option = input("Choose an option: ")

        if option == "1":
            account.show_balance(balance)
        
        elif option == "2":
            balance = account.deposit(balance)
        
        elif option == "3":
            balance = account.withdraw(balance)
        
        elif option == "4":
            account.logout(_name)
        
        else:
            print("Invalid option selected, please enter valid option!")

    

main()


