from models.customer import Customer
from repositries.customerManager import CustomerManager
customer_Manager = CustomerManager()

class Customer_Menu:

    mylist = []

    def create_user(self):
            print("Kindly fill in this form to register as a User")
            first_name = str(input("Enter your first name: "))
            last_name = str(input("Enter your last name: "))
            email = str(input("Enter your email: "))
            password = str(input("Enter your password: "))
            age = int(input("Enter your age: "))
            address = str("Enter your address: ")
            customer_Manager.create_customer(first_name, last_name, address, age, email, password)


    def log_in_user(self):
            print("Kindly fill in this form to sign-in as a User")
            email = str(input("Enter your email address: "))
            password = str(input("Enter your password: "))
            login = customer_Manager.sign_in(email, password)
            if login is False:
                print(("Incorrect Password"))
            else:
                if action == 0:
                    Customer_Menu.user_sub_menu()    
                else:
                   show_user_menu(action)        


    def update_user(self):
        print("Kindly fill in this form to edit profile")
        first_name = str(input("Enter your first name: "))
        last_name = str(input("Enter your last name: "))
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        age = int(input("Enter your age: "))
        address = str("Enter your address: ")
        customer_Manager.update_customer(first_name, last_name, address, age, email, password, mylist)      


    def show_user_menu(action):
        print("""
        Enter 1 to Book Room
        Enter 2 to View all Rooms
        Enter 0 to go back
        -->""")     
        

        