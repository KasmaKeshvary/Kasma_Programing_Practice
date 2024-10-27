from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Specify the path to your ChromeDriver
service = Service(r'C:\Users\Kasma\Desktop\Kasma_Programming_Practice\Python\chromedriver.exe')

# Initialize the WebDriver using the Service
driver = webdriver.Chrome(service=service)

# Open a URL
driver.get('https://units.bmi.ir/fa/?smnuid=10011445')  # Replace with the actual URL you want to visit

# Get and print the page title
title = driver.title
print("Page Title:", title)

# Get the complete HTML of the page
html_content = driver.page_source
print("HTML Content:")
print(html_content)  # This will print the entire HTML

# Get and print all headings
headings = driver.find_elements(By.TAG_NAME, 'h1') + driver.find_elements(By.TAG_NAME, 'h2') + driver.find_elements(By.TAG_NAME, 'h3')
for heading in headings:
    print("Heading:", heading.text)

# Get and print all paragraphs
paragraphs = driver.find_elements(By.TAG_NAME, 'p')
for paragraph in paragraphs:
    print("Paragraph:", paragraph.text)

# Close the driver
driver.quit()

# Save HTML content to a file
with open('page_content_units_interior_two.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
