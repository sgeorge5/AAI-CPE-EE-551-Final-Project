# Personal Fitness Data Tracker & Analyzer

## Team Members:

- Miguel Hernandez (Stevens ID: 20024615 , E-mail: mhernand2@stevens.edu)
- Shaun George (Stevens ID: 20019967, E-mail: sgeorge5@stevens.edu)
- Aayush Gunjal (Stevens ID: 10479416 , E-mail: agunjal@stevens.edu),

## Project Description
Modular Python application: 
- tracks fitness data, processes it, and generates both textual reports and visualizations for multiple users.
- combines data processing, object‑oriented design, error handling, and basic data visualization into a cohesive analytics pipeline.
## How to Run Program

## Main Contributions of the Team

Shaun: 
- Focused on program structure and class design, providing the initial skeleton that guided the team's development
- Implemented the core data model, CSV loading logic, and statistical analysis functions
- Added required special methods to the FitnessEntry class
- Implemented loop statements for iterating through entries and conditional statements for data validation throughout core modules
- Ensured all classes and methods in implemented files contained proper docstrings and comments

Miguel: 
- Handled data processing and external library integration, specifically implementing visualization.py with matplotlib for generating step trends, heart rate trends, and step distribution histograms
- Created exceptions.py with custom exception classes for robust error handling
- Implemented required data input and output features through CSV loading validation
- Developed functions that processed and analyzed the data
- Wrote pytest test cases to validate file loading, missing columns, and FitnessEntry validation logic

Aayush:
- Managed error handling, documentation, and project organization
- Implemented user_profile.py for managing collections of fitness entries with add, remove, filter, and lookup methods
- Created utils.py with helper functions including step-to-miles conversion, high heart rate filtering, list comprehension for step extraction, recursive step summation, and a generator function for heart rate iteration
- Implemented at least two exception handling scenarios to improve program reliability
- Organized project file structure and finalized the README file with setup instructions, dependencies, and contribution details
- Integrated all modules into main.ipynb for sequential program execution
