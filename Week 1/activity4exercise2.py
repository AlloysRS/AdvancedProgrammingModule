# Dictionary of lists to represent sales data
sales_data = {
    "L3": [390, 345, 379],  # London: April, May, June
    "P2": [250, 270, 300],  # Paris: April, May, June
    "N6": [460, 480, 450],  # New York: April, May, June
    "B8": [470, 510, 360]   # Beijing: April, May, June
}

# Initialise totals
grand_total = 0
monthly_totals = [0, 0, 0]

# Display sales by month and add to monthly totals list
print("Sales by Month Table")
print("Outlet\tApril\tMay\tJune")
for outlet, sales in sales_data.items():
    outlet_total = sum(sales)
    grand_total += outlet_total
    for i in range(3):
        monthly_totals[i] += sales[i]
    print(f"{outlet}\t{sales[0]}\t{sales[1]}\t{sales[2]}")

# Print monthly totals
print("\nMonthly Totals:")
print(f"April: {monthly_totals[0]}, May: {monthly_totals[1]}, June: {monthly_totals[2]}")

# Print outlet totals
print("\nOutlet Totals:")
for outlet, sales in sales_data.items():
    print(f"{outlet} Total: {sum(sales)}")

# Print grand total
print(f"\nGrand Total for the Quarter: {grand_total}")

# Print averages
print("\nAverages:")
for outlet, sales in sales_data.items():
    print(f"{outlet} Average: {sum(sales) / 3:.2f}")

# Print monthly averages
print("Monthly Averages:")
i = 1
for month_total in monthly_totals:
    print(f"Month {i} Average: {month_total / len(sales_data):.2f}")
    i += 1