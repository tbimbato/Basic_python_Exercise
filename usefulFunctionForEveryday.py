# in this python script you can find:
# - a function to get the current date and time
# - a function to add days to the current date
# - a function to convert a string to uppercase
# - a function to read the first line of a file
# - a function to write a list of lines to a file
# - a function to check if a file exists
# - a main function to demonstrate the usage of utility functions


import os
from datetime import datetime, timedelta

# Function to get the current date and time
def get_current_time():
    """Return the current date and time as a formatted string."""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Function to add days to the current date
def add_days_to_date(days):
    """Add a specific number of days to the current date and return the new date as a string."""
    new_date = datetime.now() + timedelta(days=days)
    return new_date.strftime("%Y-%m-%d")

# Function to convert a string to uppercase
def convert_to_uppercase(text):
    """Convert a string to uppercase."""
    return text.upper()

# Function to read the first line of a file
def read_first_line(filename):
    """Read and return the first line of a text file."""
    with open(filename, 'r') as file:
        first_line = file.readline().strip()
    return first_line

# Function to write a list of lines to a file
def write_lines_to_file(filename, lines):
    """Write a list of strings to a file, each string on a new line."""
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')

# Function to check if a file exists
def file_exists(filename):
    """Check if a file exists in the current directory."""
    return os.path.exists(filename)

# Main function to demonstrate the usage of utility functions
def main():
    print("Current Time:", get_current_time())
    print("Date 10 days from now:", add_days_to_date(10))
    print("Uppercase conversion:", convert_to_uppercase("hello world"))
    
    test_filename = 'test.txt'
    if file_exists(test_filename):
        print("First line of the file:", read_first_line(test_filename))
    else:
        print("File does not exist, creating file and writing lines...")
        write_lines_to_file(test_filename, ["Line 1", "Line 2", "Line 3"])
        print("First line of the newly created file:", read_first_line(test_filename))

if __name__ == "__main__":
    main()