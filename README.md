# General Helpers (Python Utilities)

This repository contains a set of reusable Python utilities, including local library functions and automation scripts for handling CSV files.

## Features
- **Roman numeral to integer conversion** (generalHelpers library)
- **CSV directory search & processing** (`replaceHeaders.py`)
- **CSV header formatting** (Replacing `_` with `.` dynamically)
- **Future-proof reusable functions for automation tasks**

## Usage
1. Clone the repository:  
   ```bash
   git clone https://github.com/diogoantunes291/generalHelpers.git
   cd generalHelpers

2. Run replaceHeaders.py to process CSV files in a given directory:
   
   python replaceHeaders.py /path/to/source_directory

3.The script will:

   - Locate a folder containing "CSVs"
   - Identify .csv files inside the folder
   - Replace underscores _ with dots . in headers

## Why was the script replaceHeaders.py made?

 - The replaceHeaders script was developed to meet a specific request from the company's scientific department: modifying CSV headers by replacing underscores (_) with dots (.). This adjustment enhances readability and ensures consistency with the department's data formatting standards.

 - However, since dots (.) have significant functional meaning in programming (e.g., attribute access in Python), altering the headers at the source could introduce unintended issues. To ensure a safe, flexible, and reversible approach, this script dynamically processes CSV files within a designated directory, modifying only the first line (headers) while preserving the integrity of the dataset.

 - This solution provides a quick and effective way to standardize file formatting without compromising the underlying data structure or functionality.


## Dependencies

   - Python 3.x
   - No external libraries required (only standard Python modules)


## Future Improvements

   - Expand the generalHelpers library with additional automation functions
   - Enhance error handling for CSV processing
   - Optimize performance for handling large datasets
