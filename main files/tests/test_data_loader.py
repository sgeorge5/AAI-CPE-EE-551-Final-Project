import pytest
from data_loader import load_fitness_data

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        load_fitness_data("does_not_exist.csv")
