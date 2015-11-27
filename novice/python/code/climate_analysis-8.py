import temp_conversion

climate_data = open('../data/sc_climate_data_10.csv', 'r')

for line in climate_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # extract our max temperature in Fahrenheit - 4th column
        fahr = float(data[3])

        celsius = temp_conversion.fahr_to_celsius(fahr)
        kelvin = temp_conversion.fahr_to_kelvin(fahr)

        print('Max temperature in Celsius', celsius, 'Kelvin', kelvin)
