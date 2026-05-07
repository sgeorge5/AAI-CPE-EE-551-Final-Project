import math


def convert_steps_to_miles(steps_list):


    # Convert each step count into miles and round down
    return list(map(lambda s: math.floor(s * 0.0005), steps_list))
    
def filter_high_heart_rate(entries, threshold):
    return list(filter(lambda e: e.heart_rate > threshold, entries))


def get_step_counts(entries):
