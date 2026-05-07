import math


def convert_steps_to_miles(steps_list):


    # Convert each step count into miles and round down
    return list(map(lambda s: math.floor(s * 0.0005), steps_list))
