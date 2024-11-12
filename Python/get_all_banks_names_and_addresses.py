from bs4 import BeautifulSoup
import pandas as pd

# Load the HTML content from the saved file
with open('All_Iranian_Banks_greenpepper.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML with Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the div with class 'cc main-content'
main_content = soup.find('div', class_='cc main-content')

# Find the 'ul' tag within that div
ul_tag = main_content.find('ul')

# Initialize lists to hold the extracted data
bank_names = []
bank_links = []

# Loop through each 'li' item in the 'ul'
for li in ul_tag.find_all('li'):
    a_tag = li.find('a')
    if a_tag:
        bank_names.append(a_tag.text)        # Get the text of the link
        bank_links.append(a_tag['href'])     # Get the href attribute

# Create a DataFrame
df = pd.DataFrame({
    'Bank Name': bank_names,
    'Link': bank_links
})

# Save the DataFrame to an Excel file
df.to_excel('Iranian_Banks.xlsx', index=False)

print("Data has been written to Iranian_Banks.xlsx")
