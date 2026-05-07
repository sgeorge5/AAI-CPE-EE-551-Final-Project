import math
def convert_steps_to_miles(steps_list):

    return list(map(lambda s: math.floor(s * 0.0005), steps_list))

def filter_high_heart_rate(entries, threshold):

    return list(filter(lambda e: e.heart_rate > threshold, entries))


def get_step_counts(entries):

    return [e.steps for e in entries]


def recursive_sum_steps(entries, n):
 
    if n == 0:
        return entries[0].steps

    return entries[n].steps + recursive_sum_steps(entries, n - 1)


def iter_heart_rates(entries):


    # Yield one heart rate at a time
    for e in entries:
        yield e.heart_rate
