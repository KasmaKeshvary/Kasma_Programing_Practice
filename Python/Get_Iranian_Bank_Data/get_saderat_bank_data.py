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

# Specify the path to your webdriver
service = Service(r'C:\Users\Kasma\Desktop\Kasma_Programming_Practice\Python\chromedriver.exe')

# Initialize the WebDriver using the Service
driver = webdriver.Chrome(service=service)

# Create a list to hold data
headers = []
data = []

try:
    # Open the URL
    driver.get('https://www.bsi.ir/Pages/BankUnits/branches.aspx')
    driver.maximize_window()
    time.sleep(5)

    wait = WebDriverWait(driver, 10)  
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ms-listviewtable')))

    table = driver.find_element(By.CLASS_NAME, 'ms-listviewtable')
    tbody = table.find_element(By.TAG_NAME, 'tbody')
    rows = tbody.find_elements(By.TAG_NAME, 'tr')
    # print(rows[2].text)
    headerlink = rows[2].find_element(By.TAG_NAME, 'a')
    headerlink.click()
    time.sleep(4)
    headerTables = driver.find_elements(By.TAG_NAME, 'table')
    headerTbody = headerTables[0].find_element(By.TAG_NAME, 'tbody')
    headerSection = headerTbody.find_elements(By.TAG_NAME, 'tr')[0].find_element(By.TAG_NAME, 'table').find_elements(By.TAG_NAME, 'td')[1]
    headerSection.find_element(By.TAG_NAME, 'a').click()
    time.sleep(5)

    headerMain = driver.find_element(By.ID, 'WebPartWPQ3').find_elements(By.TAG_NAME, 'table')[4].find_elements(By.TAG_NAME, 'tr')
    for i in range(len(headerMain)):
        # print(headerMain[i].find_elements(By.TAG_NAME, 'td')[0].text.split(":",1)[0])
        headers.append(headerMain[i].find_elements(By.TAG_NAME, 'td')[0].text.split(":",1)[0])

    print(headers)

    driver.get('https://www.bsi.ir/Pages/BankUnits/branches.aspx')
    
    
    wait = WebDriverWait(driver, 10)  
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ms-listviewtable')))

    provincesTable = driver.find_element(By.CLASS_NAME, 'ms-listviewtable')
    provincesTbody = provincesTable.find_element(By.TAG_NAME, 'tbody')
    provincesRows = provincesTbody.find_elements(By.TAG_NAME, 'tr')

    for j in range(len(provincesRows))[2:]:
        print(provincesRows[j].text)
        try:
            provincesTable = driver.find_element(By.CLASS_NAME, 'ms-listviewtable')
            provincesTbody = provincesTable.find_element(By.TAG_NAME, 'tbody')
            provincesRows = provincesTbody.find_elements(By.TAG_NAME, 'tr')

            provincelink = provincesRows[j].find_element(By.TAG_NAME, 'a')
            
            print(f'Clicking on: {provincelink.text}')  # Debug print
            
            provincelink.click()
            time.sleep(4)

            wait = WebDriverWait(driver, 10)  
            wait.until(EC.presence_of_element_located((By.TAG_NAME, 'table')))

            citiesTable = driver.find_elements(By.TAG_NAME, 'table')[0]
            citiesTbody = citiesTable.find_element(By.TAG_NAME, 'tbody')
            cities = citiesTbody.find_elements(By.TAG_NAME, 'tr')
            
            for k in range(len(cities)):
                # print(cities[k].find_element(By.TAG_NAME, 'tr').find_elements(By.TAG_NAME, 'td')[1].text)
                tempCity = cities[k].find_elements(By.TAG_NAME, 'td')[0].find_elements(By.TAG_NAME, 'td')
                for l in range(len(tempCity)):
                    if l == 1 :
                        try :
                            
                            citiesTable = driver.find_elements(By.TAG_NAME, 'table')[0]
                            citiesTbody = citiesTable.find_element(By.TAG_NAME, 'tbody')
                            cities = citiesTbody.find_elements(By.TAG_NAME, 'tr')
                            tempCity = cities[k].find_elements(By.TAG_NAME, 'td')[0].find_elements(By.TAG_NAME, 'td')

                            cityLink = tempCity[l].find_element(By.TAG_NAME, 'a')
                            print(f'Clicking on City: {cityLink.text}')

                            cityLink.click()
                            time.sleep(4)

                            rowData = []

                            wait = WebDriverWait(driver, 5)  
                            wait.until(EC.presence_of_element_located((By.ID, 'WebPartWPQ3')))


                            dataMain = driver.find_element(By.ID, 'WebPartWPQ3').find_elements(By.TAG_NAME, 'table')[4].find_elements(By.TAG_NAME, 'tr')
                            for i in range(len(dataMain)):
                                if dataMain[i].find_elements(By.TAG_NAME, 'td')[1].text:
                                    # print(dataMain[i].find_elements(By.TAG_NAME, 'td')[1].text)
                                    rowData.append(dataMain[i].find_elements(By.TAG_NAME, 'td')[1].text)
                                else:
                                    rowData.append('')


                            print(rowData)
                            data.append(rowData)
                        

                            driver.back()
                            time.sleep(3)  # Wait for the original page to reload

                            citiesTable = driver.find_elements(By.TAG_NAME, 'table')[0]
                            citiesTbody = citiesTable.find_element(By.TAG_NAME, 'tbody')
                            cities = citiesTbody.find_elements(By.TAG_NAME, 'tr')
                            tempCity = cities[k].find_elements(By.TAG_NAME, 'td')[0].find_elements(By.TAG_NAME, 'td')


                        except StaleElementReferenceException:
                            # Re-fetch the list if a StaleElementReferenceException is caught
                            print("Caught StaleElementReferenceException, re-fetching links.")
                            citiesTable = driver.find_elements(By.TAG_NAME, 'table')[0]
                            citiesTbody = citiesTable.find_element(By.TAG_NAME, 'tbody')
                            cities = citiesTbody.find_elements(By.TAG_NAME, 'tr')
                            tempCity = cities[k].find_elements(By.TAG_NAME, 'td')[0].find_elements(By.TAG_NAME, 'td')


                        except Exception as e:
                            print(f"An error occurred: {e}")
                            break  # Exit the loop if an unexpected error occurs
        

            driver.back()
            time.sleep(3)  # Wait for the original page to reload


            provincesTable = driver.find_element(By.CLASS_NAME, 'ms-listviewtable')
            provincesTbody = provincesTable.find_element(By.TAG_NAME, 'tbody')
            provincesRows = provincesTbody.find_elements(By.TAG_NAME, 'tr')


        except StaleElementReferenceException:
            # Re-fetch the list if a StaleElementReferenceException is caught
            print("Caught StaleElementReferenceException, re-fetching links.")
            provincesTable = driver.find_element(By.CLASS_NAME, 'ms-listviewtable')
            provincesTbody = provincesTable.find_element(By.TAG_NAME, 'tbody')
            provincesRows = provincesTbody.find_elements(By.TAG_NAME, 'tr')

        except NoSuchElementException:
                # If the next page button does not exist, break the loop
                print("Next page button not found, ending pagination.")
                continue

        except Exception as e:
            print(f"An error occurred: {e}")
            break  # Exit the loop if an unexpected error occurs
                    


    df = pd.DataFrame(data)
    # df.columns = ['Column1', 'Column2', 'Column3']  # Replace with actual column names as needed
    df.to_excel('saderat_bank_data.xlsx', index=False)

    # # Create a DataFrame and save to Excel
    df_headers = pd.DataFrame(headers)  # Use the headers as columns
    df_headers.to_excel('saderat_headers.xlsx', index=False)

    df_branches = pd.DataFrame(data, columns=headers)  # Use the headers as columns
    df_branches.to_excel('saderat_bank_branches.xlsx', index=False)


finally:
    # Close the driver
    driver.quit()