# Import required modules
import csv
from datetime import datetime

# Define relative file paths
new_file_path = "PeopleTrainingDateUpdate.csv"
sorted_file_path = "SortedPeopleTrainingDate.csv"

# Headers for the new data format
headers = ['Updated', 'Title', 'Name', 'ID', 'Email', 'Company']

# Read data from the new file, no rows to skip as data has no headers
new_data_rows = []
with open(new_file_path, mode='r', newline='') as new_file:
    reader = csv.reader(new_file)
    for row in reader:
        # Assign headers and add 'NULL' for the missing 'ID' column, note the order relates to the prior file structure
        new_data_rows.append({
            'Updated': row[0],
            'Title': row[2],
            'Name': row[3],
            'ID': 'NULL',
            'Email': row[1],
            'Company': row[4]
        })

# Sort new data by 'Updated' date
new_data_rows = sorted(new_data_rows, key=lambda date_value: datetime.strptime(date_value['Updated'], '%d/%m/%Y'), reverse=False)

# Open csv in append mode and append sorted new data to the existing sorted file
with open(sorted_file_path, mode='a', newline='') as sorted_file:
    writer = csv.DictWriter(sorted_file, fieldnames=headers)
    
    # Write each row from new data
    for row in new_data_rows:
        writer.writerow(row)

print("New data has been successfully appended to", sorted_file_path)
