drip-filter (Python Edition) ☕
Filters through data like a slow drip coffee machine — thoughtful, clean, and efficient.


📝 Overview
Drip-Filter (by SoftStack Studios) is a robust terminal-based tool for sorting and filtering user datasets. Using a "slow-pour" philosophy, it allows you to sift through large JSON files to find exactly who you are looking for, with a UI that is as friendly as your favorite barista.


⚙️ Features
Multi-Criteria Filtering: Sift through data by Age, City, Name, or ID.

Range Logic: Built-in "min/max" filtering for numerical data (Age and ID).

Object-Oriented Design: Data is converted from raw JSON into a managed User class for better attribute handling.

Friendly UI: Custom error handling with fun, "Scooby-Doo" inspired prompts (Zoinks! Jinkies!).

Data Persistence: Save your filtered "brew" into a new JSON file to keep your results for later.


🧰 Tech Stack
Python 3: The core engine of the filtering logic.

JSON: Used for both input data and filtered output.

OS Module: For smart file path checking and system management.


🚀 Getting Started
Ensure your main.py, user.py, and your JSON data file are in the same folder.

Run the program:

Bash

python main.py
Enter your filename (e.g., data.json) when prompted.

Follow the Filter Fun Menu to refine your data!


♿ Accessibility Notes
Terminal Friendly: Designed to work perfectly with screen readers in a CLI environment.

Input Validation: Robust error checking ensures the program doesn't crash on typos or invalid numbers.

Clear Hierarchy: Uses ASCII formatting (=======) to create a visual structure for keyboard users.


📸 Screenshots
The Welcome Menu
The Filtered Result


✨ Future Plans
Dynamic Attribute Filtering: Allow users to filter by any key found in the JSON file automatically.

Visual Reports: Export the results into the "CodeLatte" web dashboard.
