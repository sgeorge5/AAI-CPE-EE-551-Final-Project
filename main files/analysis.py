import numpy as np
from utils import iter_heart_rates

"""
This python code provides basic statistical analysis for FitnessEntry objects,
including averages, peak values, standard deviations, and a formatted summary report.
"""

def compute_averages(entries):
    """
    Compute the average heart rate, steps, calories, and walking time
    across all FitnessEntry objects in the list. And then Returns a dictionary
    containing the average values for each metric.
    """
    # Collect values into lists for easier processing
    heart_rates = []
    steps_list = []
    calories_list = []
    walking_times = []

    for e in entries:
        heart_rates.append(e.heart_rate)
        steps_list.append(e.steps)
        calories_list.append(e.calories)
        walking_times.append(e.walking_time)

    # Compute averages using NumPy
    return {
        "avg_heart_rate": float(np.mean(heart_rates)),
        "avg_steps": float(np.mean(steps_list)),
        "avg_calories": float(np.mean(calories_list)),
        "avg_walking_time": float(np.mean(walking_times)),
    }


def compute_peaks(entries):
    """
    Find the maximum (peak) heart ratem steps, calories, and walking time
    among all FitnessEntry objects. Returns a dictionary containing the highest 
    value for each metric.
    """
    # initialize peaks
    max_hr = 0
    max_steps = 0
    max_cal = 0
    max_walk = 0

    # loop through entries and update peaks.
    for e in entries:
        if e.heart_rate > max_hr:
            max_hr = e.heart_rate
        if e.steps > max_steps:
            max_steps = e.steps
        if e.calories > max_cal:
            max_cal = e.calories
        if e.walking_time > max_walk:
            max_walk = e.walking_time

    return {
        "max_heart_rate": max_hr,
        "max_steps": max_steps,
        "max_calories": max_cal,
        "max_walking_time": max_walk,
    }


def compute_stddev(entries):
    """
    Compute the standard deviation for heart rate and steps using NumPy.
    Heart rate values are obtained using a generator from utils.py. This 
    function returns a dictionary containing the two standard deviation values.
    """
    # Use generator for heart rate values.
    hr_values = list(iter_heart_rates(entries))
    # List comprehension for steps values.
    step_values = [e.steps for e in entries]

    return {
        "std_heart_rate": float(np.std(hr_values)),
        "std_steps": float(np.std(step_values)),
    }


def generate_report(user_profile):
    """
    Print a formatted fitness report for the given UserProfile. 
    The report includes total number of days, average values, peak values,
    and standard deviations for heart rate and steps. If the profile has no entries, 
    a message indicating that no data is available will be printed instead.
    """
    entries = user_profile.entries

    # Handle empty dataset case.
    if len(entries) == 0:
        print("No fitness data available.")
        return

    # compute all metrics
    avg = compute_averages(entries)
    peaks = compute_peaks(entries)
    std = compute_stddev(entries)

    # Print formatted report to the console.
    print("\n===== FITNESS REPORT =====")
    print(f"Total Days: {len(entries)}\n")

    print("Averages:")
    print(f"  Heart Rate: {avg['avg_heart_rate']:.2f} bpm")
    print(f"  Steps: {avg['avg_steps']:.2f}")
    print(f"  Calories: {avg['avg_calories']:.2f}")
    print(f"  Walking Time: {avg['avg_walking_time']:.2f} min\n")

    print("Peaks:")
    print(f"  Max Heart Rate: {peaks['max_heart_rate']}")
    print(f"  Max Steps: {peaks['max_steps']}")
    print(f"  Max Calories: {peaks['max_calories']}")
    print(f"  Max Walking Time: {peaks['max_walking_time']} min\n")

    print("Variability (Standard Deviation):")
    print(f"  Heart Rate Std Dev: {std['std_heart_rate']:.2f}")
    print(f"  Steps Std Dev: {std['std_steps']:.2f}")

    print("===========================\n")
