"""
Utility functions for processing and analyzing fitness tracker data.

- Step conversion utilities
- Heart rate filtering
- Step count extraction
- Recursive calculations
- Generator functions for heart rate iteration
"""

import math


def convert_steps_to_miles(steps_list):
    """
    Convert a list of step counts into approximate miles walked.

    Each step count is multiplied by a conversion factor
    (0.0005 miles per step) and rounded down to the nearest
    whole number using math.floor().

    Parameters:
        steps_list (list[int]):
            A list containing step counts.

    Returns:
        list[int]:
            A list of converted mile values.
    """

    # Convert each step count into miles and round down
    return list(map(lambda s: math.floor(s * 0.0005), steps_list))


def filter_high_heart_rate(entries, threshold):
    """
    Filter fitness entries based on heart rate.

    Returns only the entries where the heart rate exceeds
    the specified threshold value.

    Parameters:
        entries (list):
            A list of fitness entry objects containing
            a 'heart_rate' attribute.

        threshold (int):
            The minimum heart rate required for an entry
            to be included.

    Returns:
        list:
            A list of entries with heart rates above
            the threshold.
    """

    # Keep only entries with heart rates above the threshold
    return list(filter(lambda e: e.heart_rate > threshold, entries))


def get_step_counts(entries):
    """
    Extract step counts from fitness entries.

    Parameters:
        entries (list):
            A list of fitness entry objects containing
            a 'steps' attribute.

    Returns:
        list[int]:
            A list of step counts from all entries.
    """

    # Create a list containing only the step counts
    return [e.steps for e in entries]


def recursive_sum_steps(entries, n):
    """
    Recursively calculate the total number of steps.

    This function sums the steps from index 0 up to index n
    using recursion.

    Parameters:
        entries (list):
            A list of fitness entry objects containing
            a 'steps' attribute.

        n (int):
            The ending index for the recursive calculation.

    Returns:
        int:
            The total number of steps from entry 0 to entry n.
    """

    # Base case: return the first entry's steps
    if n == 0:
        return entries[0].steps

    # Recursive case: add current steps to previous total
    return entries[n].steps + recursive_sum_steps(entries, n - 1)


def iter_heart_rates(entries):
    """
    Generator function that yields heart rates one at a time.

    This allows heart rate values to be processed lazily
    instead of creating a full list in memory.

    Parameters:
        entries (list):
            A list of fitness entry objects containing
            a 'heart_rate' attribute.

    Yields:
        int:
            The heart rate of each fitness entry.
    """

    # Yield one heart rate at a time
    for e in entries:
        yield e.heart_rate
