import pandas as pd
from main_files.fitness_entry import FitnessEntry
from main_files.exceptions import InvalidFitnessEntryError, DataFormatError


def load_fitness_data(file_path):
    """
    Load fitness data from a CSV file using pandas.
    The CSV file is validated to ensure it contains the required columns,
    and each row is converted into a FitnessEntry object. The function 
    checks that the file exists, is a valid CSV, and contains all
    required columns. If any required column is missing, a DataFormatError is
    raised. Rows with invalid values are skipped, and the rest are returned as
    a list of FitnessEntry objects.
    """
    # Try reading the CSV file and handle potential errors.
    try:
        df = pd.read_csv(file_path) 
    except FileNotFoundError:
        # Raise a custom error if the file is not found.
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except ValueError:
        # Raise a custom error if the file is not a valid CSV.
        raise DataFormatError(f"File '{file_path}' is not a valid CSV file.")
    
    # Normalize date format to YYYY-MM-DD for consistency.
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    # Required columns that must be present in the CSV
    required_columns = [
        "date",
        "heart_rate_avg",
        "steps",
        "calories_burned",
        "active_minutes"
    ]

    # Check for missing columns and raise an error if any are missing.
    for col in required_columns:
        if col not in df.columns:
            raise DataFormatError(f"Missing required column '{col}' in the CSV file.")

    # List to store valid FitnessEntry objects
    fitness_entries = []

    # Convert each row into a FitnessEntry object, handling invalid data.
    for index, row in df.iterrows():
        try:
            entry = FitnessEntry(
                row["date"],
                row["heart_rate_avg"],
                row["steps"],
                row["calories_burned"],
                row["active_minutes"]
            )
            fitness_entries.append(entry)
        except InvalidFitnessEntryError as e:
            # Skip the rows with invalid data but continue processing the rest of the file.
            print(f"Skipping row {index} due to invalid data: {e}")

    return fitness_entries
