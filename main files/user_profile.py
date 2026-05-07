"""
User profile module for managing fitness tracking data.

This module defines the UserProfile class, which stores and manages
a collection of FitnessEntry objects for an individual user.
Class Functions:
- Adding and removing entries
- Searching entries by date
- Filtering entries by step count
- Counting stored entries
- Custom string representation
"""

from fitness_entry import FitnessEntry


class UserProfile:
    """
    Represents a user's collection of FitnessEntry objects.

    Each profile stores:
    - The user's name
    - A list of fitness entries associated with the user

    The class provides methods for managing and querying
    fitness tracking data.
    """

    def __init__(self, name):
        """
        Initialize a UserProfile object.

        Parameters:
            name (str):
                The name of the user.

        Attributes:
            name (str):
                Stores the user's name.

            entries (list):
                A list used to store FitnessEntry objects.
        """

        # Store the user's name
        self.name = name

        # Initialize an empty list for fitness entries
        self.entries = []

    def add_entry(self, entry):
        """
        Add a FitnessEntry object to the user's profile.

        The method first validates that the provided object
        is an instance of the FitnessEntry class.

        Parameters:
            entry (FitnessEntry):
                The fitness entry to add.

        Returns:
            None
        """

        # Ensure the object is a valid FitnessEntry
        if isinstance(entry, FitnessEntry):

            # Add the entry to the profile
            self.entries.append(entry)

        else:
            # Display an error message for invalid objects
            print("Cannot add entry: not a FitnessEntry object.")

    def remove_entry_by_date(self, date_str):
        """
        Remove the first fitness entry that matches a given date.

        Parameters:
            date_str (str):
                The date string to search for.

        Returns:
            bool:
                True if an entry was removed,
                False if no matching entry was found.
        """

        # Search through all entries
        for e in self.entries:

            # Check if the entry date matches
            if e.date == date_str:

                # Remove the matching entry
                self.entries.remove(e)

                return True

        # Return False if no matching entry exists
        return False

    def get_entry_by_date(self, date_str):
        """
        Retrieve a fitness entry for a specific date.

        Parameters:
            date_str (str):
                The date string to search for.

        Returns:
            FitnessEntry or None:
                The matching entry if found,
                otherwise None.
        """

        # Search through all entries
        for e in self.entries:

            # Return the matching entry
            if e.date == date_str:
                return e

        # Return None if no match is found
        return None

    def filter_by_steps(self, min_steps):
        """
        Filter entries by minimum step count.

        Parameters:
            min_steps (int):
                The minimum number of steps required.

        Returns:
            list:
                A list of FitnessEntry objects where
                steps are greater than or equal to min_steps.
        """

        # Return only entries meeting the step requirement
        return [e for e in self.entries if e.steps >= min_steps]

    def total_entries(self):
        """
        Return the total number of fitness entries stored.

        Returns:
            int:
                The number of FitnessEntry objects in the profile.
        """

        # Return the size of the entries list
        return len(self.entries)

    def __len__(self):
        """
        Return the number of entries using len().

        This special method allows:
            len(user_profile)

        Returns:
            int:
                The number of stored fitness entries.
        """

        # Return total number of entries
        return len(self.entries)

    def __str__(self):
        """
        Return a readable string representation of the profile.

        Returns:
            str:
                A formatted summary of the user's profile.
        """

        # Return a formatted profile summary string
        return f"UserProfile(name={self.name}, entries={len(self.entries)})"
