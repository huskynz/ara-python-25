class Aircraft:
    """WHY IS THIS NUMBER 3 YET REQUIRED FOR NUMBER 2"""
    def __init__(self,aircraft_type,max_passengers):
        self.all_passengers = []
        self.aircraft_type = aircraft_type.strip().title()
        self.max_passengers = max_passengers

small_plane = Aircraft('Cessna 182',3)
print(small_plane.aircraft_type)
print(small_plane.max_passengers)
print()
big_plane = Aircraft('airbus a320',170)
print(big_plane.aircraft_type)
print(big_plane.max_passengers)