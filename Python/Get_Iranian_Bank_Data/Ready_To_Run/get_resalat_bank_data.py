from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException  # Import here
import pandas as pd
import time

# Specify the path to your webdriver
service = Service(r'C:\Users\Kasma\Desktop\Kasma_Programming_Practice\Python\Get_Iranian_Bank_Data\Ready_To_Run\chromedriver.exe')

# Initialize the WebDriver using the Service
driver = webdriver.Chrome(service=service)

# Create a list to hold data
headers = []
data = []

try:
    # Open the URL
    driver.get('https://www.rqbank.ir/atmlist')


    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'thead')))

    # Extract header data
    thead = driver.find_element(By.TAG_NAME, 'thead')
    header_rows = thead.find_elements(By.TAG_NAME, 'th')  # Get all header cells
    headers = [header.text for header in header_rows]  # Save the header texts
    

    tbody = driver.find_element(By.TAG_NAME, 'tbody')
    rows = driver.find_elements(By.TAG_NAME, 'tr')

    for row in rows:
        
        try:
            
            columns = row.find_elements(By.TAG_NAME, 'td')
            # Append the column data to the list
            row_data = [column.text for column in columns]
            data.append(row_data)
            print(row_data)
        
        except StaleElementReferenceException:
            print("Encountered stale element reference exception. Continuing.")

        print()  # Add a newline for better readability

    df_branches = pd.DataFrame(data, columns=headers)  # Use the headers as columns
    df_branches.to_excel('resalat_bank_branches.xlsx', index=False)

finally:
    # Close the driver
    driver.quit()