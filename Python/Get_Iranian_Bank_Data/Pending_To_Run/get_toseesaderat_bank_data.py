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
    driver.get('https://www.edbi.ir/general_content/1138/1138.htm')

    # wait = WebDriverWait(driver, 10)  
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, 'form')))
    
    # headers_counter = 0

    time.sleep(3)

    div = driver.find_element(By.CLASS_NAME, 'MainDivBankbranch')

    NameBankbranch = div.find_element(By.CLASS_NAME, 'NameBankbranch')
    headers.append(NameBankbranch.text.split(" ",1)[0])
    # print(NameBankbranch.text.split(" ",1)[0])

    divs = div.find_elements(By.TAG_NAME, 'div')
    # print(divs[1].text.splitlines())
    kshr = divs[1].text.splitlines()
    for k in range(len(kshr)):
        # print(kshr[k].split(':',1)[0])
        headers.append(kshr[k].split(':',1)[0])

    postCodeBankbranch = div.find_element(By.CLASS_NAME, 'postCodeBankbranch')
    headers.append(postCodeBankbranch.text.split(":",1)[0])
    # print(postCodeBankbranch.text.split(":",1)[0])

    tellBankbranchs = div.find_elements(By.CLASS_NAME, 'tellBankbranch')
    # print(len(tellBankbranchs))
    if len(tellBankbranchs) == 1 :
        tellBankbranch = div.find_element(By.CLASS_NAME, 'tellBankbranch')
        print(tellBankbranch.text.split(":",1)[0])
        headers.append(tellBankbranch.text.split(":",1)[0])
        headers.append('')
    else:
        # print(tellBankbranchs[0].text.split(":",1)[0])
        headers.append(tellBankbranchs[0].text.split(":",1)[0])
        # print(tellBankbranchs[1].text.split(":",1)[0])
        headers.append(tellBankbranchs[1].text.split(":",1)[0])

    faxBankbranch = div.find_element(By.CLASS_NAME, 'faxBankbranch')
    headers.append(faxBankbranch.text.split(":",1)[0])
    # print(faxBankbranch.text.split(":",1)[0])

    prefixesTellBankbranch = div.find_element(By.CLASS_NAME, 'prefixesTellBankbranch')
    headers.append(prefixesTellBankbranch.text.split(":",1)[0])
    # print(prefixesTellBankbranch.text.split(":",1)[0])

    emailBankbranch = div.find_element(By.CLASS_NAME, 'emailBankbranch')
    headers.append(emailBankbranch.text.split(":",1)[0])

    
    driver.get('https://www.edbi.ir/web_directory/41640-%D8%B4%D8%B9%D8%A8-%D8%AF%D8%A7%D8%AE%D9%84%DB%8C.html')

    pages = driver.find_elements(By.TAG_NAME, 'h3')

    for i in range(len(pages)-4):
        try:

            time.sleep(5)
            current_page = pages[i]
            current_page.click()

            try:

                div = driver.find_element(By.CLASS_NAME, 'navigator2-cell')
                print('y')
                next_page_clicked_number = div.find_elements(By.CLASS_NAME,'navigator-item')

                for i in range(len(next_page_clicked_number)+1):

                    try:
                        # time.sleep(5)

                        div = driver.find_element(By.CLASS_NAME, 'navigator2-cell')
                        next_page_clicked_number = div.find_elements(By.CLASS_NAME,'navigator-item')

                        divs = driver.find_elements(By.CLASS_NAME, 'cntService')

                        for i in range(len(divs)):
                        
                            try:    
                                # Re-fetch elements to avoid stale references
                                divs = driver.find_elements(By.CLASS_NAME, 'cntService')
                                contentTextContainer = divs[i].find_element(By.CLASS_NAME,'contentTextContainer')
                                branch_name = contentTextContainer.find_element(By.TAG_NAME,'a')
                                print(f'Clicking on: {branch_name.text}')  # Debug print

                                if branch_name.text == 'شعبه بجنورد(خراسان شمالی)':
                                    print('must pass')
                                    continue

                                branch_name.click()
                                time.sleep(4)  # Wait for the new page to load

                                try:

                                    row_data = []
                                    div = driver.find_element(By.CLASS_NAME, 'MainDivBankbranch')
                                    
                                    try:
                                        NameBankbranch = div.find_element(By.CLASS_NAME, 'NameBankbranch')
                                        if ' ' in NameBankbranch.text:
                                            row_data.append(NameBankbranch.text.split(" ",1)[1])
                                            # print(NameBankbranch.text.split(" ",1)[1])
                                        else:
                                            row_data.append(NameBankbranch.text)
                                            # print(NameBankbranch.text)
                                        
                                    except NoSuchElementException:
                                        row_data.append('')
                                
                                    divs = div.find_elements(By.TAG_NAME, 'div')
                                    # print(divs[1].text.splitlines())
                                    kshr = divs[1].text.splitlines()
                                    for k in range(len(kshr)):
                                        # print(kshr[k].split(':',1)[1])
                                        try: 
                                            if ':' in kshr[k]:
                                                row_data.append(kshr[k].split(':',1)[1])
                                            else:
                                                row_data.append(kshr[k])
                                        except NoSuchElementException:
                                            row_data.append('')

                                    try:
                                        postCodeBankbranch = div.find_element(By.CLASS_NAME, 'postCodeBankbranch')
                                        row_data.append(postCodeBankbranch.text.split(":",1)[1])
                                        # print(postCodeBankbranch.text.split(":",1)[1])
                                    except NoSuchElementException:
                                        row_data.append('')
                                
                                    try:    
                                        tellBankbranchs = div.find_elements(By.CLASS_NAME, 'tellBankbranch')
                                        # print(len(tellBankbranchs))
                                        if len(tellBankbranchs) == 1 :
                                            tellBankbranch = div.find_element(By.CLASS_NAME, 'tellBankbranch')
                                            # print(tellBankbranch.text.split(":",1)[1])
                                            row_data.append(tellBankbranch.text.split(":",1)[1])
                                            row_data.append('')
                                
                                        else:
                                            # print(tellBankbranchs[0].text.split(":",1)[1])
                                            row_data.append(tellBankbranchs[0].text.split(":",1)[1])
                                            # print(tellBankbranchs[1].text.split(":",1)[1])
                                            row_data.append(tellBankbranchs[1].text.split(":",1)[1])
                                    except NoSuchElementException:
                                        row_data.append('')
                                        row_data.append('')
                                    
                                    try:
                                        faxBankbranch = div.find_element(By.CLASS_NAME, 'faxBankbranch')
                                        if len(faxBankbranch.text.split(":",1)) < 3 :
                                            row_data.append(faxBankbranch.text.split(":",1)[1])
                                            # print(faxBankbranch.text.split(":",1)[1])
                                        else:
                                            row_data.append('')         
                                    except NoSuchElementException:
                                        row_data.append('')
                                
                                    try:
                                        prefixesTellBankbranch = div.find_element(By.CLASS_NAME, 'prefixesTellBankbranch')
                                        row_data.append(prefixesTellBankbranch.text.split(":",1)[1])
                                        # print(prefixesTellBankbranch.text.split(":",1)[1])
                                    except NoSuchElementException:
                                        row_data.append('')
                                
                                    try:
                                        emailBankbranch = div.find_element(By.CLASS_NAME, 'emailBankbranch')
                                        row_data.append(emailBankbranch.text.split(":",1)[1])
                                        # print(emailBankbranch.text.split(":",1)[1])
                                    except NoSuchElementException:
                                        row_data.append('')
                                
                                    data.append(row_data)

                                
                                except NoSuchElementException:
                                    print("MainDivBankbranch not found. Skipping to next iteration.")
                                    driver.back()
                                    time.sleep(3)  # Wait for the original page to reload

                                    # Ensure we are still referencing the correct list of divs
                                    divs = driver.find_elements(By.CLASS_NAME, 'cntService')

                                    continue  # Skip to the next iteration of the for loop
                                
                                # Go back to the previous page
                                driver.back()
                                time.sleep(3)  # Wait for the original page to reload

                                # Ensure we are still referencing the correct list of divs
                                divs = driver.find_elements(By.CLASS_NAME, 'cntService')

                            except StaleElementReferenceException:
                                # Re-fetch the list if a StaleElementReferenceException is caught
                                print("Caught StaleElementReferenceException, re-fetching links.")
                                divs = driver.find_elements(By.CLASS_NAME, 'cntService')

                            except Exception as e:
                                print(f"An error occurred: {e}")
                                break  # Exit the loop if an unexpected error occurs
                            
                        # print(headers)
                        # print(data)

                        next_page_button = driver.find_element(By.CLASS_NAME, 'navigator-next')
                        is_visible = driver.execute_script("return arguments[0].offsetParent !== null;", next_page_button)
                        if is_visible:
                            next_page_button.click()
                        else:
                            print("Next page button is not visible.")

                        div = driver.find_element(By.CLASS_NAME, 'navigator2-cell')
                        next_page_clicked_number = div.find_elements(By.CLASS_NAME,'navigator-item')

                    except StaleElementReferenceException:
                        # print("Caught StaleElementReferenceException, re-fetching links.")
                        div = driver.find_element(By.CLASS_NAME, 'navigator2-cell')
                        next_page_clicked_number = div.find_elements(By.CLASS_NAME,'navigator-item')

            except NoSuchElementException:
                print('n')
               

                divs = driver.find_elements(By.CLASS_NAME, 'cntService')

                for i in range(len(divs)):

                    try:    
                        # Re-fetch elements to avoid stale references
                        divs = driver.find_elements(By.CLASS_NAME, 'cntService')
                        contentTextContainer = divs[i].find_element(By.CLASS_NAME,'contentTextContainer')
                        branch_name = contentTextContainer.find_element(By.TAG_NAME,'a')

                        print(f'Clicking on: {branch_name.text}')  # Debug print

                        branch_name.click()
                        time.sleep(3)  # Wait for the new page to load

                        row_data = []
                        div = driver.find_element(By.CLASS_NAME, 'MainDivBankbranch')

                        try:
                            NameBankbranch = div.find_element(By.CLASS_NAME, 'NameBankbranch')
                            if ' ' in NameBankbranch.text:
                                row_data.append(NameBankbranch.text.split(" ",1)[1])
                                # print(NameBankbranch.text.split(" ",1)[1])
                            else:
                                row_data.append(NameBankbranch.text)
                                # print(NameBankbranch.text)

                        except NoSuchElementException:
                            row_data.append('')

                        divs = div.find_elements(By.TAG_NAME, 'div')
                        # print(divs[1].text.splitlines())
                        kshr = divs[1].text.splitlines()
                        for k in range(len(kshr)):
                            # print(kshr[k].split(':',1)[1])
                            try: 
                                if ':' in kshr[k]:
                                    row_data.append(kshr[k].split(':',1)[1])
                                else:
                                    row_data.append(kshr[k])
                            except NoSuchElementException:
                                row_data.append('')
                        try:
                            postCodeBankbranch = div.find_element(By.CLASS_NAME, 'postCodeBankbranch')
                            row_data.append(postCodeBankbranch.text.split(":",1)[1])
                            # print(postCodeBankbranch.text.split(":",1)[1])
                        except NoSuchElementException:
                            row_data.append('')

                        try:    
                            tellBankbranchs = div.find_elements(By.CLASS_NAME, 'tellBankbranch')
                            # print(len(tellBankbranchs))
                            if len(tellBankbranchs) == 1 :
                                tellBankbranch = div.find_element(By.CLASS_NAME, 'tellBankbranch')
                                # print(tellBankbranch.text.split(":",1)[1])
                                row_data.append(tellBankbranch.text.split(":",1)[1])
                                row_data.append('')

                            else:
                                # print(tellBankbranchs[0].text.split(":",1)[1])
                                row_data.append(tellBankbranchs[0].text.split(":",1)[1])
                                # print(tellBankbranchs[1].text.split(":",1)[1])
                                row_data.append(tellBankbranchs[1].text.split(":",1)[1])
                        except NoSuchElementException:
                            row_data.append('')
                            row_data.append('')

                        try:
                            faxBankbranch = div.find_element(By.CLASS_NAME, 'faxBankbranch')
                            row_data.append(faxBankbranch.text.split(":",1)[1])
                            # print(faxBankbranch.text.split(":",1)[1])
                        except NoSuchElementException:
                            row_data.append('')

                        try:
                            prefixesTellBankbranch = div.find_element(By.CLASS_NAME, 'prefixesTellBankbranch')
                            row_data.append(prefixesTellBankbranch.text.split(":",1)[1])
                            # print(prefixesTellBankbranch.text.split(":",1)[1])
                        except NoSuchElementException:
                            row_data.append('')

                        try:
                            emailBankbranch = div.find_element(By.CLASS_NAME, 'emailBankbranch')
                            row_data.append(emailBankbranch.text.split(":",1)[1])
                            # print(emailBankbranch.text.split(":",1)[1])
                        except NoSuchElementException:
                            row_data.append('')

                        data.append(row_data)

                        # Go back to the previous page
                        driver.back()
                        time.sleep(3)  # Wait for the original page to reload

                        # Ensure we are still referencing the correct list of divs
                        divs = driver.find_elements(By.CLASS_NAME, 'cntService')

                    except StaleElementReferenceException:
                        # Re-fetch the list if a StaleElementReferenceException is caught
                        print("Caught StaleElementReferenceException, re-fetching links.")
                        divs = driver.find_elements(By.CLASS_NAME, 'cntService')

                    except Exception as e:
                        print(f"An error occurred: {e}")
                        break  # Exit the loop if an unexpected error occurs
                    
                # print(headers)
                # print(data)
    

            pages = driver.find_elements(By.TAG_NAME, 'h3')

        except StaleElementReferenceException:
            # print("Caught StaleElementReferenceException, re-fetching links.")
            pages = driver.find_elements(By.TAG_NAME, 'h3')

    df = pd.DataFrame(data)
    # df.columns = ['Column1', 'Column2', 'Column3']  # Replace with actual column names as needed
    df.to_excel('toseesaderat_bank_data.xlsx', index=False)

    # # Create a DataFrame and save to Excel
    df_headers = pd.DataFrame(headers)  # Use the headers as columns
    df_headers.to_excel('toseesaderat_headers.xlsx', index=False)

    df_branches = pd.DataFrame(data, columns=headers)  # Use the headers as columns
    df_branches.to_excel('toseesaderat_bank_branches.xlsx', index=False)

finally:
    # Close the driver
    driver.quit()