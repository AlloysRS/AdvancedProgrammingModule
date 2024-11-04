# Import required modules
import csv
from tabulate import tabulate

# Relative file path of csv data
file_path = "PeopleTrainngDate.csv"

# Initialise empty lists for each column for further processing if required
title_list = []
name_list = []
id_list = []
email_list = []
company_list = []
updated_list = []

# Open csv file in read mode and store rows data
with open(file_path, mode='r', newline='') as file:
    rows = csv.DictReader(file)
    
    # Loop through each row and append data to each list
    for row in rows:
        title_list.append(row['Title'])
        name_list.append(row['Name'])
        id_list.append(row['ID'])
        email_list.append(row['Email'])
        company_list.append(row['Company'])
        updated_list.append(row['Updated'])

# Combine all columns into a list of lists for easy processing
headers = ['Title', 'Name', 'ID', 'Email', 'Company', 'Updated']
columns = [title_list, name_list, id_list, email_list, company_list, updated_list]

# Transpose columns to create rows for each record
data = list(zip(*columns))

# Display data in a neat table format
print(tabulate(data, headers=headers, tablefmt="grid"))
