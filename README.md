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
   git clone https://github.com/diogoantunes291/general-helpers.git
   cd general-helpers

2. Run replaceHeaders.py to process CSV files in a given directory:
   
   python replaceHeaders.py /path/to/source_directory

3.The script will:

   - Locate a folder containing "CSVs"
   - Identify .csv files inside the folder
   - Replace underscores _ with dots . in headers


Dependencies

   - Python 3.x
   - No external libraries required (only standard Python modules)


Future Improvements

   - Expand the generalHelpers library with additional automation functions
   - Enhance error handling for CSV processing
   - Optimize performance for handling large datasets
