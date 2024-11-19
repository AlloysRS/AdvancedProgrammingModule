import pandas as pd

# Create a matrix
matrix = [
    ["1A", "2A", "3A", "4A"],
    ["1B", "2B", "3B", "4B", "5B"],
    ["1C", "2C", "3C"]
]

# Normalize the matrix to have equal column lengths (fill empty spaces with None or NaN)
max_length = max(len(row) for row in matrix)
normalized_matrix = [row + [None] * (max_length - len(row)) for row in matrix]

# Create a pandas DataFrame from the normalized matrix
df = pd.DataFrame(normalized_matrix)

# Display the DataFrame
print("Matrix as a DataFrame:")
print(df)

# Access individual elements
row_index, col_index = 0, 0  # Top left element
print("\nAccessing specific element (top left):", df.iloc[row_index, col_index])

row_index, col_index = 2, 2  # Bottom right element of the normalized matrix
print("Accessing specific element (bottom right):", df.iloc[row_index, col_index])

# Access an entire row
row_index = 1
print("\nAccessing Row", row_index, ":")
print(df.iloc[row_index, :])

# Access an entire column
col_index = 2
print("\nAccessing Column", col_index, ":")
print(df.iloc[:, col_index])

# Access a block of data (2 rows and 2 columns)
row_range = slice(0, 2)  # Rows 0 to 1
col_range = slice(1, 3)  # Columns 1 to 2
print("\nAccessing a block of data (2 rows, 2 columns):")
print(df.iloc[row_range, col_range])
