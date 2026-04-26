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
            raise InvalidFitnessEntryError("Date parts must be in numbers.")
        
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)

        if year < 1900 or month < 1 or month > 12 or day < 1 or day > 31:
            raise InvalidFitnessEntryError("date must be in the format 'YYYY-MM-DD' and in reasonable range.")
        
        self.date = f"{year:04d}-{month::02d}-{day:02d}"

        try:
            self.heart_rate = int(heart_rate)
            self.steps = int(steps)
            self.calories = float(calories)
            self.walking_time = float(walking_time)
        except ValueError:
            raise InvalidFitnessEntryError("Heart rate and steps must be integers, calories and walking time must be in numbers.")
    
    def __str__(self):
        return(f"{self.date}: Heart Rate = {self.heart_rate} bpm, "
               f"steps = {self.steps}, calories = {self.calories: .1f}, walking time = {self.walking_time:.1f} minutes")
    
    def __add__(self, other):
        if not isinstance(other, FitnessEntry):
            return NotImplemented
        
        combined_date = f"{self.date}__{other.date}"
        combined_hr = int(round((self.heart_rate + other.heart_rate) / 2.0))
        combined_steps = self.steps + other.steps
        combined_calories = self.calories + other.calories
        combined_walking_time = self.walking_time + other.walking_time

        return FitnessEntry(combined_date, combined_hr, combined_steps, combined_calories, combined_walking_time,)
    
    def __eq__(self, other):
        if not isinstance(other, FitnessEntry):
            return False
        return(self.date == other.date and
               self.heart_rate == other.heart_rate and
               self.steps == other.steps and
               abs(self.calories - other.calories) < 1e-9 and
               abs(self.walking_time -other.walking_time) < 1e-9)
    
    def toTuple(self):
        return(self.date, self.heart_rate, self.steps, self.calories, self.walking_time)
    
    def isIrregularHr(self, low = 40, high = 180):
        return not (low <= self.heart_rate <= high)
    
    def stepsToMiles(self, stride_length = 0.762):
        meters = self.steps * stride_length
        miles = meters / 1609.34
        return miles
