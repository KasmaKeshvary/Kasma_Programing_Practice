from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException  # Import here

import pandas as pd
import time
import sys

config_directory = r'C:\Users\Kasma\Desktop\Kasma_Programming_Practice\Python\Get_Iranian_Bank_Data'
sys.path.append(config_directory)

from config import CHROMEDRIVER_PATH

# Specify the path to your webdriver
service = Service(CHROMEDRIVER_PATH)

# Initialize the WebDriver using the Service
driver = webdriver.Chrome(service=service)

# Create a list to hold data
headers = []
data = []

try:
    # Open the URL
    driver.get('https://bim.ir/fa-IR/Portal/5026/page/%D9%86%D8%B4%D8%A7%D9%86%DB%8C-%D8%B4%D8%B9%D8%A8')


    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'MasterTable_Default2006')))

    # Extract header data
    tables = driver.find_elements(By.CLASS_NAME, 'MasterTable_Default2006')
    header_rows = tables[0].find_elements(By.TAG_NAME, 'th')  # Get all header cells
    headers = [header.text for header in header_rows]  # Save the header texts
    # print(tables)
    for idx, table in enumerate(tables):
        # print(f"Table {idx + 1}:")

        tBodies = table.find_elements(By.TAG_NAME, 'tbody')
        
        for tbody in tBodies:
            try:
                # Find all rows in the current tbody
                rows = tbody.find_elements(By.TAG_NAME, 'tr')
                
                for row in rows:
                    # For each row, get all columns
                    columns = row.find_elements(By.TAG_NAME, 'td')
                    # Append the column data to the list
                    row_data = [column.text for column in columns]
                    data.append(row_data)
                    # print(row_data)

            except StaleElementReferenceException:
                print("Encountered stale element reference exception. Continuing.")

        print()  # Add a newline for better readability


    df_branches = pd.DataFrame(data, columns=headers)  # Use the headers as columns
    df_branches.to_excel('sanaatomadan_bank_branches.xlsx', index=False)




finally:
    # Close the driver
    driver.quit()