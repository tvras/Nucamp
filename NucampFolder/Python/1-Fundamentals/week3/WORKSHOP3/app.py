from donations_pkg.homepage import show_homepage
from donations_pkg.user import login, get_login, register, donate , auth_user, show_donations


database = {
    "admin" : "password123",
}

donations = []

authorized_user = ""
while True:
    show_homepage()
    auth_user(authorized_user)


    choice = input("Choose an option: ")

    if choice == "1":
        username,password = get_login()
        authorized_user = login(database,username,password)

    elif choice == "2":
        username,password = get_login()
        authorized_user = register(database,username)
        if authorized_user != "":
            database[username] = password
        

    elif choice == "3":
        if authorized_user != "":
            donation_string = donate(username)
            donations.append(donation_string)

    elif choice == "4":
        show_donations(donations)
        

    elif choice == "5":
        print("\nLeaving DonateMe...")
        break
            
    else:
        print("\nInvalid option. Please choose a valid option!")
        continue




