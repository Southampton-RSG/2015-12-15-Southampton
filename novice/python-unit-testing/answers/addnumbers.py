def addnumbers(list):
    if list == []:
        return None

    count = 0
    for number in list:
        count = count + number
    return count
