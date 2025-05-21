class Passenger():
    """ Passenger blueprint """
    def __init__(self, first_name, last_name, seat_number, ticket_type):
        self.first_name = first_name.strip().title()
        self.last_name = last_name.strip().title()
        self.seat_number = seat_number
        self.ticket_type = ticket_type

    def __str__(self):
        return f'{self.first_name} {self.last_name} is in seat {self.seat_number} in {self.ticket_type} class.'

class Aircraft:
    """ Aircraft blueprint """
    def __init__(self, aircraft_type, max_passengers):
        self.all_passengers = []
        self.aircraft_type = aircraft_type.strip().title()
        self.max_passengers = max_passengers


    # No checking of seat availability
    def add_passenger(self, first_name, last_name, seat_number, ticket_type):
        self.all_passengers.append(Passenger(first_name, last_name, seat_number, ticket_type))
        return True

    def __str__(self):
        msg = f'The plane contains the following passengers:\n'
        for a_passenger in self.all_passengers:
            msg += f'{a_passenger.first_name} {a_passenger.last_name} is in seat {a_passenger.seat_number}\n'
        return msg


    def get_total_passengers(self):
        return len(self.all_passengers) 


    def get_total_free_seats(self):
        return self.max_passengers - self.get_total_passengers()


    def get_seat_availability(self, seat_number):
        if seat_number <= self.max_passengers:
            for a_passenger in self.all_passengers:
                if a_passenger.seat_number == seat_number:
                    return False
            return True
        return False


    def remove_passenger(self, first_name, last_name, seat_number): 
        for a_passenger in self.all_passengers:
            if all([a_passenger.first_name == first_name,
                    a_passenger.last_name == last_name,
                    a_passenger.seat_number == seat_number]):
                self.all_passengers.remove(a_passenger)
                return True
        return False
