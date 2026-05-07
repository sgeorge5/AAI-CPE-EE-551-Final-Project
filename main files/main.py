"""
Main entry point for the fitness tracker analysis program.

1. Loads fitness tracking data from a CSV file.
2. Creates user profiles for multiple users.
3. Assigns fitness entries to users.
4. Generates summary reports.
5. Displays visualizations for fitness trends.

Modules imported:
- data_loader: Handles loading fitness data from files.
- exceptions: Contains custom exception classes.
- user_profile: Defines the UserProfile class.
- analysis: Generates fitness analysis reports.
- visualization: Creates charts and graphs.
"""
from data_loader import load_fitness_data
from exceptions import DataFormatError
from user_profile import UserProfile
from analysis import generate_report
from visualization import (
    plot_steps_trend,
    plot_heart_rate_trend,
    plot_steps_histogram
)


def main():
    """
    Main driver function for the fitness tracking application.

    Workflow:
    - Load fitness data from a CSV file.
    - Handle possible file or formatting errors.
    - Create user profiles.
    - Distribute fitness entries among users.
    - Generate reports and visualizations for each user.

    Exceptions handled:
    - FileNotFoundError:
        Raised if the CSV data file cannot be found.
    - DataFormatError:
        Raised if the CSV file contains invalid or corrupted data.
    """

    try:
        # Load fitness data entries from the CSV file
        entries = load_fitness_data("tracker_fitness_data.csv")

    except FileNotFoundError:
        # Handle missing file errors
        print("Error: tracker_fitness_data.csv not found.")
        return

    except DataFormatError as e:
        # Handle invalid data formatting issues
        print("Data format error:", e)
        return

    # List of user names for creating user profiles
    names = ["Shaun", "Miguel", "Ayush"]

    # Create a UserProfile object for each user
    profiles = [UserProfile(name) for name in names]

    # Distribute fitness entries evenly among the users
    # using round-robin assignment
    i = 0
    for e in entries:
        profiles[i % 3].add_entry(e)
        i = i + 1

    # Generate reports and visualizations for each user profile
    for p in profiles:

        # Print a section header for the current user
        print(f"\n ---- Report for {p.name} ----")

        # Display the number of entries assigned to the user
        print(f"Entries: {len(p.entries)}")

        # Generate and display a fitness analysis report
        generate_report(p)

        # Only generate charts if the user has fitness entries
        if len(p.entries) > 0:

            # Plot daily step count trends
            plot_steps_trend(p.entries)

            # Plot heart rate trends over time
            plot_heart_rate_trend(p.entries)

            # Plot a histogram of step count distribution
            plot_steps_histogram(p.entries)


# Execute the program only if this file is run directly
if __name__ == "__main__":
    main()
