import openpyxl

def get_data_from_excel(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data = []

    # Skip the header row (row 1)
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)
    return data
