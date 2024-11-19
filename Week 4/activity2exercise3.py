import pandas as pd

# Load the dataset
df = pd.read_csv('SalesData.csv')

# 1. Create a new data table with percentage increases for each month based on the store's average for the year
# Calculate the store's yearly average
df['Yearly Average'] = df.iloc[:, 1:].mean(axis=1)

# Calculate percentage increase for each month based on the yearly average
percentage_increase = df.copy()
for month in df.columns[1:-1]:
    percentage_increase[month] = (df[month] - df['Yearly Average']) / df['Yearly Average'] * 100

# Drop the yearly average column from the percentage table to match the new data table
percentage_increase.drop(columns=['Yearly Average'], inplace=True)

print("\nPercentage Increase Table:")
print(percentage_increase)

# 2. Determine which store had the largest and smallest increase and in which months they occurred
largest_increase = None
smallest_increase = None
largest_value = float('-inf')
smallest_value = float('inf')

for i, row in percentage_increase.iterrows():
    for month in percentage_increase.columns[1:]:
        if row[month] > largest_value:
            largest_value = row[month]
            largest_increase = (row['Unnamed: 0'], month, largest_value)
        if row[month] < smallest_value:
            smallest_value = row[month]
            smallest_increase = (row['Unnamed: 0'], month, smallest_value)

print("\nStore with the Largest Increase:")
print(pd.DataFrame([largest_increase], columns=['Store', 'Month', 'Percentage Increase']))

print("\nStore with the Smallest Increase:")
print(pd.DataFrame([smallest_increase], columns=['Store', 'Month', 'Percentage Increase']))

# 3. Determine across all stores which months showed the smallest and largest average increase
average_increases = {}
for month in percentage_increase.columns[1:]:
    average_increases[month] = percentage_increase[month].mean()

smallest_avg_increase = min(average_increases, key=average_increases.get)
largest_avg_increase = max(average_increases, key=average_increases.get)

print("\nMonth with the Smallest Average Increase:")
print(pd.DataFrame([(smallest_avg_increase, average_increases[smallest_avg_increase])], columns=['Month', 'Average Increase']))

print("\nMonth with the Largest Average Increase:")
print(pd.DataFrame([(largest_avg_increase, average_increases[largest_avg_increase])], columns=['Month', 'Average Increase']))
