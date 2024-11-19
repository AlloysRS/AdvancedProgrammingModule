import pandas as pd
import numpy as np

# Step 1: Load the CSV file and extract headers and data into NumPy arrays
sales_data = pd.read_csv('SalesData.csv')
column_headers = sales_data.columns.to_numpy()
row_headers = sales_data.iloc[:, 0].to_numpy()
data_values = sales_data.iloc[:, 1:].to_numpy()


# Step 2: Print sales for the second quarter (Jul-18 to Sep-18 inclusive)
q2_sales = data_values[:, 6:9]
q2_totals = q2_sales.sum(axis=0)
q2_means = q2_sales.mean(axis=0)

print("Second Quarter (Jul-18 to Sep-18) Sales:")
print("Totals:", q2_totals)
print("Means:", q2_means)
print()

# Step 3: Print sales for stores L3 and L1 for the first and third quarters
row_headers_list = list(row_headers)
L3_index = row_headers_list.index('L3')
L1_index = row_headers_list.index('L1')
L3_sales = data_values[L3_index, :]
L1_sales = data_values[L1_index, :]
L3_q1_q3_sales = np.concatenate((L3_sales[0:3], L3_sales[9:12]))  
L1_q1_q3_sales = np.concatenate((L1_sales[0:3], L1_sales[9:12]))  
L3_total = L3_q1_q3_sales.sum()  
L3_mean = L3_q1_q3_sales.mean()  
L1_total = L1_q1_q3_sales.sum()  
L1_mean = L1_q1_q3_sales.mean() 

print("First and Third Quarter Sales for Store L3:")
print("Total Sales:", L3_total)
print("Mean Sales:", L3_mean)
print("First and Third Quarter Sales for Store L1:")
print("Total Sales:", L1_total)
print("Mean Sales:", L1_mean)
print()

# Step 4: Print sales for N6 and N4 lower than 400 and their corresponding months
row_headers_list = list(row_headers)
N6_index = row_headers_list.index('N6')
N4_index = row_headers_list.index('N4')
N6_sales = data_values[N6_index, :]
N4_sales = data_values[N4_index, :]

sales_below_400 = []
months_below_400 = []

for i in range(len(column_headers) - 1):
    if N6_sales[i] < 400:
        sales_below_400.append(N6_sales[i])
        months_below_400.append(column_headers[i + 1])
    elif N4_sales[i] < 400:
        sales_below_400.append(N4_sales[i])
        months_below_400.append(column_headers[i + 1])

sales_dict = dict(zip(months_below_400, sales_below_400))

print("Sales for N6 and N4 Below 400:\n", sales_dict)