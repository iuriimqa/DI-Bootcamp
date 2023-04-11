password = 1234

logged_in = False

while not logged_in:
    try:
        user_pass = int(input("password: "))
        if user_pass == password:
            print("You're logged in!")
            logged_in = True
    except ValueError:
        print("Invalid input!")