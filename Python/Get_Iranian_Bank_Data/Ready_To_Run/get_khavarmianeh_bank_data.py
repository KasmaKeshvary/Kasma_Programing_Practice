from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException  # Import here
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import pandas as pd
import time
import sys

config_directory = r'C:\Users\Kasma\Desktop\Kasma_Programming_Practice\Python\Get_Iranian_Bank_Data'
sys.path.append(config_directory)

from config import CHROMEDRIVER_PATH
from config import EXCEL_TARGET_DIRECTORY

# Specify the path to your webdriver
service = Service(CHROMEDRIVER_PATH)

# Initialize the WebDriver using the Service
driver = webdriver.Chrome(service=service)

# Create a list to hold data
headers = []
data = []

try:
    # Open the URL
    driver.get('https://www.middleeastbank.ir/page/branches')

    
    panels = driver.find_elements(By.CLASS_NAME, 'panel-default')
    # divs = driver.find_elements(By.CLASS_NAME, 'panel-default')
    # headers
    branch = panels[0].find_element(By.CLASS_NAME, 'panel-title')
    # print(branch.text.split(" ",1)[0])
    headers.append(branch.text.split(" ",1)[0])

    branchColumns = panels[0].find_elements(By.CLASS_NAME, 'branches-row2')

    for i in range(len(branchColumns)):
        if i == 1 :
            continue
        # if i < 9 :
        spans = branchColumns[i].find_elements(By.TAG_NAME, 'span')
        # print(spans[0].text.split(':')[0])
        headers.append(spans[0].text.split(':')[0])
    

    print(len(panels))
    for i in range(len(panels)-1):
        print(i)
        try:
            rowData = []    
            time.sleep(1.5)

            current_panel = panels[i]
            current_panel.click()
            time.sleep(1.5)

            branchName = panels[i].find_element(By.CLASS_NAME,'panel-title')
            print(branchName.text.split(" ",1)[1])
            rowData.append(branchName.text.split(" ",1)[1])

            branchDataRows = panels[i].find_elements(By.CLASS_NAME, 'branches-row2')

            for j in range(len(branchDataRows)):
                print(j)
                if j == 1 :
                    continue
                if j < 10 :
                    spans = branchDataRows[j].find_elements(By.TAG_NAME, 'span')
                    print(spans[1].text.replace("\n"," - "))
                    rowData.append(spans[1].text.replace("\n"," - "))
                if j == 10 :
                    table = branchDataRows[j].find_element(By.TAG_NAME, 'table')
                    print(table.text.replace("\n"," - "))
                    rowData.append(table.text.replace("\n"," - "))
    
            print(rowData)
    
            data.append(rowData)

            # current_panel = panels[i]
            # current_panel.click()
            # time.sleep(1.5)

            if i ==10:
                time.sleep(1)
                driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + Keys.HOME)
                time.sleep(1)
                main = driver.find_element(By.CLASS_NAME,'nav-tabs')
                subMain = main.find_elements(By.TAG_NAME,'a')
                print(subMain[1].text)
                subMain[1].click()
                time.sleep(3)
                continue
                # break
                    
            # else:
            #     print("Next page panel is not visible.")
            #     continue

            panels = driver.find_elements(By.CLASS_NAME, 'panel-default')

        except StaleElementReferenceException:
            # print("Caught StaleElementReferenceException, re-fetching links.")
            panels = driver.find_elements(By.CLASS_NAME, 'panel-default')
            # continue

        except Exception as e:
            print(f"An error occurred: {e}")
            break  # Exit the loop if an unexpected error occurs
               

    # divs = driver.find_elements(By.CLASS_NAME, 'panel-default')
    
    # # headers
    # branch = divs[0].find_element(By.CLASS_NAME, 'panel-title')
    # # print(branch.text.split(" ",1)[0])
    # headers.append(branch.text.split(" ",1)[0])

    # branchColumns = divs[0].find_elements(By.CLASS_NAME, 'branches-row2')

    # for i in range(len(branchColumns)):
    #     if i == 1 :
    #         continue
    #     # if i < 9 :
    #     spans = branchColumns[i].find_elements(By.TAG_NAME, 'span')
    #     # print(spans[0].text.split(':')[0])
    #     headers.append(spans[0].text.split(':')[0])
    
    # #data
    # for i in range(len(divs)-6):
        
    #     rowData = []
        
    #     branchName = divs[i].find_element(By.CLASS_NAME, 'panel-title')
    #     print(branchName.text.split(" ",1)[1])
    #     rowData.append(branchName.text.split(" ",1)[1])

    #     branchDataRows = divs[i].find_elements(By.CLASS_NAME, 'branches-row2')

    #     for j in range(len(branchDataRows)):
    #         print(j)
    #         if j == 1 :
    #             continue
    #         if j < 10 :
    #             spans = branchDataRows[j].find_elements(By.TAG_NAME, 'span')
    #             print(spans[1].text.replace("\n"," - "))
    #             rowData.append(spans[1].text.replace("\n"," - "))
    #         if j == 10 :
    #             table = branchDataRows[j].find_element(By.TAG_NAME, 'table')
    #             print(table.text.replace("\n"," - "))
    #             rowData.append(table.text.replace("\n"," - "))

    #     print(rowData)

    #     data.append(rowData)

    
    # df = pd.DataFrame(data)
    # df.columns = ['Column1', 'Column2', 'Column3']  # Replace with actual column names as needed
    # df.to_excel('khavarmianeh_bank_data.xlsx', index=False)

    # Create a DataFrame and save to Excel
    # df_headers = pd.DataFrame(headers)  # Use the headers as columns
    # df_headers.to_excel('khavarmianeh_headers.xlsx', index=False)

    df_branches = pd.DataFrame(data, columns=headers)  # Use the headers as columns
    
    # Ensure there's a trailing backslash
    if not EXCEL_TARGET_DIRECTORY.endswith('\\'):
        EXCEL_TARGET_DIRECTORY += '\\'

    # Define the full path for the Excel file
    excel_file_path = f"{EXCEL_TARGET_DIRECTORY}\\khavarmianeh_bank_branches_data.xlsx"

    df_branches.to_excel(excel_file_path, index=False)


finally:
    # Close the driver
    driver.quit()