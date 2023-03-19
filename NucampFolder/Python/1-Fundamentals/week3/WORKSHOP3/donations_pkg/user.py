def auth_user(authorized_user):
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:",authorized_user.title())



def get_login():
    username = input("Enter Username: ").lower()
    password = input("Enter password: ")
    return username, password



def login(database, username, password):

    if username in database and password == database[username]:
        print(f"\nWelcome, {username.title()}!")
        if password != database[username]:
            print(f"\nIncorrect password for {username.title()}")
            return ""
        return username       
    else:
        print("\nUser not found. PLease register.")
        return ""



def register(database, username):
     if username in database:
          print("\nUsername already registered.")
          return ""
     else:
          print(f"\nUsername {username.title()} registered.")
          return username



def donate(username):
    try:
        donation_amt = float(input("Enter amount to donate: "))
        donation_string = f"{username.title()} donated ${donation_amt}"
    except:
        print(donation_string)
        return donation_string



def show_donations(donation):
    total_d = 0
    print("\n--- All Donations ---")
    if donation == []:
        print("Currently, there are no donations.")
    for d in donation:
        d_amount = float(d[d.index("$") + 1::])
        total_d +=d_amount
        print(d)
    print(f"Total = ${total_d}")



