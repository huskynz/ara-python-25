class Passenger:
    """ PASSANGER """
    def __init__(self,first_name,last_name,seat_number,ticket_type):
         self.first_name = first_name.strip().title()
         self.last_name = last_name.strip().title()
         self.seat_number = seat_number
         self.ticket_type = ticket_type

         self.a_passanger = []
    
    def add_passenger(self,first_name,last_name,seat_number,ticket_type):
        a_passanger = Passenger(first_name,last_name,seat_number,ticket_type)
        self.a_passanger.append(a_passanger)
        return True
    
small_plane = Aircraft('cessna 182',3)
print('Adding passengers...')
small_plane.add_passenger('paddington','brown',1,'Economy')
small_plane.add_passenger('Aunt','Lucy',3,'Economy')
small_plane.add_passenger('Uncle','Pastuzo',2,'Economy')
print('The passengers are ...')
for passenger in small_plane.all_passengers:
    print(f'Passenger: {passenger.first_name} {passenger.last_name} Seat: {passenger.seat_number} Ticket type: {passenger.ticket_type}')