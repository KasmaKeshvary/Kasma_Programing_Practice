from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time
import sys

name_condition = 'BMIUnits'
new_file_name = 'melli_bank_branches_data.xlsx'  # Desired new file name

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

try:
    # Open the URL
    driver.get('https://units.bmi.ir/fa/?smnuid=10011445')
    driver.maximize_window()
    time.sleep(5)

    wait = WebDriverWait(driver, 10)  
    wait.until(EC.presence_of_element_located((By.ID, 'MainContent_ucUnitList1_lnkExcelDownload')))

    downloadButton = driver.find_element(By.ID, 'MainContent_ucUnitList1_lnkExcelDownload')
    downloadButton.click()
    time.sleep(90)

    print(os.listdir(EXCEL_TARGET_DIRECTORY))
    # Wait for the download to complete
    download_wait_time = 30  # wait max 30 seconds
    start_time = time.time()

    while (time.time() - start_time) < download_wait_time:
        if any(fname.endswith(('.xls', '.xlsx')) for fname in os.listdir(EXCEL_TARGET_DIRECTORY)):
            break
        time.sleep(1)

    # Check if any file containing 'BMIUnits' was downloaded
    found_file = None
    for filename in os.listdir(EXCEL_TARGET_DIRECTORY):
        if name_condition in filename and filename.endswith(('.xls', '.xlsx')):
            found_file = filename
            print(f'Found downloaded file: {found_file}')
            break  # Exit the loop once we find the desired file

    # If the file was found, rename it
    if found_file:
        old_file_path = os.path.join(EXCEL_TARGET_DIRECTORY, found_file)
        new_file_path = os.path.join(EXCEL_TARGET_DIRECTORY, new_file_name)
        os.rename(old_file_path, new_file_path)
        print(f'Renamed downloaded file to: {new_file_name}')

    else:
        print(f"No file containing {name_condition} was found.")

finally:
    # Close the driver
    driver.quit()