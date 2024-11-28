import subprocess
import os
import glob

# Path to your directory
directory = r"C:\Users\Kasma\Desktop\Kasma_Programming_Practice\Python\Get_Iranian_Bank_Data\Ready_To_Run"

# Change the current working directory to your target directory
os.chdir(directory)

# Use glob to find all Python files in the directory
python_files = glob.glob("*.py")

# Run each Python file one by one
for filename in python_files:
    print(f"Running {filename}...")
    subprocess.run(['python', filename], check=True)  # Wait for each to finish
    print(f"Finished {filename}.")
