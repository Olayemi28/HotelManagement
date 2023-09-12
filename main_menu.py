from services.customerMenu import Customer_Menu

customer_menu = Customer_Menu()
def main_menu():
    print("""Welcome to Wasir Hotel & Suites
            Enter 1 to Aceess the User Menu
            Enter 2 to Access the Manager Menu
            Enter 0 to Quit
    -->""")

def sub_menu(option):
    if option == 0:
        print("Thanks for patronizing Wasir Suites")
    elif option == 1:
        user_register_login_menu()
        response = int(input())
        if response == 0:
            main_menu()
        else:
          user_sub_menu(response)
    elif option == 2:
       manager_register_login_menu()
    else:
        print("Wrong Input")    


def user_sub_menu(response):
        if response == 1:
           customer_menu.create_user()
        elif response == 2:
            customer_menu.log_in_user()


def user_register_login_menu():
    print(""" User Menu:
        Enter 1 to register as a User
        Enter 2 to login as a User 
        Enter 0 to go back
    -->""")

def manager_register_login_menu():
    print(""" User Menu:
        Enter 1 to register as a Manager
        Enter 2 to login as a Manager 
        Enter 0 to go back
    -->""")

def main():
    result = True
    while (result):
        main_menu()
        option = int(input())
        if (option == 0):
            print("Thanks for patronizing Wasir Suites")
            flag = False
        else:
            sub_menu(option)


main()


