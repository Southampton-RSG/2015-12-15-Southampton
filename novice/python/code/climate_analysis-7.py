climate_data = open('../data/sc_climate_data_10.csv', 'r')

def fahr_to_celsius(fahr):
    # apply standard Fahrenheit to Celsius formula
    celsius = ((fahr - 32) * (5/9)) 
    return celsius

def fahr_to_kelvin(fahr):
    # apply standard Fahrenheit to Kelvin formula
    kelvin = fahr_to_celsius(fahr) + 273.15
    return kelvin

for line in climate_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # extract our max temperature in Fahrenheit - 4th column
        fahr = float(data[3])

        celsius = fahr_to_celsius(fahr)
        kelvin = fahr_to_kelvin(fahr)

        print('Max temperature in Celsius', celsius, 'Kelvin', kelvin)
