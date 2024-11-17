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
service = Service(r'C:\Users\Kasma\Desktop\Kasma_Programming_Practice\Python\chromedriver.exe')

# Initialize the WebDriver using the Service
driver = webdriver.Chrome(service=service)

# Create a list to hold data
headers = []
data = []

try:
    # Open the URL
    driver.get('https://izbank.ir/fa/page/100691-%D8%AC%D8%B3%D8%AA%D8%AC%D9%88%DB%8C-%D9%BE%DB%8C%D8%B4%D8%B1%D9%81%D8%AA%D9%87.html#content_search_form_227285')

    wait = WebDriverWait(driver, 10)  
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'sis-block-operation')))

    buttonParents = driver.find_elements(By.CLASS_NAME, 'sis-block-operation')
    button = buttonParents[1].find_element(By.TAG_NAME, 'button')

    button.click()

    time.sleep(3)

    headTableParent = driver.find_element(By.ID, 'no-more-tables')
    headTable = headTableParent.find_element(By.TAG_NAME, 'table')
    headThead = headTable.find_element(By.TAG_NAME, 'thead')
    headRow = headThead.find_elements(By.TAG_NAME, 'th')

    for i in range(len(headRow)-2):
        headers.append(headRow[i].text)

    headTbody = headTable.find_element(By.TAG_NAME, 'tbody')
    headTailRow = headTbody.find_elements(By.TAG_NAME, 'tr')
    headColumns = headTailRow[0].find_elements(By.TAG_NAME, 'td')
    headSpecificColumnInfos = headColumns[4].find_elements(By.TAG_NAME, 'div')

    for j in range(len(headSpecificColumnInfos)):
        headers.append(headSpecificColumnInfos[j].text.split(':',1)[0])

    print(headers)
    
    while True:
        try:

            time.sleep(2)

            # Find the pagination element
            pagination = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'pagination'))
            )

            pageItemsTemp = pagination.find_element(By.CLASS_NAME, 'active')
            numberOfPages = int(pageItemsTemp.text)
            print(numberOfPages)

            tableParent = driver.find_element(By.ID, 'no-more-tables')
            table = tableParent.find_element(By.TAG_NAME, 'table')
            tbody = table.find_element(By.TAG_NAME, 'tbody')
            rows = tbody.find_elements(By.TAG_NAME, 'tr')

            for k in range(len(rows)):
                rowData = []
                columns = rows[k].find_elements(By.TAG_NAME, 'td')
                for l in range(len(columns)-1):
                    if l < 4:
                        rowData.append(columns[l].text)
                    if l == 4:
                        specificColumnInfos = columns[l].find_elements(By.TAG_NAME, 'div')
                        for m in range(len(specificColumnInfos)):
                            rowData.append(specificColumnInfos[m].text.split(':',1)[1])
                
                print(rowData)
                data.append(rowData)
    
            try:

                time.sleep(2)

                # Find the next page button
                nextPage = pagination.find_element(By.CLASS_NAME, 'page-next')

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
    df.to_excel('iranzamin_bank_data.xlsx', index=False)

    # # Create a DataFrame and save to Excel
    df_headers = pd.DataFrame(headers)  # Use the headers as columns
    df_headers.to_excel('iranzamin_headers.xlsx', index=False)

    df_branches = pd.DataFrame(data, columns=headers)  # Use the headers as columns
    df_branches.to_excel('iranzamin_bank_branches.xlsx', index=False)



finally:
    # Close the driver
    driver.quit()