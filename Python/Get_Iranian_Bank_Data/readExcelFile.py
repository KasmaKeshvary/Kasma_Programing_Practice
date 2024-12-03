import os
import time
import subprocess
import pandas as pd
from pywinauto import Application

# Path to your Excel file in the Downloads folder
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
file_name = "Data.xls"  # Original Excel file name
file_path = os.path.join(downloads_folder, file_name)

# Function to open the Excel file and handle dialogs
def open_excel_and_save_data(file_path, new_file_path):
    if os.path.isfile(file_path):
        try:
            # Open the file using the default program associated with .xls files
            subprocess.Popen(['start', '', file_path], shell=True)
            print(f"{file_name} is being opened.")

            time.sleep(5)  # Wait for the application to start and the dialog to appear
            
            # Connect to the Excel application
            app = Application(backend='uia').connect(path="EXCEL.EXE")

            # Handle the initial warning dialog
            dialog = app.window(title_re=".*Excel.*")
            dialog.wait('visible')
            time.sleep(1)  # Ensure the dialog is visible
            
            dialog.Yes.click()  # Click the "Yes" button
            print("Clicked 'Yes' on the warning dialog.")

            # Wait for the Excel window to be ready
            time.sleep(5)

            # Handle Protected View and Enable Editing
            excel_window = app.window(title_re=".*Excel.*")
            enable_edit_button = excel_window.child_window(title="Enable Editing", control_type="Button")

            # Check if the Enable Editing button is present and click it
            if enable_edit_button.exists(timeout=10):  # Wait a maximum of 10 seconds for the button to appear
                enable_edit_button.click()
                print("Clicked 'Enable Editing'.")
                time.sleep(2)  # Wait for the action to complete

            # Wait a moment for Excel to process the button click
            time.sleep(3)

            # After enabling editing, read the data using pandas directly from the initial file path
            # Here we assume the file is now accessible for reading
            df = pd.read_excel(file_path)  # You can specify the engine if needed
            print("Data read successfully.")
            
            # Save the data to a new Excel file
            df.to_excel(new_file_path, index=False)
            print(f"Data has been copied and saved to {new_file_path}.")

        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print(f"The file {file_name} does not exist in {downloads_folder}.")

# Specify where to save the new Excel file
new_file_name = "Copied_Data.xlsx"
new_file_directory = os.path.join(os.path.expanduser("~"), "Desktop", new_file_name)  # Change this path as needed

# Optionally wait for a couple of seconds before running the function
time.sleep(2)  # Adding a wait time before opening the file
open_excel_and_save_data(file_path, new_file_directory)
