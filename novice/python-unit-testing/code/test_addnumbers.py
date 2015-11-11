from addnumbers import addnumbers

def test_empty():
   assert addnumbers([]) == None

def test_single_value():
   assert addnumbers([1]) == 1

def test_two_values():
   assert addnumbers([1, 2]) == 3

def test_three_values():
   assert addnumbers([1, 2, 3]) == 6
