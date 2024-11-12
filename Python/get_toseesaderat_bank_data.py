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
    driver.get('https://www.edbi.ir/general_content/1115/1115.htm')

    # wait = WebDriverWait(driver, 10)  
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, 'form')))
    
    # headers_counter = 0

    time.sleep(5)

    div = driver.find_element(By.CLASS_NAME, 'MainDivBankbranch')
    informations = div.find_elements(By.TAG_NAME,'div') 
    
    for i in range(len(informations)):

        if i == 0:
            headers.append(informations[i].text.split(" ",1)[0])
        elif i == 1: 
            # print('poi')
            info_details = informations[i].text.splitlines()
            for info_detail in info_details:
                # print(info_detail.split(":")[0])
                headers.append(info_detail.split(":",1)[0]) 
        elif i == 2:
            continue
        else:
            headers.append(informations[i].text.split(":",1)[0])
    
    driver.get('https://www.edbi.ir/web_directory/41640-%D8%B4%D8%B9%D8%A8-%D8%AF%D8%A7%D8%AE%D9%84%DB%8C.html')

    pages = driver.find_elements(By.TAG_NAME, 'h3')

    for i in range(len(pages)-3):
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

                                branch_name.click()
                                time.sleep(3)  # Wait for the new page to load

                                div = driver.find_element(By.CLASS_NAME, 'MainDivBankbranch')
                                informations = div.find_elements(By.TAG_NAME,'div') 

                                row_data = []

                                for j in range(len(informations)):
                                    # print(i,j)
                                    # print(informations[i].text.splitlines())
                                    # print(i)
                                    if j == 0:
                                        if ' ' in informations[j].text:
                                            row_data.append(informations[j].text.split(" ",1)[1])
                                        else:
                                            row_data.append(informations[j].text)
                                    elif j == 1: 
                                        # print('poi')
                                        info_details = informations[j].text.splitlines()
                                        for info_detail in info_details:
                                            if ':' in info_detail:
                                                row_data.append(info_detail.split(":",1)[1])
                                            else:
                                                row_data.append(info_detail)
                                    elif j == 2:
                                        continue
                                    else:
                                        row_data.append(informations[j].text.split(":",1)[0])

                                    # print(row_data)

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

                        div = driver.find_element(By.CLASS_NAME, 'MainDivBankbranch')
                        informations = div.find_elements(By.TAG_NAME,'div') 

                        row_data = []

                        for j in range(len(informations)):
                            # print(i,j)
                            # print(informations[i].text.splitlines())
                            # print(i)
                            if j == 0:
                                if ' ' in informations[j].text:
                                    row_data.append(informations[j].text.split(" ",1)[1])
                                else:
                                    row_data.append(informations[j].text)
                            elif j == 1: 
                                # print('poi')
                                info_details = informations[j].text.splitlines()
                                for info_detail in info_details:
                                    if ':' in info_detail:
                                        row_data.append(info_detail.split(":",1)[1])
                                    else:
                                        row_data.append(info_detail)
                            elif j == 2:
                                continue
                            else:
                                row_data.append(informations[j].text.split(":",1)[0])

                            # print(row_data)

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

    # df = pd.DataFrame(data)
    # # df.columns = ['Column1', 'Column2', 'Column3']  # Replace with actual column names as needed
    # df.to_excel('mehreiranian_bank_data.xlsx', index=False)

    # # # Create a DataFrame and save to Excel
    # df_headers = pd.DataFrame(headers)  # Use the headers as columns
    # df_headers.to_excel('branch_data_headers.xlsx', index=False)

    df_branches = pd.DataFrame(data, columns=headers)  # Use the headers as columns
    df_branches.to_excel('toseesaderat_bank_branches.xlsx', index=False)

finally:
    # Close the driver
    driver.quit()




    
# try:

#     # Open the URL
#     driver.get('https://www.edbi.ir/web_directory/41642-%D8%B4%D8%B9%D8%A8-%D8%B4%D9%87%D8%B1%D8%B3%D8%AA%D8%A7%D9%86-%D9%87%D8%A7.html')

#     # wait = WebDriverWait(driver, 10)  
#     # wait.until(EC.presence_of_element_located((By.TAG_NAME, 'form')))
    
#     # headers_counter = 0

#     time.sleep(5)

#     div = driver.find_element(By.CLASS_NAME, 'navigator2-cell')
#     print('y')
#     next_page_clicked_number = div.find_elements(By.CLASS_NAME,'navigator-item')
    
#     for i in range(len(next_page_clicked_number)+1):
#         try:

#             # time.sleep(5)
#             div = driver.find_element(By.CLASS_NAME, 'navigator2-cell')
#             next_page_clicked_number = div.find_elements(By.CLASS_NAME,'navigator-item')


#             # print(next_page_clicked_number[i].get_attribute('innerHTML'))

#             divs = driver.find_elements(By.CLASS_NAME, 'cntService')
#             temp = 1
#             for i in range(temp):

#                 try:    
#                     # Re-fetch elements to avoid stale references
#                     divs = driver.find_elements(By.CLASS_NAME, 'cntService')
#                     contentTextContainer = divs[i].find_element(By.CLASS_NAME,'contentTextContainer')
#                     branch_name = contentTextContainer.find_element(By.TAG_NAME,'a')

#                     print(f'Clicking on: {branch_name.text}')  # Debug print

#                     branch_name.click()
#                     time.sleep(3)  # Wait for the new page to load

#                     div = driver.find_element(By.CLASS_NAME, 'MainDivBankbranch')
#                     informations = div.find_elements(By.TAG_NAME,'div') 

#                     row_data = []

#                     for j in range(len(informations)):
#                         # print(i,j)
#                         # print(informations[i].text.splitlines())
#                         # print(i)
#                         if j == 0:
#                             if ' ' in informations[j].text:
#                                 row_data.append(informations[j].text.split(" ",1)[1])
#                             else:
#                                 row_data.append(informations[j].text)
#                         elif j == 1: 
#                             # print('poi')
#                             info_details = informations[j].text.splitlines()
#                             for info_detail in info_details:
#                                 if ':' in info_detail:
#                                     row_data.append(info_detail.split(":",1)[1])
#                                 else:
#                                     row_data.append(info_detail)
#                         elif j == 2:
#                             continue
#                         else:
#                             row_data.append(informations[j].text.split(":",1)[0])

#                                     # print(row_data)

#                         data.append(row_data)
#                         # Go back to the previous page
#                         driver.back()
#                         time.sleep(3)  # Wait for the original page to reload

#                         # Ensure we are still referencing the correct list of divs
#                         divs = driver.find_elements(By.CLASS_NAME, 'cntService')

#                 except StaleElementReferenceException:
#                     # Re-fetch the list if a StaleElementReferenceException is caught
#                     print("Caught StaleElementReferenceException, re-fetching links.")
#                     divs = driver.find_elements(By.CLASS_NAME, 'cntService')

#                 except Exception as e:
#                     print(f"An error occurred: {e}")
#                     break  # Exit the loop if an unexpected error occurs

#             # if i == len(next_page_clicked_number):

#             #     continue 
            
#             # next_page_button = WebDriverWait(driver, 10).until(
#             #     EC.element_to_be_clickable((By.CLASS_NAME, 'navigator-next'))
#             # )
#             # # next_page_button = div.find_element(By.CLASS_NAME,'navigator-next')
#             # next_page_button.click()

#             next_page_button = driver.find_element(By.CLASS_NAME, 'navigator-next')
#             is_visible = driver.execute_script("return arguments[0].offsetParent !== null;", next_page_button)
#             if is_visible:
#                 next_page_button.click()
#             else:
#                 print("Next page button is not visible.")

            
#             time.sleep(3)

#             div = driver.find_element(By.CLASS_NAME, 'navigator2-cell')
#             next_page_clicked_number = div.find_elements(By.CLASS_NAME,'navigator-item')

#         except StaleElementReferenceException:
#             # print("Caught StaleElementReferenceException, re-fetching links.")
#             div = driver.find_element(By.CLASS_NAME, 'navigator2-cell')
#             next_page_clicked_number = div.find_elements(By.CLASS_NAME,'navigator-item')

# except NoSuchElementException:

#     print('n')

# finally:
#     # Close the driver
#     driver.quit()
