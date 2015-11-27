climate_data = open('../data/sc_climate_data_10.csv', 'r')

for line in climate_data:
    print(line.rstrip())
