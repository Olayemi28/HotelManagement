import datetime
from datetime import date
class Booking:
    id:int
    booking_date: date
    end_date: date
    payment_status:bool
    customer_id:int
    room_id:int
    def __init__(self, booking_date:datetime, end_date:datetime, payment_status:bool, customer_id:int, room_id:int):
        self.booking_date = datetime.datetime().now()
        self.customer_id = customer_id
        self.end_date = end_date
        self.payment_status = payment_status
        self.room_id = room_id
    
