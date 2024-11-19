import numpy as np
import pandas as pd

csv_file = 'RandomeValues.csv'

# Step 1: Import csv file data and insert into a NumPy array
data = pd.read_csv(csv_file)
data_array = data.to_numpy()

# Step 2: Print the data in rows 5, 7 and 9.
rows_5_7_9 = data_array[[5, 7, 9], :]
print("Data for rows 5, 7 and 9:\n", rows_5_7_9)
print()

# Step 3: Print the data in columns 0, 7, 10:
columns_0_7_10 = data_array[:, [0, 7, 10]]
print("Data for columns 0, 7, and 10:\n", columns_0_7_10)
print()

# Step 4: Print the data in columns 1 to 3 exclusively, and from rows 7 to 9 inclusively
# For this exercise, I assume this means give columns 1 and 2 but not 3, and give rows 7, 8 and 9
columns_1_to_3_rows_7_to_9 = data_array[7:10, 1:3]
print("Data for columns 1 and 2, and rows 7, 8, and 9:\n", columns_1_to_3_rows_7_to_9)