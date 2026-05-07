class InvalidEntryError(Exception):
    """
    Base exception when something is wrong with an entry
    Other more specific exceptions inherit from this one
    """
    pass

class InvalidFitnessEntryError(ValueError):
    """
    Exception is thrown when attempting to create a FitnessEntry with bad data. 
    For instance: negative heart rate, steps, date in wrong format, etc.
    This inherits from ValueError which is built-in Python for invalid values
    """
    pass

class DataFormatError(Exception):
    """
    Exception is thrown when CSV files has missing columns or is malformed.
    This is used during file loading when the data structure is wrong
    """
    pass
