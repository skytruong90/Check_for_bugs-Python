# Title: Bug Checker
I created a script in Python that uses the built-in pylint library to check for potential bugs in a Python code file.

## Summary:
This script uses the pylint library, which is a popular tool for analyzing and checking Python code for potential errors and bugs. It defines a check_for_bugs() function that takes a filename as an argument, and then calls the pylint.lint.Run() method to analyze the file and produce an output with potential bugs and issues.

To use this script, simply replace 'example.py' with the name of the Python file you want to check, and then run the script. The pylint library will generate a detailed report of any issues or potential bugs in the code, which can then be addressed and fixed.

## How to use:
To use the script, follow these steps:
1. Save the script to a file on your local machine with a .py extension, such as check_for_bugs.py.
2. Open a command-line interface or terminal on your machine.
3. Navigate to the directory where the script is saved.
4. Run the script by entering python check_bugs.py in the command line, replacing check_bugs.py with the name of the file you saved the script as.
5. The script will prompt you to enter the file name of the code file you want to check for bugs. Type in the name of the file, including the file extension (e.g. example.py), and press Enter.
6. The script will then run and generate a report of any potential issues or bugs in the code file you specified.
7. Review the report and make any necessary changes to address the issues identified.

Note that you will need to have Python installed on your machine in order to run the script. You may also need to install the pylint library if it is not already installed. You can install pylint using the command pip install pylint in your command-line interface or terminal.
