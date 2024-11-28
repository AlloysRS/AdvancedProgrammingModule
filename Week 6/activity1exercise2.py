import pandas as pd
from activity1exercise1 import step_1_process, step_2_transform

# PROCESSING

# Using processing steps from previous exercise, process both datasets into a long data format for ease of use.
step_1_process('CollegeGrades1.csv', 'Act1_Exc2_College_Grades_1_Interim.csv')
step_2_transform('Act1_Exc2_College_Grades_1_Interim.csv', 'Act1_Exc2_College_Grades_1_Final.csv')
step_1_process('CollegeGrades2.csv', 'Act1_Exc2_College_Grades_2_Interim.csv')
step_2_transform('Act1_Exc2_College_Grades_2_Interim.csv', 'Act1_Exc2_College_Grades_2_Final.csv')

# Load the data and rename headers as CollegeGrades2.csv differs slightly from CollegeGrades1, then save
college_grades_2 = pd.read_csv(
    'Act1_Exc2_College_Grades_2_Final.csv',
    header=0,
    names=['Area', 'Subject', 'Grade', 'Gender', 'Age', 'Value']
)
college_grades_2.to_csv('Act1_Exc2_College_Grades_2_Final.csv', index=False)

# Load in tidied College Grades from both datasets into pandas dataframe
college_grades_1 = pd.read_csv('Act1_Exc2_College_Grades_1_Final.csv')
college_grades_2 = pd.read_csv('Act1_Exc2_College_Grades_2_Final.csv')

# Assuming that Year 1 maps to ages 16-17, and Year 2 maps to ages 17-18, map these and use to merge
age_to_year_mapping = {
    "16-17": "Year 1",
    "17-18": "Year 2"
}
college_grades_2['Time'] = college_grades_2['Age'].map(age_to_year_mapping)
college_grades_2 = college_grades_2.drop(columns=['Age'])

# Standardise column names for merging
college_grades_1 = college_grades_1.rename(columns={'Time': 'Year'})
college_grades_2 = college_grades_2.rename(columns={'Time': 'Year'})

# Filter out "Evening" data as only merging based on Year 1 and Year 2
college_grades_1 = college_grades_1[college_grades_1['Year'].isin(['Year 1', 'Year 2'])]
college_grades_2 = college_grades_2[college_grades_2['Year'].isin(['Year 1', 'Year 2'])]

## MERGE AND SUMMARISE

# Merge the two datasets into one long dataset
merged_data = pd.concat([college_grades_1, college_grades_2], ignore_index=True)

# Summarise by summing 'Value' for duplicate rows and group by Area, Subject, Grade, Gender, Year
merged_data = merged_data.groupby(['Area', 'Subject', 'Grade', 'Gender', 'Year'], as_index=False).sum()

merged_data.to_csv('Merged_College_Grades.csv')

print(merged_data)

## TASK 1: Descriptive statistics filtered to specific subjects

# Filter for relevant subjects into a filtered data subset
relevant_subjects = ['Mathematics', 'English', 'Technology']
filtered_data = merged_data[merged_data['Subject'].isin(relevant_subjects)]

# Generate descriptive statistics for Year 1 and Year 2 performance for filtered dataset
descriptive_stats = filtered_data.groupby(['Subject', 'Year'])['Value'].describe()
print("Descriptive Statistics:")
print(descriptive_stats)

## TASK 2: Failure rates by subject and gender

# Filter for failing data (Grade = 'F')
failures_data = merged_data[merged_data['Grade'] == 'F']

# Calculate the percentage of males and females failing in each subject
failure_percentages = (
    failures_data.groupby(['Subject', 'Gender'])['Value'].sum()
    / merged_data.groupby(['Subject', 'Gender'])['Value'].sum()
) * 100

# Unstack the data
failure_percentages = failure_percentages.unstack()

# Display the results
print("Percentage of Males and Females Failing (All Subjects):")
print(failure_percentages)

## TASK 3: Female vs Male M/D rates

# Filter data for Merit (M) and Distinction (D)
merit_distinction_data = merged_data[merged_data['Grade'].isin(['M', 'D'])]

# Calculate the total count of Merit/Distinction for each Subject and Gender
merit_distinction_totals = merit_distinction_data.groupby(['Subject', 'Gender'])['Value'].sum()

# Calculate the overall total counts for each Subject and Gender
overall_totals = merged_data.groupby(['Subject', 'Gender'])['Value'].sum()

# Calculate the rate of attaining Merit/Distinction
merit_distinction_rates = (merit_distinction_totals / overall_totals) * 100

# Unstack the data
merit_distinction_rates = merit_distinction_rates.unstack()

# Filter the data to where females perform better than males (higher Merit/Distinction rate)
better_subjects_for_females = merit_distinction_rates[merit_distinction_rates['F'] > merit_distinction_rates['M']]

# Display the results
print("Subjects where females perform better than males (based on Merit/Distinction rates):")
print(better_subjects_for_females)