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

