from fitness_entry import FitnessEntry

def test_valid_entry():
    e = FitnessEntry("2024-01-01", 70, 5000, 300, 30)
    assert e.date == "2024-01-01"
    assert e.heart_rate == 70
    assert e.steps == 5000
    assert e.calories == 300
    assert e.walking_time == 30
