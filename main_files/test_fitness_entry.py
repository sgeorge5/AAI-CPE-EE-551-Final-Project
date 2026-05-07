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



def test_invalid_steps():
    """
    Checks that InvalidFitnessEntryError is raised when steps is negative.
    Steps count cant be negative - you cant take negative steps.
    """
    #negative steps triggers validation error
    with pytest.raises(InvalidFitnessEntryError):
        FitnessEntry("2024-01-01", 70, -100, 300, 30)
        


def test_str_method():
    """
    Checks that the __str__ method returns a readable string with date and steps.
    User should see something meaningful when they print an entry.
    """
    e = FitnessEntry("2024-01-01", 70, 5000, 300, 30)
    s = str(e)
    #verifies date appears in the string output
    assert "2024-01-01" in s
    #verifies step count appears in the string output
    assert "5000" in s


def test_add_entries():
    """
    Checks that the + operator correctly adds two FitnessEntry objects together.
    Numeric fields (heart rate, steps, calories, walking time) then get summed.
    Date field keeps the first entrys date
    """
    e1 = FitnessEntry("2024-01-01", 70, 5000, 300, 30)
    e2 = FitnessEntry("2024-01-02", 80, 6000, 350, 40)

    #uses + operator to combine entries
    e3 = e1 + e2

    #verfies that all numeric fields were added correctly
    assert e3.heart_rate == 150
    assert e3.steps == 11000
    assert e3.calories == 650
    assert e3.walking_time == 70
