admin = "Ranjan"
adpass = 123
cust = "Customer"
cupass = 123
pizza = 35
pepsi = 25
french_fries = 65
order = 0
pepsiq = 0
pizzaq = 0
frenq = 0
# admin id=admin
# admin password=123
# customer id=customer
# customer password=123
while (True):
    print("<----------------------------WELCOME TO PIZZA HUT--------------------------->")
    print("press 1. --> for admin section")
    print("press 2. --> for customer section")
    print("press 3. --. for quitting")
    main_choice = int(input("enter your choice:"))
    while (True):
        if main_choice == 1:
            print("welcome to admin section")
            print("press 2 to go back")
            adid = input("please enter your admin id to continue").capitalize()
            if adid == admin:
                print("welcome", admin)
                adpas = int(input("enter your password to continue"))
                if adpas == adpass:
                    print(admin, " logged in successfully")
                    while (True):
                        print("press 1.--> for stock management ")
                        print("press 2.--> for viewing stocks")
                        print("press 3.--> for logout")
                        adchoice = int(input("enter your choice:"))
                        if adchoice == 1:
                            print("welcome to stock management section")
                            while (True):
                                print("what you want to do??")
                                print("press 1.--> for adding stock")
                                print("press 2.--> for deleting stock")
                                print("press 3.--> to go back")
                                stock_choice = int(input("enter your choice:"))
                                if stock_choice == 1:
                                    while (True):
                                        print("what you want to add?")
                                        print("1. Pizza")
                                        print("2. pepsi")
                                        print("3. french fries")
                                        print("press 4. to go back")
                                        add_choice = int(input("enter your choice:"))
                                        if add_choice == 1:
                                            pia = int(input("enter the quantity of pizza you want to add"))
                                            pizza = pizza + pia
                                            print(pia, " pizzas were added in stock")
                                        elif add_choice == 2:
                                            pea = int(input("enter the quantity of pepsi you want to add"))
                                            pepsi = pepsi + pea
                                            print(pea, " pepsis were added in stock")
                                        elif add_choice == 3:
                                            fra = int(input("enter the quantity of french fries you want to add"))
                                            french_fries = french_fries + fra
                                            print(fra, " french fries were added in stock")
                                        elif add_choice == 4:
                                            break
                                        else:
                                            print("wrong choice")
                                elif stock_choice == 2:
                                    while (True):
                                        print("what you want to delete?")
                                        print("1. Pizza")
                                        print("2. pepsi")
                                        print("3. french fries")
                                        print("press 4. to go back")
                                        add_choice2 = int(input("enter your choice:"))
                                        if add_choice2 == 1:
                                            pia1 = int(input("enter the quantity of pizza you want to delete"))
                                            pizza = pizza - pia1
                                            print(pia1, " pizzas were removed from stock")
                                        elif add_choice2 == 2:
                                            pea1 = int(input("enter the quantity of pepsi you want to delete"))
                                            pepsi = pepsi - pea1
                                            print(pea1, " pepsis were removed from stock")
                                        elif add_choice2 == 3:
                                            fra1 = int(input("enter the quantity of french fries you want to delete"))
                                            french_fries = french_fries - fra1
                                            print(fra1, " french fries were removed from stock")
                                        elif add_choice2 == 4:
                                            break
                                        else:
                                            print("wrong choice")
                                elif stock_choice == 3:
                                    break
                                else:
                                    print("wrong choice")
                        elif adchoice == 2:
                            print("welcome to view section")
                            print("you have the following in stocks:-")
                            print("pepsi", pepsi)
                            print("pizza", pizza)
                            print("french fries", french_fries)

                        elif adchoice == 3:
                            print("thank you ")
                            break
                        else:
                            print("wrong choice")
                else:
                    print("password didn't matched")
            elif adid == "2":
                break
            else:
                print("user did'nt matched")
                print("please enter correct id")
        elif main_choice == 2:
            print("welcome to customer section")
            print("press 2 to go back")
            cdid = input("please enter your admin id to continue").capitalize()
            if cdid == cust:
                print("welcome", cdid)
                cupas = int(input("enter your password to continue"))
                if cupas == cupass:
                    print(cdid, " logged in successfully")
                    while (True):
                        print("press 1.--> for menu")
                        print("press 2.--> for order")
                        print("press 3,-->view cart and bill")
                        print("press 4. to logout")
                        cuchoice = int(input("enter your choice:"))
                        if cuchoice == 1:
                            print("-------------------------")
                            print("------Today's menu-------")
                            print("-------------------------")
                            print("pizza,         Rs.99")
                            print("pepsi,         Rs.75")
                            print("french fries   Rs.135")
                        elif cuchoice == 2:
                            while (True):
                                print("what you want to order?")
                                print("press 1.--> for pizza")
                                print("press 2.--> for pepsi")
                                print("press 3.--> for french fries")
                                print("press 4.--> to go back")
                                order_choice = int(input("enter your choice"))
                                if order_choice == 1:
                                    pizzaq = int(input("enter the quantity of pizza you want to add"))
                                    if pizzaq < pizza:
                                        pizza = pizza - pizzaq
                                        order = order + 1
                                        print(pizzaq, " were successfully added to cart ")
                                    else:
                                        print("sorry :(, we don't have the stocks now")
                                elif order_choice == 2:
                                    print("enter the quantity of pepsi you want to add")
                                    pepsiq = int(input("enter the quantity pepsi you want to add"))
                                    if pepsiq < pepsi:
                                        pepsi = pepsi - pepsiq
                                        order = order + 1
                                        print(pepsiq, " were successfully added to cart ")
                                    else:
                                        print("sorry :(, we don't have the stocks now")
                                elif order_choice == 3:
                                    print("enter the quantity of french fries you want to add")
                                    frenq = int(input("enter the quantity of french you want to add"))
                                    if frenq < french_fries:
                                        french_fries = french_fries - frenq
                                        order = order + 1
                                        print(frenq, " were successfully added to cart ")
                                    else:
                                        print("sorry :(, we don't have the stocks now")
                                else:
                                    break
                        elif cuchoice == 3:
                            print("view cart and billing")
                            if order > 0:
                                print(
                                    "==================================     CASH BILL    ================================================")
                                print(
                                    "----------------------------------------------------------------------------------------------------")
                                print(
                                    "Sl No.        item              quantity               rate                             total")
                                print(
                                    "----------------------------------------------------------------------------------------------------")
                                print("1.             pepsi            ", pizzaq,
                                      "             Rs.99                             ", pizzaq * 99)
                                print("2.             pepsi            ", pepsiq,
                                      "             Rs.75                             ", pepsiq * 75)
                                print("3.             french fries     ", frenq,
                                      "              Rs.135                             ", frenq * 135)
                                print(
                                    "-------------------------------------------------------------------------------------------------------")
                                print(
                                    "                                                         GRAND TOTAL(incl. of 18% GST)=",
                                    (pizzaq * 99) + (pepsiq * 75) + (frenq * 135))
                                print(
                                    "------------------------------------------------------------------------------------------------------")
                                print("\n \n ")
                                print("press 1.--> to confirm the order")
                                print("press 2.--> to go back")
                                cart = int(input("enter your choice:"))
                                while (True):
                                    if cart == 1:
                                        print("order placed")
                                        break
                                    elif cart == 2:
                                        break
                                    else:
                                        print("wrong choice")
                                        break

                            else:
                                print("please add sonething first")
                        elif cuchoice == 4:
                            break
                        else:
                            print("wrong choice")

                else:
                    print("password didn't matched")
            elif cdid == "2":
                break
            else:
                print("user didn't matched")
                print("please enter correct id")

        elif main_choice == 3:
            print("thank you for using our app")
            exit()
        else:
            print("please enter correct choice")
            break
