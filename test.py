# Build a Python application that can execute a command line and display the 
# installed version of Python. Use “python -V” to get python version information.

import subprocess

# Define the command to execute
command = "python -V"

# Execute the command and capture the output
output = subprocess.check_output(command.split())

# Decode the output as a string and print it to the console
print(output.decode("utf-8"))




