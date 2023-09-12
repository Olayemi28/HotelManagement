from typing import List
from models.customer import Customer
class CustomerManager:
    customers:List[Customer] = []

    file = open("Customer.txt","a+")

    def __init__(self):
        self.file.seek(0)
        for detail in self.file:
            self.customers.append(Customer.parse(detail))
            
    def create_customer(self, first_name, last_name, address, age, email, password):
        id = self.get_id()
        customers = Customer(id = id, email = email, password = password, first_name = first_name, last_name = last_name, age = age, address = address, mylist=[])
        self.customers.append(customers)
        if self.file.closed is True:
            self.file = open("Customer", "a+")
        else:
            self.file.write(f"{str(customers)}" "\n")
            self.file.flush() 
            return "Sucessfully Registered"  

    def get_id(self):
        unique_id = len(self.customers)
        if unique_id == 0:
          unique_id += 1  
          return unique_id
        else:
           for customer in self.customers:
            if customer.id == unique_id or customer.id >= unique_id:
                unique_id += 1
                return unique_id
            else:
                continue    

    def sign_in(self, email:str, password:str):
        for customer in self.customers:
            if customer.email == email and customer.password == password:
                return "Succesfully Sign-in"
            else:
                return "User  doesn't exist"   

    def update_customer(self, first_name, last_name, address, age, email, password, mylist):
        customer = self.find_customer(email = email)
        if customer:
            customer.first_name = first_name
            customer.last_name = last_name
            customer.address = address
            customer.age = age
            self.refresh_file()
            return True
        else:
            return False    



    def find_customer(self, email:str):
        for customer in self.customers:
            if customer.email == email:
              return customer 
            else:
                return False

    def refresh_file(self):
        self.file = open("Customer.txt", "a") 
        for customer in self.customers:
            self.file.writable(customer + "\n") 
            self.file.flush()          
