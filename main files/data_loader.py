import pandas as pd
from fitness_entry import FitnessEntry, InvalidFitnessEntryError

class DataFormatError(ValueError):
    pass

def load_fitness_data(file_path):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except ValueError:
        raise DataFormatError(f"File '{file_path}' is not in a valid CSV format. It may be corrupted.")
    
    required_columns = ["date", "heart_rate", "steps", "calories", "walking_time"]

    for col in required_columns:
        if col not in df.columns:
            raise DataFormatError (f"Missing required column '{col}' in the CSV file.")
        fitness_entries = []

        for index, row in df.iterrows():
            try:
                entry = FitnessEntry(
                    row["date"],
                    row["heart_rate"],
                    row["steps"],
                    row["calories"],
                    row["walking_time"] )
                fitness_entries.append(entry)
            except InvalidFitnessEntryError as e:
                print(f"Skipping row {index} due to invalid data: {e}")
        return fitness_entries
    