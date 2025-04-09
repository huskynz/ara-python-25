# 1-1-1
# Peter
# peter@husky.nz
# wow

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Converts the given temperature from Fahrenheit to Celsius, rounded to 1 decimal place.
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 1)