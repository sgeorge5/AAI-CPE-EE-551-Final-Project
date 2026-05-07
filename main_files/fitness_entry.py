from main_files.exceptions import InvalidFitnessEntryError

class FitnessEntry:
    """
    Represents a single day's fitness data with validations, conversions
    and operator support. Validates data and numeric fields on construction.
    This class validates the date format and all numeric fields when an entry 
    is created. It also provides helper methods, string formatting, and 
    operator overloading so entries can be compared, combined, and converted easily.
    """
    def __init__(self, date_value, heart_rate_avg, steps, calories_burned, active_minutes):
        """
        Create a FitnessEntry using the provided daily fitness values. The date
        must be in YYYY-MM-DD format, and all numeric values must be valid
        and non-negative. If any value is invalid, an InvalidFitnessEntryError
        is raised.
        """
        # Validate date format and values.
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

        # Basic range checks for date components. More complex validation 
        # (like checking for valid days in a month) is not implemented here.
        if year < 1900 or month < 1 or month > 12 or day < 1 or day > 31:
            raise InvalidFitnessEntryError("date must be in the format 'YYYY-MM-DD' and in reasonable range.")
        
        # Store the normalized date string.
        self.date = f"{year:04d}-{month:02d}-{day:02d}"

        # Validate and store numeric fields, ensuring they are non-negative.
        try:
            self.heart_rate = int(heart_rate_avg)
            self.steps = int(steps)
            self.calories = float(calories_burned)
            self.walking_time = float(active_minutes)

            if self.heart_rate < 0:
                raise InvalidFitnessEntryError("Heart rate must be non-negative.")
            if self.steps < 0:
                raise InvalidFitnessEntryError("Steps must be non-negative.")
            if self.calories < 0:
                raise InvalidFitnessEntryError("Calories must be non-negative.")
            if self.walking_time < 0:
                raise InvalidFitnessEntryError("Walking time must be non-negative.")
        except ValueError:
            raise InvalidFitnessEntryError("Heart rate and steps must be integers, calories and walking time must be in numbers.")
    
    def __str__(self):
        """
        Return a readable string describing the fitness entry, 
        including date, heart rate, steps, calories, and walking time.
        """
        return(f"{self.date}: Heart Rate = {self.heart_rate} bpm, "
               f"steps = {self.steps}, calories = {self.calories: .1f}, walking time = {self.walking_time:.1f} minutes")
    
    def __add__(self, other):
        """
        This funciton Combines two FitnessEntry objects by adding their numeric values.
        The date of the first entry is used for the combined result.
        If the other object is not a FitnessEntry, NotImplemented is returned.
        """
        if not isinstance(other, FitnessEntry):
            return NotImplemented
        
        combined_date = self.date
        combined_hr = self.heart_rate + other.heart_rate
        combined_steps = self.steps + other.steps
        combined_calories = self.calories + other.calories
        combined_walking_time = self.walking_time + other.walking_time

        return FitnessEntry(combined_date, combined_hr, combined_steps, combined_calories, combined_walking_time,)
    
    def __eq__(self, other):
        """
        This function compares two FitnessEntry objects for equality. Entries are considered
        equal if all fields match within a small tolerance for floating values.
        """
        if not isinstance(other, FitnessEntry):
            return False
        return(self.date == other.date and
               self.heart_rate == other.heart_rate and
               self.steps == other.steps and
               abs(self.calories - other.calories) < 1e-9 and
               abs(self.walking_time -other.walking_time) < 1e-9)
    
    def toTuple(self):
        """
        This function returns the entry's data as a tuple containing:
        date, heart_rate, steps, calories, walking_time.
        """
        return(self.date, self.heart_rate, self.steps, self.calories, self.walking_time)
    
    def isIrregularHr(self, low = 40, high = 180):
        """
        This function returns True if the heart rate is outside the normal range defined
        by the 'low' and 'high' thresholds.
        """
        return not (low <= self.heart_rate <= high)
    
    def stepsToMiles(self, stride_length = 0.762):
        """
        This function converts the number of steps into miles using the provided stride
        length (default is 0.762 meters per step). Returns the distance
        in miles.
        """
        meters = self.steps * stride_length
        miles = meters / 1609.34
        return miles
