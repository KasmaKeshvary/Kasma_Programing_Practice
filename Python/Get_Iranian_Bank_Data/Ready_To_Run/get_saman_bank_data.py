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
    driver.get('https://www.sb24.ir/contact-us/branches')

    wait = WebDriverWait(driver, 10)  
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'box-links')))

    linksParent = driver.find_element(By.CLASS_NAME, 'box-links')
    links = linksParent.find_elements(By.TAG_NAME, 'a')

    tehranLink = links[1]
    # print(tehranLink.get_attribute('href'))
    driver.get(tehranLink.get_attribute('href'))
    time.sleep(10)
    
    
    wait = WebDriverWait(driver, 10)  
    wait.until(EC.presence_of_element_located((By.ID, 'SearchResults')))

    tablesParent = driver.find_element(By.ID, 'SearchResults')
    # tables = headTableParent.find_elements(By.TAG_NAME, 'table')
    # for i in range(len(tables)):
    #     print(i)
    headTable = tablesParent.find_elements(By.TAG_NAME, 'table')[0]
    headThead = headTable.find_elements(By.TAG_NAME, 'tr')[0]
    headRow = headThead.find_elements(By.TAG_NAME, 'th')

    for i in range(len(headRow))[2:9]:
        # print(i,headRow[i].text)
        headers.append(headRow[i].text)

    print(headers)

    while True:
        try:

            time.sleep(10)

            # Find the pagination element
            paginationWait = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'SearchResults'))
            )

            tablesParent = driver.find_element(By.ID, 'SearchResults')

            pagination = tablesParent.find_elements(By.TAG_NAME, 'table')[2]

            pageItemsTemp = pagination.find_element(By.CLASS_NAME, 'CurrentPage')
            numberOfPages = int(pageItemsTemp.text)
            print(numberOfPages)

            tableParent = driver.find_element(By.ID, 'SearchResults')
            table = tableParent.find_elements(By.TAG_NAME, 'table')[0]
            tbody = table.find_element(By.TAG_NAME, 'tbody')
            rows = tbody.find_elements(By.TAG_NAME, 'tr')

            for k in range(len(rows))[1:]:
                rowData = []
                columns = rows[k].find_elements(By.TAG_NAME, 'td')
                for l in range(len(columns))[2:9]:
                    rowData.append(columns[l].text)
                    
                print(rowData)
                data.append(rowData)
    
            try:

                time.sleep(2)

                # Find the next page button
                nextPage = pagination.find_element(By.CLASS_NAME, 'NextPage')

                # nextPage = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'NextPage')))
                driver.execute_script("arguments[0].scrollIntoView();", nextPage)


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

    driver.get('https://www.sb24.ir/contact-us/branches')

    wait = WebDriverWait(driver, 10)  
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'box-links')))

    linksParent = driver.find_element(By.CLASS_NAME, 'box-links')
    links = linksParent.find_elements(By.TAG_NAME, 'a')
    
    tehranLink = links[2]
    # print(tehranLink.get_attribute('href'))
    driver.get(tehranLink.get_attribute('href'))
    time.sleep(10)

    while True:
        try:

            time.sleep(10)

            # Find the pagination element
            paginationWait = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'SearchResults'))
            )

            tablesParent = driver.find_element(By.ID, 'SearchResults')

            pagination = tablesParent.find_elements(By.TAG_NAME, 'table')[2]

            pageItemsTemp = pagination.find_element(By.CLASS_NAME, 'CurrentPage')
            numberOfPages = int(pageItemsTemp.text)
            print(numberOfPages)

            tableParent = driver.find_element(By.ID, 'SearchResults')
            table = tableParent.find_elements(By.TAG_NAME, 'table')[0]
            tbody = table.find_element(By.TAG_NAME, 'tbody')
            rows = tbody.find_elements(By.TAG_NAME, 'tr')

            for k in range(len(rows))[1:]:
                rowData = []
                columns = rows[k].find_elements(By.TAG_NAME, 'td')
                for l in range(len(columns))[2:9]:
                    rowData.append(columns[l].text)
                    
                print(rowData)
                data.append(rowData)
    
            try:

                time.sleep(2)

                # Find the next page button
                nextPage = pagination.find_element(By.CLASS_NAME, 'NextPage')

                # nextPage = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'NextPage')))
                driver.execute_script("arguments[0].scrollIntoView();", nextPage)


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
    df.to_excel('saman_bank_data.xlsx', index=False)

    # # Create a DataFrame and save to Excel
    df_headers = pd.DataFrame(headers)  # Use the headers as columns
    df_headers.to_excel('saman_headers.xlsx', index=False)

    df_branches = pd.DataFrame(data, columns=headers)  # Use the headers as columns
    df_branches.to_excel('saman_bank_branches.xlsx', index=False)



finally:
    # Close the driver
    driver.quit()