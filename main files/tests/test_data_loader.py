import pytest
import pandas as pd
from data_loader import load_fitness_data
from exceptions import DataFormatError
from fitness_entry import FitnessEntry

def test_missing_file():
    """
    Checks that load_fitness_data raises FileNotFoundError when the CSV doesnt exist.
    This prevents the program from crashing with errors when the file is missing
    """
    #attempts to load a file that doesn't exist (error is expected to be raised)
    with pytest.raises(FileNotFoundError):
        load_fitness_data("does_not_exist.csv")

def test_missing_column(tmp_path):
    """
    Checks that DataFormatError is raised when the CSV is missing the required columns.
    These dates are: data, heart_rate_avg, steps, calories_burned, and active_minutes.
    Then a tmp_path fixture is used to create a temporary file that gets deleted after the test.
    """
    #creates dataframe missing calories_burned and active_minutes columns
    df = pd.DataFrame({
        "date": ["2023-01-01"],
        "heart_rate_avg": [70],
        "steps": [1000],
    })

    #saves incomplete dataframe to temp csv file
    p = tmp_path / "bad.csv"
    df.to_csv(p, index=False)
    #expects DataFormatError due to missing columns
    with pytest.raises(DataFormatError):
        load_fitness_data(str(p))
