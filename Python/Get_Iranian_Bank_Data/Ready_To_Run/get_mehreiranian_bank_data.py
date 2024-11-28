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
    driver.get('https://qmb.ir/Index.aspx?tempname=Branches&lang=1&sub=0')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'bankbranch')))
    
    checkbox_three = driver.find_element(By.ID,'checkbox3')
    checkbox_three_label = checkbox_three.find_element(By.TAG_NAME,'label')
    checkbox_three_label.click()

    checkbox_two = driver.find_element(By.ID,'checkbox2')
    checkbox_two_label = checkbox_two.find_element(By.TAG_NAME,'label')
    checkbox_two_label.click()
    # print(checkbox_two_label.get_attribute('innerHTML'))

    city_td = driver.find_element(By.XPATH, '//td[span[text()="شهر"]]')
    
    # Step 2: Get the parent <tr>
    parent_tr = city_td.find_element(By.XPATH, '..')
    
    # Step 3: Extract all <td> elements in this <tr>
    td_elements = parent_tr.find_elements(By.TAG_NAME, 'td')

    # # Step 4: Create an array with the text content from the <span> elements within the <td>
    headers = [td.find_element(By.TAG_NAME, 'span').get_attribute('innerHTML') for td in td_elements]
    print(headers)

    tables = driver.find_elements(By.TAG_NAME, 'table')
    
    # Loop through each table
    for table in tables:
        rows = table.find_elements(By.TAG_NAME, 'tr')  # Get all rows from the current table

        # Iterate through rows and print the data
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')  # Get table data cells
            row_data = []
            # Iterate through cells to find non-empty ones
            for i in range(len(cells)-1) :
                # if cells[i].text.strip() != '':  # Check if cell is not empty (strip to remove whitespace)
                    
                row_data.append(cells[i].text)
                    
            if row_data:

                data.append(row_data)


    # df = pd.DataFrame(data)
    # # df.columns = ['Column1', 'Column2', 'Column3']  # Replace with actual column names as needed
    # df.to_excel('mehreiranian_bank_data.xlsx', index=False)

    # # # Create a DataFrame and save to Excel
    # df_headers = pd.DataFrame(headers)  # Use the headers as columns
    # df_headers.to_excel('branch_data_headers.xlsx', index=False)

    df_branches = pd.DataFrame(data, columns=headers)  # Use the headers as columns
    df_branches.to_excel('mehreiranian_bank_branches.xlsx', index=False)

finally:
    # Close the driver
    driver.quit()