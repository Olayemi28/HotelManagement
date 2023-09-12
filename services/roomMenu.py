from models.room import Room
from repositries.roomManager import Room_Manager
room_manager = Room_Manager()

class Room_Menu:
    def create(self):
      room_number = str(input("Enter the room number:"))
      room_type = str(input("Enter the room type:"))
      availability_status = bool(input("Availability Status = "))
      price = float(input("Room price = "))
      room_manager.create_room(price, availability_status, room_number, room_type)
