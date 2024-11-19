import pandas as pd
import uuid

# Load the data from CSV
file_path = 'PeoplesFavourites.csv'
data = pd.read_csv(file_path)

# Generate a unique identifier using uuid for each row
data['Unique ID'] = [uuid.uuid4() for _ in range(len(data))]

# Remove 'First Name' and 'Last Name' columns
data = data.drop(columns=['First Name', 'Last Name'])

# Replace inconsistent null values with null values
data = data.replace(['none', '0', '', 'NaN'], pd.NA)

# Remove rows with missing 'Email'
data = data.dropna(subset=['Email'])

# Save the cleaned dataset
cleaned_file_path = 'Cleaned_PeoplesFavourites.csv'
data.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")