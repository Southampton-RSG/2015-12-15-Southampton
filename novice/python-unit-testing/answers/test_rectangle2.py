from rectangle2 import rectangle_area

def test_unit_square():
    assert rectangle_area([0, 0, 1, 1]) == 1.0

def test_large_square():
    assert rectangle_area([1, 1, 4, 4]) == 9.0

def test_actual_rectangle():
    assert rectangle_area([0, 1, 4, 7]) == 24.0
