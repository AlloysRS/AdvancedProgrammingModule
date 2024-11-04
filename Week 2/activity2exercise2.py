# Import required modules
import csv
from datetime import datetime

# Relative file path of csv data
file_path = "PeopleTrainngDate.csv"
output_file_path = "SortedPeopleTrainingDate.csv"

# Initialise empty list to store row data
data_rows = []

# Open csv file in read mode and store rows data
with open(file_path, mode='r', newline='') as file:
    rows = csv.DictReader(file)
    
    # Loop through each row and add it to data_rows
    for row in rows:
        data_rows.append(row)

# Sort data by 'Updated' date (oldest first) <- Thanks https://blogboard.io/blog/knowledge/python-sorted-lambda/
data_rows = sorted(data_rows, key=lambda date_value: datetime.strptime(date_value['Updated'], '%d/%m/%Y'), reverse=False)

# Define new order of headers with 'Updated' as the first column
headers = ['Updated', 'Title', 'Name', 'ID', 'Email', 'Company']

# Write sorted data to a new csv file with 'Updated' as the first column
with open(output_file_path, mode='w', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data_rows)

print("Data has been successfully sorted and written to", output_file_path)

