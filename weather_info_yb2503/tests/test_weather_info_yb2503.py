from weather_info_yb2503 import weather_info_yb2503
import pytest

def test_weather_sector(zipcode, column): 
    zipcode = 11101
    column = 'humidity'
    expected = 74.0
    actual = weather_sector(zipcode, column)
    assert actual == expected, 'not works for the zipcode'