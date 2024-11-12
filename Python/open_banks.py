import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Load the Excel file
excel_file_path = r"C:\Users\Kasma\Desktop\Kasma_Programming_Practice\Python\Iranian_Banks.xlsx"  # Update this path
data = pd.read_excel(excel_file_path)

service = Service(r'C:\Users\Kasma\Desktop\Kasma_Programming_Practice\Python\chromedriver.exe')

# Initialize the WebDriver using the Service
driver = webdriver.Chrome(service=service)

# Iterate through each link and open it in a new tab
for index, row in data.iterrows():
    link = row['Link']
    # Open a new tab for each link
    driver.execute_script("window.open(arguments[0]);", link)
    time.sleep(2)  # Pause to allow the tab to load (optional)

# If you want to keep the browser open, uncomment the next line:
input("Press Enter to close the browser...") 

# Close the driver (will close all tabs)
driver.quit()
