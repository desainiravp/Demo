# script.py

import matplotlib
matplotlib.use('Agg')  # Set the Matplotlib backend to Agg (non-interactive)

import openpyxl
import os

def generate_excel_file(file_path):
    # Create a new Excel workbook
    workbook = openpyxl.Workbook()

    # Get the active sheet
    sheet = workbook.active

    # Add headers
    sheet['A1'] = 'Name'
    sheet['B1'] = 'Age'
    sheet['C1'] = 'City'

    # Add data
    data = [
        ('John Doe', 30, 'New York'),
        ('Jane Smith', 25, 'San Francisco'),
        ('Bob Johnson', 35, 'Chicago'),
    ]

    for row_idx, row_data in enumerate(data, start=2):
        for col_idx, value in enumerate(row_data, start=1):
            sheet.cell(row=row_idx, column=col_idx, value=value)

    # Apply bold font to header row
    for cell in sheet['1:1']:
        cell.font = openpyxl.styles.Font(bold=True)

    # Save the workbook to the specified file path
    workbook.save(file_path)

if __name__ == "__main__":
    # Specify the file path for the generated Excel file
    output_file_path = "/home/jenkins/devops_dev/workspace/gitrepo/generated_file.xlsx"

    # Generate the Excel file
    generate_excel_file(output_file_path)

    print(f"Excel file generated: {output_file_path}")

 
