# Personal Fitness Data Tracker & ANalyzer

## Team Members:

- Miguel Hernandez (Stevens ID: 20024615 , E-mail: mhernand2@stevens.edu)
- Shaun George (Stevens ID: 20019967, E-mail: sgeorge5@stevens.edu)
- Aayush Gunjal (Stevens ID: 10479416 , E-mail: agunjal@stevens.edu),

## Project Description

## How to Run Program

This section explains, the steps in detail how to successfully clone this Github repository and run the program:

### 1. Clone the Repository

- It is recommended to use git for this part (Download Link for Git: https://git-scm.com/)
- Open VS Code (or your preferred IDE/terminal)
- In the terminal, choose a folder or create a new one for where you would like the project to be saved/cloned
- Run this command to clone the entire repository: git clone https://github.com/sgeorge5/AAI-CPE-EE-551-Final-Project.git
- navigate/change into the project directory by using the command: cd AAI-CPE-EE-551-Final-Project
- Inside the project directory should contain a folder named "main files" and a README.md file
- Inside the "main files" folder, there should be 9 python files, a .csv file and a folder named "tests"
- Inside the folder named "tests" there should be 2 more python files.
- If your project directory matches the description above and is similar to the directory of our GitHub repository, then you have successfully cloned our python project repository.

### 2. Open the Project in VSCode

- In the terminal after you cloned the repository, type: code .
- This opens the project in VSCode.
- If you are having issues, then you can manually open the cloned project folder in VSCode. By navigating File -> Open Folder and opening the folder where you saved the cloned repository.

### 3. Running the interactive notebook (main.ipynb)

- Once you have successfully cloned this repository, navigate to the AAI-CPE-EE-551-FINAL-PROJECT -> main files -> main.ipynb
- In your preferred compiler, open the main.ipynb.
- Select a Python Kernel if prompted (your installed python environment)
- Run the cells in order (You can click "Run All" at the top of the notebook or run each cell individually by using the Run Cell button on each cell.)
- As you run the main.ipynb notebook the respective outputs will appear under each cell. Additionally, Plots and visualizations will appear inline in the notebook.

### 4. Running the main script (main.py)

- Make sure you are in the project root folder in the terminal(cd AAI-CPE-EE-551-Final-Project
  )
- Execute the script: python main.py
- This program will load tracher_fitness_data.csv, create user profiles, generate reports, and display visualizations all in the terminal window.
- Unlike main.ipynb, this version is non-interactive

### 5. Run Tests with pytest

- To run the pytest file under the test folder (test_data_loader.py and test_fitness_entry.py).
- Ensure you are still in the project root: (cd AAI-CPE-EE-551-Final-Project
  )
- To run all the tests run this command in the terminal: pytest
- To run a single test_data_loader.py pytest file, run: pytest tests/test_data_loader.py
- To run a single test_fitness_entry.py pytest file, run: pytest tests/test_fitness_entry.py

## Main Contributions of the Team

Shaun:

- focused program structure and class design.
- added the required special methods.
- Implemented loops and conditional statements
- Ensured that all classes and methods contained proper docstring and comments.

Miguel:

- handled the data processing and external library integration.
- implemented the required data input and output features
- developed functions that processed and analyzed the data.
- wrote pytest cases

Aayush:

- Error handling, documentation, and project organization.
- implemented at least two exception-handling scenarios to improve program reliability.
- organized the file structure.
- finalized the README file.
