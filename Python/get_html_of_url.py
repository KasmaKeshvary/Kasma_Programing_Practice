from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Specify the path to your ChromeDriver
service = Service(r'C:\Users\Kasma\Desktop\Kasma_Programming_Practice\Python\chromedriver.exe')

# Initialize the WebDriver using the Service
driver = webdriver.Chrome(service=service)

# Open a URL
driver.get('https://izbank.ir/fa/page/100691-%D8%AC%D8%B3%D8%AA%D8%AC%D9%88%DB%8C-%D9%BE%DB%8C%D8%B4%D8%B1%D9%81%D8%AA%D9%87.html#content_search_form_227285')  # Replace with the actual URL you want to visit

# Get the complete HTML of the page
html_content = driver.page_source
# print("HTML Content:")
# print(html_content)  # This will print the entire HTML

# Close the driver
driver.quit()

# Save HTML content to a file
with open('iranzamin_Bank_branches.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
