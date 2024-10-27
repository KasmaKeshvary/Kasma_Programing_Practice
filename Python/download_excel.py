from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Specify the path to your ChromeDriver
service = Service(r'C:\Users\Kasma\Desktop\Kasma_Programming_Practice\Python\chromedriver.exe')

# Initialize the WebDriver using the Service
driver = webdriver.Chrome(service=service)

# Open a URL
driver.get('https://units.bmi.ir/fa/?smnuid=10011445')  # Replace with the actual URL you want to visit

# Get and print the page title
title = driver.title
print("Page Title:", title)

# # Get and print the complete HTML of the page
# html_content = driver.page_source
# print("HTML Content:")
# print(html_content)  # This will print the entire HTML

# # Get and print all headings
# headings = driver.find_elements(By.TAG_NAME, 'h1') + driver.find_elements(By.TAG_NAME, 'h2') + driver.find_elements(By.TAG_NAME, 'h3')
# for heading in headings:
#     print("Heading:", heading.text)

# # Get and print all paragraphs
# paragraphs = driver.find_elements(By.TAG_NAME, 'p')
# for paragraph in paragraphs:
#     print("Paragraph:", paragraph.text)

# Assuming the download button has a specific class or ID
# Adjust the selector as necessary to target the download link/button
try:
    excel_link = driver.find_element(By.ID, 'MainContent_ucUnitList1_lnkExcelDownload')
    
    # Click the link to trigger the download
    excel_link.click()

    # Wait for the download to complete (adjust time if necessary)
    time.sleep(10)  # Make sure to wait enough time for the file to download

except Exception as e:
    print("Excel button not found:", e)

# Close the driver
driver.quit()
