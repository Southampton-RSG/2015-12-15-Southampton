from running import running

def test_empty():
   assert running([]) == []

def test_two_arguments():
   assert running([0, 1]) == [0, 1]

def test_three_arguments():
   assert running([0, 1, 2]) == [0, 1, 3]

def test_four_arguments():
   assert running([0, 1, 2, 3]) == [0, 1, 3, 6]
