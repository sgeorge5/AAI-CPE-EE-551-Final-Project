"""
visualization.py
Generates Matplotlib plots for FitnessEntry data. It displays:
Daily Steps Trend (sampled), Daily Heart Rate Trend (sampled), and
Steps Distribution (histogram)
All functions use basic Python and Matplotlib only.
"""

import matplotlib.pyplot as plt


def plot_steps_trend(entries):
    """
    Takes in a list of the fitness entries and draws a blue line chart that
    show the step counts over time. Then it samples every 100th entry so the x-axis 
    does not get too crowded
    """
    import matplotlib.pyplot as plt

    #every 1000th entry is grabbed to create a cleaner plot
    sampled = entries[::1000]

    #data and steps are pulled from each sampled entry into separate lists
    dates = [e.date for e in sampled]
    steps = [e.steps for e in sampled]

    #creates a figure sized 10x4
    plt.figure(figsize=(10, 4))
    #draws blue line to connect data points
    plt.plot(dates, steps, color="blue")
    plt.title("Daily Steps Trend (sampled)")
    plt.xlabel("Date")
    plt.ylabel("Steps")
    #limits x-axis to max 10 labels so there is no overlap
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
    #dates are rotated 45degrees and decreases text size to fit
    plt.gca().tick_params(axis='x', labelrotation=45, labelsize=8)

    #prevents labels fromgetting cut off at edges
    plt.tight_layout()
    #pops up the plot window
    plt.show()


def plot_heart_rate_trend(entries):
    """
    Takes in list of fitness entries and draws a red line chart showing the
    heart rate over time. Then the same sampling strategy as before (steps plot)
    is used but uses a red color to differentiate them
    """
    import matplotlib.pyplot as plt

    #decreases clutter by samping every 1000th entry
    sampled = entries[::1000]
    #builds list for x axis dates and y axist heart rates
    dates = [e.date for e in sampled]
    hr = [e.heart_rate for e in sampled]

    plt.figure(figsize=(10, 4))
    #red line distinguishes from blue steps plot
    plt.plot(dates, hr, color="red")
    plt.title("Daily Heart Rate Trend (sampled)")
    plt.xlabel("Date")
    plt.ylabel("Heart Rate (bpm)")
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
    plt.gca().tick_params(axis='x', labelrotation=45, labelsize=8)

    plt.tight_layout()
    plt.show()
