from typing import List
from .booking import Booking
class Room:
    id:int
    price:float
    availability_status:bool
    room_number:int
    room_type:str
    mylist: List[Booking] = []
    def __init__(self, price:float, availability_status:bool, room_number:int, room_type:str, mylist = [Booking]):
        self.availability_status = availability_status
        self.mylist = mylist
        self.price = price
        self.room_number = room_number
        self.room_type = room_type