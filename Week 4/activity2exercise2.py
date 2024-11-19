import pandas as pd

# Load the dataset
df = pd.read_csv('SalesData.csv')

# 1. Sales for P2 and B8 in Nov-18, Feb-19, and Mar-19
# Filter rows for P2 and B8 and select the relevant columns
sales_p2 = df.loc[df['Unnamed: 0'] == 'P2', ['Unnamed: 0', 'Nov-18', 'Feb-19', 'Mar-19']]
sales_b8 = df.loc[df['Unnamed: 0'] == 'B8', ['Unnamed: 0', 'Nov-18', 'Feb-19', 'Mar-19']]
sales_p2_b8 = pd.concat([sales_p2, sales_b8])
print("Sales for P2 and B8 in Nov-18, Feb-19, and Mar-19:")
print(sales_p2_b8)

# 2. Sales figures for London (L3 & L2) in Q3 (Oct-18 to Dec-18) and monthly percentage increase
# Filter rows for L3 and L2
sales_l3 = df.loc[df['Unnamed: 0'] == 'L3', ['Unnamed: 0', 'Oct-18', 'Nov-18', 'Dec-18']]
sales_l2 = df.loc[df['Unnamed: 0'] == 'L2', ['Unnamed: 0', 'Oct-18', 'Nov-18', 'Dec-18']]
sales_london_q3 = pd.concat([sales_l3, sales_l2])

# Calculate percentage increases
sales_london_q3['Nov-Dec % Increase'] = (sales_london_q3['Dec-18'] - sales_london_q3['Nov-18']) / sales_london_q3['Nov-18'] * 100
sales_london_q3['Oct-Nov % Increase'] = (sales_london_q3['Nov-18'] - sales_london_q3['Oct-18']) / sales_london_q3['Oct-18'] * 100
print("\nLondon Sales (Q3: Oct-18 to Dec-18) and Monthly Percentage Increase:")
print(sales_london_q3)

# 3. Top three months for New York (N6 and N4) and their stores
# Filter rows for N6 and N4
sales_n6 = df.loc[df['Unnamed: 0'] == 'N6']
sales_n4 = df.loc[df['Unnamed: 0'] == 'N4']
sales_ny = pd.concat([sales_n6, sales_n4])

# Find top three months
months = sales_ny.columns[1:]
top_ny_sales = []
for i, row in sales_ny.iterrows():
    for month in months:
        top_ny_sales.append((row['Unnamed: 0'], month, row[month]))

top_ny_sales = sorted(top_ny_sales, key=lambda x: x[2], reverse=True)[:3]
print("\nTop Three Months for New York Stores (N6 and N4):")
print(pd.DataFrame(top_ny_sales, columns=['Store', 'Month', 'Sales']))

# 4. Overall lowest sales figure, store, and month
lowest_sales = None
lowest_value = float('inf')
for i, row in df.iterrows():
    for month in df.columns[1:]:
        if row[month] < lowest_value:
            lowest_value = row[month]
            lowest_sales = (row['Unnamed: 0'], month, lowest_value)

print("\nOverall Lowest Sales Figure:")
print(pd.DataFrame([lowest_sales], columns=['Store', 'Month', 'Sales']))
