class InvalidEntryError(Exception):
    """
    Raised when a Genric invalid entry is encountered.
    """
    pass

class InvalidFitnessEntryError(ValueError):
    """
    Raised when a FitnessEntry cannot be constructed with the provided data.
    """
    pass

class DataFormatError(Exception):
    """
    Raised when input data is missing the required columns. or is malformed.
    """
    pass