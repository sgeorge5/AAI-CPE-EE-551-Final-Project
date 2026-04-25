class InvalidFitnessEntryError(ValueError):
    pass
class FitnessEntry:
    def __init__(self, date_value, heart_rate, steps, calories, walking_time):
        if not isinstance(date_value, str):
            raise InvalidFitnessEntryError("Date must be a string in the format 'YYYY-MM-DD'.")
        parts = date_value.strip().split('-')
        if len(parts) != 3:
            raise InvalidFitnessEntryError("Date must be a string in the format 'YYYY-MM-DD'.")
        year_str, month_str, day_str = parts
        if not (year_str.isdigit() and month_str.isdigit() and day_str.isdigit()):
            raise InvalidFitnessEntryError("Date parts must be numeric.")
    
    def __str__(self):
        return(f"{self.date}: Heart Rate = {self.heart_rate} bpm, "
               f"steps = {self.steps}, calories = {self.calories: .1f}, walking time = {self.walking_time:.1f} minutes")