from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException  # Import here
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


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
    driver.get('https://sinabank.ir/web_directory/189-%D8%B4%D8%B9%D8%A8.html')

    wait = WebDriverWait(driver, 10)  
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'block_body_center')))

    # buttonParents = driver.find_elements(By.CLASS_NAME, 'sis-block-operation')
    # button = buttonParents[1].find_element(By.TAG_NAME, 'button')

    # button.click()

    time.sleep(3)

    headTableParent = driver.find_element(By.CLASS_NAME, 'block_body_center')
    headTable = headTableParent.find_elements(By.TAG_NAME, 'table')[0]
    headThead = headTable.find_elements(By.TAG_NAME, 'tr')[0]
    headRow = headThead.find_elements(By.TAG_NAME, 'td')

    for i in range(len(headRow)):
        headers.append(headRow[i].text)

    print(headers)

    # navigatorcell = driver.find_element(By.CLASS_NAME, 'navigator2-cell')

    # pageItemsTemp = navigatorcell.find_element(By.CLASS_NAME, 'navigator2-selected')
    # numberOfPages = int(pageItemsTemp.text)
    # print(numberOfPages)

    # print('ok')
    
    while True:
        try:

            time.sleep(2)

            # Find the pagination element
            pagination = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'navigator2-cell'))
            )

            pageItemsTemp = pagination.find_element(By.CLASS_NAME, 'navigator2-selected')
            numberOfPages = int(pageItemsTemp.text)
            print(numberOfPages)

            tableParent = driver.find_element(By.CLASS_NAME, 'block_body_center')
            table = tableParent.find_elements(By.TAG_NAME, 'table')[0]
            tbody = table.find_element(By.TAG_NAME, 'tbody')
            rows = tbody.find_elements(By.TAG_NAME, 'tr')

            for k in range(len(rows))[1:]:
                rowData = []
                columns = rows[k].find_elements(By.TAG_NAME, 'td')
                for l in range(len(columns)):
                    rowData.append(columns[l].text)
                    
                print(rowData)
                data.append(rowData)
    
            try:

                time.sleep(2)

                # Find the next page button
                nextPage = pagination.find_element(By.CLASS_NAME, 'navigator-next')

                # Check if nextPage is visible before clicking
                if nextPage.is_displayed():
                    nextPage.click()
                    time.sleep(3)  # Adjust sleep as needed or use WebDriverWait to wait for the next page to load
                else:
                    break  # Exit if nextPage is not displayed
            except NoSuchElementException:
                # If the next page button does not exist, break the loop
                print("Next page button not found, ending pagination.")
                break

        except TimeoutException:
            print("Pagination timed out.")
            break  # Exit the loop if pagination takes too long

        except StaleElementReferenceException:
            print("Encountered a stale element reference error. Retrying...")
            continue  # Continue back to the start of the loop to re-select elements

        except Exception as e:
            print(f"An error occurred: {e}")
            break  # Exit the loop if any unexpected error occurs

            
    df = pd.DataFrame(data)
    # df.columns = ['Column1', 'Column2', 'Column3']  # Replace with actual column names as needed
    df.to_excel('sina_bank_data.xlsx', index=False)

    # # Create a DataFrame and save to Excel
    df_headers = pd.DataFrame(headers)  # Use the headers as columns
    df_headers.to_excel('sina_headers.xlsx', index=False)

    df_branches = pd.DataFrame(data, columns=headers)  # Use the headers as columns
    df_branches.to_excel('sina_bank_branches.xlsx', index=False)



finally:
    # Close the driver
    driver.quit()