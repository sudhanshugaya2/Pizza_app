admin = "Farman"
apass = 123

customer = "Aspire"
cpass = 123

while(True):
    print("Press 1 for the admin panel")
    print("Press 2 for the customer panel")
    print("Press 3 for quiting the app")
    mpc = int(input("Enter your choice"))
    if mpc == 1:
        while(True):
            print("Admin Panel")
            print("Press 1 to go back to the main menu")
            aid = input("Enter your id").capitalize()
            if aid==admin:
                apassword = int(input("Enter the password"))
                if apass==apassword:
                    print(admin," you have logged in succesfully")
                    while (True):
                        else:
                        print("Wrong password")
                        elif aid == '1':
                break
                else:
                print("Wrong id")
            elif mpc == 2:
                print("Customer Panel")
        elif mpc == 3:
        print("Thanks for using the app")
        break
    else:
        print("Choose a good option")