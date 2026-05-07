from fitness_entry import FitnessEntry
"""
Represents a single day's fitness data with validation and operator support.
"""

class UserProfile:
    """
    Represents a user's collection of FitnessEntry objects.
    """

    def __init__(self, name):
        """
        Initialize a UserProfile with a name and an empty list of entries.
        """
        self.name = name
        self.entries = []

    def add_entry(self, entry):
        """
        Add a FitnessEntry to the profile.
        """
        if isinstance(entry, FitnessEntry):
            self.entries.append(entry)
        else:
            print("Cannot add entry: not a FitnessEntry object.")

    def remove_entry_by_date(self, date_str):
        """
        Remove the first entry that matches the given date.
        """
        for e in self.entries:
            if e.date == date_str:
                self.entries.remove(e)
                return True
        return False

    def get_entry_by_date(self, date_str):
        """
        Return the FitnessEntry for a specific date, or None if not found.
        """
        for e in self.entries:
            if e.date == date_str:
                return e
        return None

    def filter_by_steps(self, min_steps):
        """
        Return a list of entries where steps >= min_steps.
        """
        return [e for e in self.entries if e.steps >= min_steps]

    def total_entries(self):
        """
        Return the number of FitnessEntry objects stored.
        """
        return len(self.entries)

    def __len__(self):
        """
        Allow len(user_profile) to return number of entries.
        """
        return len(self.entries)

    def __str__(self):
        """
        Simple readable summary of the profile.
        """
        return f"UserProfile(name={self.name}, entries={len(self.entries)})"
