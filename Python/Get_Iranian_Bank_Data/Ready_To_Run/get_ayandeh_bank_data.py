from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import os
import time
import sys
import mimetypes
import pandas as pd

name_condition = 'Data'
new_file_name = 'ayandeh_bank_branches_data'  # Desired new file name

config_directory = r'C:\Users\Kasma\Desktop\Kasma_Programming_Practice\Python\Get_Iranian_Bank_Data'
sys.path.append(config_directory)

from config import CHROMEDRIVER_PATH
from config import EXCEL_TARGET_DIRECTORY

# Set Chrome options to specify download location and behavior 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', {
    'download.default_directory': EXCEL_TARGET_DIRECTORY,  # Set the default download directory
    'download.prompt_for_download': False,           # Disable prompt for download
    'download.directory_upgrade': True,               # Allow directory upgrade
    'safebrowsing.enabled': True                       # Enable safe browsing
})

# Specify the path to your webdriver
service = Service(CHROMEDRIVER_PATH)

# Initialize the WebDriver using the Service
driver = webdriver.Chrome(service=service, options=chrome_options)

def is_file_downloaded(file_path):
    # Wait until the file is not being used anymore (i.e., size is static for a while)
    while True:
        initial_size = os.path.getsize(file_path)
        time.sleep(1)  # Wait for a second
        current_size = os.path.getsize(file_path)

        if initial_size == current_size:
            break  # File size has not changed, download seems complete.

try:
    # Open the URL
    driver.get('https://ba24.ir/ayandeh/branches')
    driver.maximize_window()
    time.sleep(5)

    a_tags = driver.find_elements(By.TAG_NAME, 'a')

    # Filter <a> tags that contain the specified string
    downloadButton = [a for a in a_tags if 'بخش1' in a.text]

    # downloadButton = advancedSearch.find_element(By.CLASS_NAME, 'btnSubmit')
    downloadButton[0].click()
    time.sleep(60)

    print(os.listdir(EXCEL_TARGET_DIRECTORY))

    # Wait for the download to complete
    download_wait_time = 30  # wait max 30 seconds
    start_time = time.time()

    while (time.time() - start_time) < download_wait_time:
        if any(fname.endswith(('.xls', '.xlsx')) for fname in os.listdir(EXCEL_TARGET_DIRECTORY)):
            break
        time.sleep(1)

    print(os.listdir(EXCEL_TARGET_DIRECTORY))
    # Check if any file containing 'BMIUnits' was downloaded
    found_file = None
    for filename in os.listdir(EXCEL_TARGET_DIRECTORY):
        if name_condition in filename and filename.endswith(('.xls', '.xlsx')):
            found_file = filename
            print(f'Found downloaded file: {found_file}')
            break  # Exit the loop once we find the desired file
    
    time.sleep(10)
    # If the file was found, rename it
    if found_file:
        file_path = os.path.join(EXCEL_TARGET_DIRECTORY, found_file)
        print(file_path)
        is_file_downloaded(file_path)  # Ensure the file download is complete

        # Read the first row of the Excel file
        try:
            df = pd.read_excel(file_path)  # Read the Excel file
            first_row = df.iloc[0]  # Get the first row
            print("First row of data:")
            print(first_row)  # Print the first row data
        except Exception as e:
            print(f"Error reading Excel file: {e}")

        # Determine the new file extension based on the original file
        _, file_extension = os.path.splitext(found_file)  # Get current file extension

        # Construct the new file name with the same extension
        new_file_path = os.path.join(EXCEL_TARGET_DIRECTORY, new_file_name + file_extension)

        # Rename the file
        os.rename(file_path, new_file_path)
        print(f'Renamed downloaded file to: {new_file_name + file_extension}')

        # old_file_path = os.path.join(EXCEL_TARGET_DIRECTORY, found_file)
        # new_file_path = os.path.join(EXCEL_TARGET_DIRECTORY, new_file_name)
        # os.rename(old_file_path, new_file_path)
        # print(f'Renamed downloaded file to: {new_file_name}')

    else:
        print(f"No file containing {name_condition} was found.")

finally:
    # Close the driver
    driver.quit()