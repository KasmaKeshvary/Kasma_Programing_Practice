from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException  # Import here
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


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
    driver.get('https://www.refah-bank.ir/smart-branch-finding-sysytem')
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)  
    wait.until(EC.presence_of_element_located((By.ID, 'ctl14_ctl06_ctl01__btnShowAll')))

    showAll = driver.find_element(By.ID, 'ctl14_ctl06_ctl01__btnShowAll')
    
    print(showAll.get_attribute('innerHTML'))
    print('-----------------------------------------')

    actions = ActionChains(driver)
    actions.move_to_element(showAll).perform()  # Scrolls to the button

    # Optionally add a slight delay after scrolling
    time.sleep(1)


    showAll.click()
    time.sleep(5)

    branches = driver.find_elements(By.CLASS_NAME, 'ShowMarkerIssue')
    
    branches[1].click()
    time.sleep(5)

    


    # for i in range(len(branches)):
    #     print(i)
    #     branches[i].click()
    #     time.sleep(5)
    #     branchAction = ActionChains(driver)
    #     if i < len(branches)-1 :
    #         branchAction.move_to_element(branches[i+1]).perform()  # Scrolls to the button

    # searchButton.click()
    # time.sleep(5)
    # branchGrid = driver.find_element(By.ID, 'branchGrid')
    # headerGrid = branchGrid.find_element(By.CLASS_NAME, 'k-grid-header')
    # headerTable = headerGrid.find_element(By.TAG_NAME, 'table')
    # headerThead = headerTable.find_element(By.TAG_NAME, 'thead')
    # headerTitels = headerThead.find_elements(By.TAG_NAME, 'th')

    # for i in range(len(headerTitels))[1:]:
    #     # print(i,headRow[i].text)
    #     headers.append(headerTitels[i].text)

    # headersDone = 0
    
    # while True:
    #     try:

    #         time.sleep(10)

    #         # Find the pagination element
    #         paginationWait = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.ID, 'branchGrid'))
    #         )

    #         branchGrid = driver.find_element(By.ID, 'branchGrid')

    #         pagination = branchGrid.find_element(By.CLASS_NAME, 'k-pager-wrap')

    #         pageItemsTemp = pagination.find_element(By.CLASS_NAME, 'k-state-selected')
    #         numberOfPages = int(pageItemsTemp.text)
    #         print(numberOfPages)

    #         # wait = WebDriverWait(driver, 10)  
    #         # wait.until(EC.presence_of_element_located((By.ID, 'branchGrid')))

    #         # branchGrid = driver.find_element(By.ID, 'branchGrid')
    #         contentGrid = branchGrid.find_element(By.CLASS_NAME, 'k-grid-content')
    #         contentTable = contentGrid.find_element(By.TAG_NAME, 'table')
    #         contentTbody = contentTable.find_element(By.TAG_NAME, 'tbody')
    #         contentRows = contentTbody.find_elements(By.TAG_NAME, 'tr')

    #         for j in range(len(contentRows)):

    #             rowData =[]

    #             if j == 1 :
    #                 headersDone =+1

    #             if j == 2 :
    #                 elem = driver.find_element(By.TAG_NAME, "html")
    #                 elem.send_keys(Keys.END)

    #             contentColumns = contentRows[j].find_elements(By.TAG_NAME, 'td')

    #             for k in range(len(contentColumns))[1:]:
    #                 rowData.append(contentColumns[k].text)

    #             contentColumns[0].click()
    #             time.sleep(3)
    #             detailCells = contentTbody.find_elements(By.CLASS_NAME, 'k-detail-cell')
    #             for l in range(len(detailCells)):
    #                 if l == (len(detailCells)-1):
    #                     # print(detailCells[l].text)
    #                     detailRows = detailCells[l].find_elements(By.CLASS_NAME, 'row')
    #                     for m in range(len(detailRows)):
    #                         detailRowDivs = detailRows[m].find_elements(By.TAG_NAME, 'div')
    #                         for n in range(len(detailRowDivs)):
                                
    #                             if headersDone == 0 :
    #                                 smallTag = detailRowDivs[n].find_element(By.TAG_NAME, 'small')
    #                                 headers.append(smallTag.text)
                                    
    #                             inputTag = detailRowDivs[n].find_element(By.TAG_NAME, 'input')
    #                             rowData.append(inputTag.get_attribute('value'))

    #             print(headers)
    #             print(rowData)
    #             data.append(rowData)
    #             time.sleep(3)
    #             contentColumns[0].click()
    #             time.sleep(3)


    #         try:

    #             time.sleep(2)

    #             # Find the next page button
    #             nextPage = pagination.find_elements(By.CLASS_NAME, 'k-pager-nav')[2]

    #             # nextPage = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'NextPage')))
    #             driver.execute_script("arguments[0].scrollIntoView();", nextPage)

    #             WebDriverWait(driver, 5).until(
    #             EC.element_to_be_clickable((By.XPATH, '//div[@id="branchGrid"]//a[contains(@class, "k-pager-nav")][2]'))
    #             )

    #             nextPage.click()
    #             time.sleep(3)  # Adjust sleep as needed or use WebDriverWait to wait for the next page to load
                


    #             # # Check if nextPage is visible before clicking
    #             # if nextPage.is_displayed():
    #             #     nextPage.click()
    #             #     time.sleep(3)  # Adjust sleep as needed or use WebDriverWait to wait for the next page to load
    #             # else:
    #             #     break  # Exit if nextPage is not displayed

    #         except NoSuchElementException:
    #             # If the next page button does not exist, break the loop
    #             print("Next page button not found, ending pagination.")
    #             break

    #     except TimeoutException:
    #         print("Pagination timed out.")
    #         break  # Exit the loop if pagination takes too long

    #     except StaleElementReferenceException:
    #         print("Encountered a stale element reference error. Retrying...")
    #         continue  # Continue back to the start of the loop to re-select elements

    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         break  # Exit the loop if any unexpected error occurs
    

    # df = pd.DataFrame(data)
    # # df.columns = ['Column1', 'Column2', 'Column3']  # Replace with actual column names as needed
    # df.to_excel('keshavarzi_bank_data.xlsx', index=False)

    # # # Create a DataFrame and save to Excel
    # df_headers = pd.DataFrame(headers)  # Use the headers as columns
    # df_headers.to_excel('keshavarzi_headers.xlsx', index=False)

    # df_branches = pd.DataFrame(data, columns=headers)  # Use the headers as columns
    # df_branches.to_excel('keshavarzi_bank_branches.xlsx', index=False)


finally:
    # Close the driver
    driver.quit()