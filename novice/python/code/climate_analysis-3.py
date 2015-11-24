climate_data = open('../data/sc_climate_data_10.csv', 'r')

for line in climate_data:
    data = line.split(',')

    # print 4th column (max temperature)
    print('Max temperature', data[3])
