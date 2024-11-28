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
    driver.get('https://bankmellat.ir/local_branches.aspx')

    # Wait until the dropdown is present, then select the 3rd option
    wait = WebDriverWait(driver, 10)
    dropdown = wait.until(EC.presence_of_element_located((By.ID, 'cp_prjModuleContent186_drpBranchHead')))
    select = Select(dropdown)
    select.select_by_index(2)  # 0-based index (2 is the third option)

    # Click the search button
    search_button = driver.find_element(By.ID, 'cp_prjModuleContent186_btnSearch')
    search_button.click()

    # Wait for the results table to be present
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, 'tfoot')))

    wait.until(EC.presence_of_element_located((By.ID, 'cp_prjModuleContent186_grdBranchSearch_ctl00')))

    # Extract header data
    table = driver.find_element(By.ID, 'cp_prjModuleContent186_grdBranchSearch_ctl00')
    header_rows = table.find_elements(By.TAG_NAME, 'th')  # Get all header cells
    headers = [header.text for header in header_rows]  # Save the header texts
    del headers[-1]
    temp_headers = ['کد پستی', 'نشانی']
    headers.append(temp_headers)

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
                # data.append([column_one.text for column_one in columns_one])
                row_data_one = [column_one.text for column_one in columns_one]

                # Assuming the last column has an <a> tag to click
                last_column_one = columns_one[-1]
                link_one = last_column_one.find_element(By.TAG_NAME, 'a')
                link_one.click()  # Click on the link to open the modal

                # Wait for the modal to appear
                time.sleep(2)  # Adjust sleep time as necessary for the modal to load

                # Extract data from the modal
                postal_code_one = driver.find_element(By.ID, 'cp_prjModuleContent186_lblPstalCode').text
                address_one = driver.find_element(By.ID, 'cp_prjModuleContent186_lblAddress').text

                # Append the postal code and address to the row data
                row_data_one[-1:] = [postal_code_one, address_one]  # Replace last element with postal code and add address

                # Add the modified row data to the main data list
                data.append(row_data_one)

                time.sleep(1)  # Adjust as needed

    else:
        print("Less than two <tbody> found in the table.")


    # Find the <tfoot> and all <a> tags within it for pagination
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
                        # data.append([column.text for column in columns])
                        row_data = [column.text for column in columns]

                        # Assuming the last column has an <a> tag to click
                        last_column = columns[-1]
                        link = last_column.find_element(By.TAG_NAME, 'a')
                        link.click()  # Click on the link to open the modal

                        # Wait for the modal to appear
                        time.sleep(2)  # Adjust sleep time as necessary for the modal to load

                        # Extract data from the modal
                        postal_code = driver.find_element(By.ID, 'cp_prjModuleContent186_lblPstalCode').text
                        address = driver.find_element(By.ID, 'cp_prjModuleContent186_lblAddress').text

                        # Append the postal code and address to the row data
                        row_data[-1:] = [postal_code, address]  # Replace last element with postal code and add address

                        # Add the modified row data to the main data list
                        data.append(row_data)

                        time.sleep(1)  # Adjust as needed

            else:
                print("Less than two <tbody> found in the table.")

            
            # Re-fetch the pagination links
            footer = driver.find_element(By.TAG_NAME, 'tfoot')
            pagination_links = footer.find_elements(By.TAG_NAME, 'a')  # Re-fetch after clicking

        except StaleElementReferenceException:
            print("Caught StaleElementReferenceException, re-fetching links.")
            footer = driver.find_element(By.TAG_NAME, 'tfoot')
            pagination_links = footer.find_elements(By.TAG_NAME, 'a')  # Re-fetch after stale reference


    # df = pd.DataFrame(data)
    # # df.columns = ['Column1', 'Column2', 'Column3']  # Replace with actual column names as needed
    # df.to_excel('mellat_bank_data.xlsx', index=False)

    # # Create a DataFrame and save to Excel
    # df_headers = pd.DataFrame(headers)  # Use the headers as columns
    # df_headers.to_excel('branch_data_headers.xlsx', index=False)

    df_branches = pd.DataFrame(data, columns=headers)  # Use the headers as columns
    df_branches.to_excel('mellat_bank_branches.xlsx', index=False)


finally:
    # Close the driver
    driver.quit()