class Passenger:
    """ PASSANGER """
    def __init__(self,first_name,last_name,seat_number,ticket_type):
         self.first_name = first_name.strip().title()
         self.last_name = last_name.strip().title()
         self.seat_number = seat_number
         self.ticket_type = ticket_type
    def __str__(self):
         fname_tital = self.first_name
         lname_tital = self.last_name
         msg = f'{fname_tital.strip().title()} {lname_tital.strip().title()} is in seat {self.seat_number} in {self.ticket_type.strip().title()} class.'

         return msg