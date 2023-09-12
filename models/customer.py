from typing import List
from .user import User
from.booking import Booking
class Customer(User):
    age:int
    address:str
    mylist:List[Booking] =[]
    def __init__(self, id, email, password, first_name, last_name, age, address, mylist):
        super().__init__(id, email, password, first_name, last_name)
        self.age:age
        self.address:address
        self.mylist:mylist