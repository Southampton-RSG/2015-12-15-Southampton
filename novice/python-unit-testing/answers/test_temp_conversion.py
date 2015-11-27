from nose.tools import *
from temp_conversion import fahr_to_kelvin

def test_basic_value():
    assert fahr_to_kelvin(20.0) == 266.4833333333333

def test_zero_kelvin():
    assert fahr_to_kelvin(-459.67) == -5.684341886080802e-14

def test_zero_kelvin_better():
    assert round(fahr_to_kelvin(-459.67),2) == 0.00

def test_negative_fahr():
    assert round(fahr_to_kelvin(-100),2) == 199.82

@raises(TypeError)
def test_string():
    fahr_to_kelvin("Something")

@raises(TypeError)
def test_null_input():
    fahr_to_kelvin()
