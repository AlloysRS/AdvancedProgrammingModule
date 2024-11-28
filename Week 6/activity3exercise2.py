import pandas as pd
import matplotlib.pyplot as plt

# Load the combined dataset from activity1exercise2
data = pd.read_csv('Merged_College_Grades.csv')  # Replace with your file path

# Step 1: Calculate pass rates
data['Pass'] = data['Grade'].isin(['P', 'M', 'D'])
total_students = data.groupby(['Area', 'Subject', 'Year'])['Value'].sum().reset_index(name='Total Students')
passing_students = data[data['Pass']].groupby(['Area', 'Subject', 'Year'])['Value'].sum().reset_index(name='Passing Students')

performance_data = pd.merge(total_students, passing_students, how='left', on=['Area', 'Subject', 'Year'])
performance_data['Pass Rate (%)'] = (performance_data['Passing Students'] / performance_data['Total Students']) * 100

# Step 2: Create separate DataFrames for Year 1 and Year 2
year_1_performance = performance_data[performance_data['Year'] == 'Year 1']
year_2_performance = performance_data[performance_data['Year'] == 'Year 2']

# Calculate overall Year 2 pass rates by subject
overall_subject_pass_rates = year_2_performance.groupby('Subject')['Passing Students'].sum() / year_2_performance.groupby('Subject')['Total Students'].sum() * 100

# Step 3: Prepare data for Year 1 vs Year 2 comparison by area
areas = performance_data['Area'].unique()

# Plot overall Year 2 pass rates separately
fig1 = plt.figure(figsize=(10, 6))
ax1 = fig1.add_subplot(1, 1, 1)
overall_subject_pass_rates.sort_values().plot(kind='bar', ax=ax1, color='blue', alpha=0.7)
ax1.set_title("Overall Pass Rate (Year 2) by Subject")
ax1.set_ylabel("Pass Rate (%)")
ax1.set_xlabel("Subject")
ax1.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.show()

# Plot Year 1 vs Year 2 pass rates for each area on a 2x3 grid
fig2 = plt.figure(figsize=(16, 10))
n_cols = 3
n_rows = 2

plot_index = 1
for area in areas:
    ax = fig2.add_subplot(n_rows, n_cols, plot_index)
    
    # Filter data for the area
    year_1_area_data = year_1_performance[year_1_performance['Area'] == area]
    year_2_area_data = year_2_performance[year_2_performance['Area'] == area]
    
    # Merge Year 1 and Year 2 data for comparison
    merged_data = pd.merge(
        year_1_area_data[['Subject', 'Pass Rate (%)']].rename(columns={'Pass Rate (%)': 'Year 1'}),
        year_2_area_data[['Subject', 'Pass Rate (%)']].rename(columns={'Pass Rate (%)': 'Year 2'}),
        on='Subject',
        how='outer'
    ).set_index('Subject')
    
    # Plot the data
    merged_data.plot(kind='bar', ax=ax, color=["green", "red"], alpha=0.7)
    ax.set_title(f"Year 1 vs Year 2 Pass Rates in {area}")
    ax.set_ylabel("Pass Rate (%)")
    ax.set_xlabel("Subject")
    ax.tick_params(axis='x', rotation=45)
    
    plot_index += 1

# Adjust layout for the 2x3 grid
fig2.tight_layout()
plt.show()
