from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Specify the path to your ChromeDriver
service = Service(r'C:\Users\Kasma\Desktop\Kasma_Programming_Practice\Python\chromedriver.exe')

# Initialize the WebDriver using the Service
driver = webdriver.Chrome(service=service)

# Open a URL
driver.get('https://www.edbi.ir/web_directory/41640-%D8%B4%D8%B9%D8%A8-%D8%AF%D8%A7%D8%AE%D9%84%DB%8C.html')  # Replace with the actual URL you want to visit

# Get the complete HTML of the page
html_content = driver.page_source
# print("HTML Content:")
# print(html_content)  # This will print the entire HTML

# Close the driver
driver.quit()

# Save HTML content to a file
with open('toseesaderat_Bank_branches.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
