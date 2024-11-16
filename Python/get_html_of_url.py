from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Specify the path to your ChromeDriver
service = Service(r'C:\Users\Kasma\Desktop\Kasma_Programming_Practice\Python\chromedriver.exe')

# Initialize the WebDriver using the Service
driver = webdriver.Chrome(service=service)

# Open a URL
driver.get('https://www.middleeastbank.ir/page/branches')  # Replace with the actual URL you want to visit

# Get the complete HTML of the page
html_content = driver.page_source
# print("HTML Content:")
# print(html_content)  # This will print the entire HTML

# Close the driver
driver.quit()

# Save HTML content to a file
with open('khavarmianeh_Bank_branches.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
