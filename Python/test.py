from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException  # Import here
import pandas as pd
import time

# Specify the path to your webdriver
service = Service(r'C:\Users\Kasma\Desktop\Kasma_Programming_Practice\Python\chromedriver.exe')

# Initialize the WebDriver using the Service
driver = webdriver.Chrome(service=service)

# Create a list to hold data
headers = []
data = []

try:
    # Open the URL
    driver.get('https://bankmellat.ir/local_branches.aspx')

    # Wait until the dropdown is present
    wait = WebDriverWait(driver, 5)
    
    dropdown_one = wait.until(EC.presence_of_element_located((By.ID, 'cp_prjModuleContent186_drpBranchHead')))
    select_one = Select(dropdown_one)
    select_one.select_by_index(2)  # 0-based index (2 is the third option)

    # Click the search button
    search_button_one = driver.find_element(By.ID, 'cp_prjModuleContent186_btnSearch')
    search_button_one.click()

    # Wait for the results table to be present
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, 'tfoot')))

    wait.until(EC.presence_of_element_located((By.ID, 'cp_prjModuleContent186_grdBranchSearch_ctl00')))

    # Extract header data
    table = driver.find_element(By.ID, 'cp_prjModuleContent186_grdBranchSearch_ctl00')
    header_rows = table.find_elements(By.TAG_NAME, 'th')  # Get all header cells
    headers = [header.text for header in header_rows]  # Save the header texts
    
    # Open the URL
    driver.get('https://bankmellat.ir/local_branches.aspx')

    # Wait until the dropdown is present
    wait = WebDriverWait(driver, 5)
    
    # We will refetch the dropdown in each iteration
    for index in range(2, 8):       
        dropdown = wait.until(EC.presence_of_element_located((By.ID, 'cp_prjModuleContent186_drpBranchHead')))
        select = Select(dropdown)

        select.select_by_index(index)  # Select the desired index

        # Click the search button
        search_button = driver.find_element(By.ID, 'cp_prjModuleContent186_btnSearch')
        search_button.click()

        # Wait for the results or data to load
        time.sleep(3)  # Adjust according to the site's response time

        wait.until(EC.presence_of_element_located((By.ID, 'cp_prjModuleContent186_grdBranchSearch_ctl00')))

        table_one = driver.find_element(By.ID, 'cp_prjModuleContent186_grdBranchSearch_ctl00')
            
        tbodies_one = table_one.find_elements(By.TAG_NAME, 'tbody')
        # Check if there are at least two <tbody> tags
        if len(tbodies_one) > 1:
            tbody_one = tbodies_one[1]  # Select the second <tbody> (index 1)
            # Collect rows from the second <tbody>
            rows_one = tbody_one.find_elements(By.TAG_NAME, 'tr')
            # Iterate over rows and collect data
            for row_one in rows_one:
                columns_one = row_one.find_elements(By.TAG_NAME, 'td')
                if columns_one:  # Check if there are any columns
                    # Append row data to the list
                    data.append([column_one.text for column_one in columns_one])

        footer = driver.find_element(By.TAG_NAME, 'tfoot')
        pagination_links = footer.find_elements(By.TAG_NAME, 'a')

        for i in range(len(pagination_links)-1):
            try:
                # Click the current pagination link
                time.sleep(10)
                current_link = pagination_links[i+1]
                current_link.click()

                wait.until(EC.presence_of_element_located((By.ID, 'cp_prjModuleContent186_grdBranchSearch_ctl00')))

                # Scrape table data
                table = driver.find_element(By.ID, 'cp_prjModuleContent186_grdBranchSearch_ctl00')

                tbodies = table.find_elements(By.TAG_NAME, 'tbody')

                # Check if there are at least two <tbody> tags
                if len(tbodies) > 1:
                    tbody = tbodies[1]  # Select the second <tbody> (index 1)

                    # Collect rows from the second <tbody>
                    rows = tbody.find_elements(By.TAG_NAME, 'tr')

                    # Iterate over rows and collect data
                    for row in rows:
                        columns = row.find_elements(By.TAG_NAME, 'td')
                        if columns:  # Check if there are any columns
                            # Append row data to the list
                            data.append([column.text for column in columns])
                
                footer = driver.find_element(By.TAG_NAME, 'tfoot')
                pagination_links = footer.find_elements(By.TAG_NAME, 'a')  # Re-fetch after clicking

            except StaleElementReferenceException:
                print("Caught StaleElementReferenceException, re-fetching links.")
                footer = driver.find_element(By.TAG_NAME, 'tfoot')
                pagination_links = footer.find_elements(By.TAG_NAME, 'a')  # Re-fetch after stale reference

    df_branches = pd.DataFrame(data, columns=headers)  # Use the headers as columns
    df_branches.to_excel('mellat_bank_branches.xlsx', index=False)


finally:
    # Close the driver
    driver.quit()
