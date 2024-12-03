const XLSX = require('xlsx');
const path = require('path');

/**
 * Copies data from an old Excel file to a new Excel file.
 *
 * @param {string} oldFilePath - The directory of the old file.
 * @param {string} oldFileName - The name of the old file with extension.
 * @param {string} newFilePath - The directory where the new file should be saved.
 * @param {string} newFileName - The name of the new file with extension.
 */
function copyExcelFile(oldFilePath, oldFileName, newFilePath, newFileName) {
    // Construct the full old file path
    const sourceFilePath = path.join(oldFilePath, oldFileName);

    // Read the Excel file
    const workbook = XLSX.readFile(sourceFilePath);

    // Get the first sheet
    const sheetName = workbook.SheetNames[0]; 
    const sheet = workbook.Sheets[sheetName]; 

    // Convert the sheet data to JSON
    const data = XLSX.utils.sheet_to_json(sheet);

    // Print the first row (optional)
    console.log(data[0]);

    // Create a new workbook and add the sheet data
    const newWorkbook = XLSX.utils.book_new(); 
    const newSheet = XLSX.utils.json_to_sheet(data); 
    XLSX.utils.book_append_sheet(newWorkbook, newSheet, sheetName); 

    // Define the output file path
    const outputFilePath = path.join(newFilePath, newFileName);

    // Write the new workbook to the specified file
    XLSX.writeFile(newWorkbook, outputFilePath);

    console.log('Data copied and saved to:', outputFilePath);
}

// Example usage:
const oldFilePath = 'C:/Users/Kasma/Downloads';
const oldFileName = 'Data.xls';
const newFilePath = 'C:/Users/Kasma/Desktop/Kasma_Programming_Practice/Python/Get_Iranian_Bank_Data/Excel_Files_Of_Iranian_Banks_Branches';
const newFileName = 'New_Data.xlsx';

// Call the function to copy the Excel file
copyExcelFile(oldFilePath, oldFileName, newFilePath, newFileName);
