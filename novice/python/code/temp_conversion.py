"""A library to perform temperature conversions"""

def fahr_to_celsius(fahr):
    """Convert Fahrenheit to Celsius.

    Uses standard fahrenheit to Celsius formula

    Arguments:
    fahr -- the temperature in Fahrenheit
    """
    celsius = ((fahr - 32) * (5/9)) 
    return celsius
