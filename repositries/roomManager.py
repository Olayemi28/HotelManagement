from models.room import Room
from typing import List

class Room_Manager:
    rooms:List[Room] = []
    file = open("Room.txt", "a+")
    def __init__(self):
        self.file.seek(0)
        for detail in self.file:
            self.rooms.append(Customer.parse(detail))


    def create_room(self, price:float, availability_status:bool, room_number:int, room_type:str, mylist = [Booking]):
        id =  self.get_id()
        rooms = Room(price = price, availability_status = availability_status, room_number = room_number, room_type = room_type)
        self.rooms.append(rooms)
        if self.file.closed is True:
            self.file = open("Room", "a+")
        else:
            self.file.write(rooms + "\n")
            self.file.flush() 
            return "Room Successfully created" 


    def get_id(self):
        unique_id = len(self.rooms)
        if unique_id == 0:
          unique_id += 1  
          return unique_id
        else:
           for room in self.rooms:
            if room.id == unique_id or room.id >= unique_id:
                unique_id += 1
                return unique_id
            else:
                continue 
            



