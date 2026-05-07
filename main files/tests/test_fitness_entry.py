import pytest
from fitness_entry import FitnessEntry
from fitness_entry import InvalidFitnessEntryError


def test_valid_entry():
    """
    Checks that FitnessEntry constructor works correctly with stadard ideal values.
    This verifies that all five attributes are stored properly.
    """
    #creates entry using valid numbers
    e = FitnessEntry("2024-01-01", 70, 5000, 300, 30)
    #checks that each attribute matches what we passed in
    assert e.date == "2024-01-01"
    assert e.heart_rate == 70
    assert e.steps == 5000
    assert e.calories == 300
    assert e.walking_time == 30


def test_invalid_heart_rate():
    """
    Checks that InvalidFitnessEntryError is raised when heart rate is negative.
    Heart rate cant be negative in real life so we reject it.
    """
    #negative heart rate triggers validation error
    with pytest.raises(InvalidFitnessEntryError):
        FitnessEntry("2024-01-01", -10, 5000, 300, 30)
