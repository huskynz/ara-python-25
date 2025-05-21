class Passenger:
    """ PASSANGER """
    def __init__(self,first_name,last_name,seat_number,ticket_type):
         self.first_name = first_name.strip().title()
         self.last_name = last_name.strip().title()
         self.seat_number = seat_number
         self.ticket_type = ticket_type

         self.allpassengers = [] = []

class Aircraft:
    """WHY IS THIS NUMBER 3 YET REQUIRED FOR NUMBER 2"""
    def __init__(self,aircraft_type,max_passengers):
        self.aircraft_type = aircraft_type.strip().title()
        self.max_passengers = max_passengers
    
    def add_passenger(self,first_name,last_name,seat_number,ticket_type):
        a_passanger = Passenger(first_name,last_name,seat_number,ticket_type)
        self.allpassengers.append(a_passanger)
        
    def __str__(self):
        msg = f'The plane contains the following passengers:\n'
        for a_passanger in self.allpassengers:
            msg += f'{self.first_name} {self.last_name} is in seat {self.seat_number}\n'
        return msg
    

cessna_caravan = Aircraft('cessna caravan', 13)
print(f'Max passengers: {cessna_caravan.max_passengers}')
print('Adding passengers...')
cessna_caravan.add_passenger('paddington','brown',5,'Economy')
cessna_caravan.add_passenger('Aunt','Lucy',6,'Economy')
cessna_caravan.add_passenger('Uncle','Pastuzo',4,'Economy')
print(cessna_caravan)