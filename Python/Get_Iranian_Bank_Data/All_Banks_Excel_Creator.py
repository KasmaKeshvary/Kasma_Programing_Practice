import os
import time
import sys
import pandas as pd

config_directory = r'C:\Users\Kasma\Desktop\Kasma_Programming_Practice\Python\Get_Iranian_Bank_Data'
sys.path.append(config_directory)

from config import EXCEL_TARGET_DIRECTORY

def bankNameInPersian(value):
    match value:
        case'ayandeh':
            return 'آینده'
        case'dey':
            return 'دی'
        case'iranzamin':
            return 'ایران زمین'
        case'karafarin':
            return 'کارآفرین'
        case'khavarmianeh':
            return 'خاورمیانه'
        case'mehreiranian':
            return 'مهر ایرانیان'
        case'melli':
            return 'ملی'
        case'parsian':
            return 'پارسیان'
        case'resalat':
            return 'رسالت'
        case'saman':
            return 'سامان'
        case'sarmaie':
            return 'سرمایه'
        case'sepah':
            return 'سپه'
        case'sina':
            return 'سینا'
        case'tejarat':
            return 'تجارت'
        case'toseetaovon':
            return 'توسعه تعاون'
        
# print(os.listdir(EXCEL_TARGET_DIRECTORY))

# for fname in os.listdir(EXCEL_TARGET_DIRECTORY):
#     if fname.endswith(('.xls', '.xlsx')):
#         print(fname)
#         persianBankName = bankNameInPersian(fname.split('_',1)[0])
#         print(persianBankName)

# List files and read data from the first row of the first Excel file
print(os.listdir(EXCEL_TARGET_DIRECTORY))
excel_files = [fname for fname in os.listdir(EXCEL_TARGET_DIRECTORY) if fname.endswith(('.xls', '.xlsx'))]

if excel_files:
    first_file = excel_files[1]  # Get the first Excel file
    print(f'First Excel file: {first_file}')

    # Read the Excel file
    file_path = os.path.join(EXCEL_TARGET_DIRECTORY, first_file)
    df = pd.read_excel(file_path)

    # Print the first row
    first_row = df.iloc[0]  # Get the first row
    print('First row data:')
    print(first_row)

    # Print Persian bank name if needed
    persianBankName = bankNameInPersian(first_file.split('_', 1)[0])
    print(persianBankName)
else:
    print('No Excel files found in the directory.')

