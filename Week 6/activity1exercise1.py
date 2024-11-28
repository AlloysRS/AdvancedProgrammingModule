import pandas as pd

def step_1_process(input_file: str, cleaned_file_path: str):
    # Step 1: Process the raw data to extract headers, create hierarchical headers, and clean the dataset.
    # Load the data from the CSV
    data = pd.read_csv(input_file, header=None)
    
    # Extract headers and data
    header_rows = data.iloc[:4]  # First four rows contain headers
    data_rows = data.iloc[4:].reset_index(drop=True)  # Remaining rows contain the data
    
    # Create hierarchical headers
    header_cleaned = header_rows.fillna(method='ffill', axis=1)  # Forward fill to clean headers
    grades = header_cleaned.iloc[0].fillna('')
    subjects = header_cleaned.iloc[2].fillna('')
    
    # Combine the two header levels into a MultiIndex
    columns = pd.MultiIndex.from_tuples(zip(grades, subjects), names=["Location", "Subject"])
    
    # Assign headers to the data
    data_rows.columns = columns
    
    # Drop completely empty rows
    data_cleaned = data_rows.dropna(how='all').reset_index(drop=True)
    
    # Forward fill down the first column (Year, Evening, etc.)
    data_cleaned.iloc[:, 0] = data_cleaned.iloc[:, 0].fillna(method='ffill')

    # Save cleaned data to a CSV - Interim step
    data_cleaned.to_csv(cleaned_file_path, index=False)
    print(f"Cleaned data saved to {cleaned_file_path}")
    #print(data_cleaned.head())

def step_2_transform(cleaned_file_path: str, tidy_file_path: str):
    # Step 2: Transform the cleaned dataset into a tidy long data format.
    # Load the cleaned data
    df = pd.read_csv(cleaned_file_path, header=None)
    
    # Extract relevant header rows and handle missing values
    area = df.iloc[0].fillna(method='ffill')  # First row: Area
    subject = df.iloc[1].fillna(method='ffill')  # Second row: Subject
    grade = df.iloc[2]  # Third row: Grade (no need to fill)
    
    # Drop the first three rows (headers) from the data
    data = df.iloc[3:].reset_index(drop=True)
    
    # Assign new multi-level columns
    data.columns = pd.MultiIndex.from_arrays([area, subject, grade], names=["Area", "Subject", "Grade"])
    
    # Extract 'Time' and 'Gender' columns (first two original columns)
    data.insert(0, "Time", df.iloc[3:, 0].values)
    data.insert(1, "Gender", df.iloc[3:, 1].values)
    
    # Melt the data to long format
    tidy_data = data.melt(
        id_vars=["Time", "Gender"],
        var_name=["Area", "Subject", "Grade"],
        value_name="Value"
    )
    
    # Reorganize columns into the desired order
    tidy_data = tidy_data[["Area", "Subject", "Grade", "Time", "Gender", "Value"]]
    
    # Remove rows with missing or empty values
    tidy_data = tidy_data.dropna(subset=["Area", "Subject", "Grade", "Time", "Gender", "Value"])
    tidy_data = tidy_data[tidy_data["Value"] != ""]  # Exclude empty Value rows, if applicable

    # Define typo corrections for Subject and Area
    typo_corrections = {
        "Subject": {
            "Phsyics": "Physics",
            "Chemisrty": "Chemistry",
            "Psycology": "Psychology",
            "Enginering": "Engineering"
        },
        "Area": {
            "Darligton": "Darlington",
            "Scarborugh": "Scarborough"
        }
    }

    # Fix typos inplace
    tidy_data.replace(typo_corrections, inplace=True)
    
    # Save the tidy dataset
    tidy_data.to_csv(tidy_file_path, index=False)
    print(f"Tidy data saved to {tidy_file_path}")
    #print(tidy_data.head())

def step_3_pivot(tidy_file_path: str, pivot_file_path: str):
    # Step 3: Pivot the tidy dataset into the subject-by-grade-by-time format.
    # Load the tidy dataset
    tidy_data = pd.read_csv(tidy_file_path)
    
    # Pivot the data
    pivot_table = tidy_data.pivot_table(
        index=['Time'],                     # Time as rows
        columns=['Subject', 'Grade'],    # Subject as headers and Grade as subheaders
        values='Value',                     # Values to aggregate
        aggfunc='sum'                       # Sum of values
    )
    
    # Reset index for clarity
    pivot_table = pivot_table.reset_index()
    
    # Save the pivoted dataset
    pivot_table.to_csv(pivot_file_path, index=False)
    print(f"Pivoted data saved to {pivot_file_path}")
    #print(pivot_table.head())

def step_4_pivot(tidy_file_path: str, pivot_file_path: str):
    # Step 4: Pivot the tidy dataset into the area-by-grade-by-gender format.
    # Load the tidy dataset
    tidy_data = pd.read_csv(tidy_file_path)
    
    # Pivot the data
    pivot_table = tidy_data.pivot_table(
        index=['Gender'],                  # Gender as rows
        columns=['Area', 'Grade'],      # Area as headers and Grade as subheaders
        values='Value',                    # Values to aggregate
        aggfunc='sum'                      # Sum of values
    )
    
    # Reset index for clarity
    pivot_table = pivot_table.reset_index()
    
    # Save the pivoted dataset
    pivot_table.to_csv(pivot_file_path, index=False)
    print(f"Reformatted data saved to {pivot_file_path}")
    #print(pivot_table.head())

step_1_process('CollegeGrades1.csv', 'Act1_Exc1_College_Grades_Interim.csv')
step_2_transform('Act1_Exc1_College_Grades_Interim.csv', 'Act1_Exc1_College_Grades_Final.csv')
step_3_pivot('Act1_Exc1_College_Grades_Final.csv', 'Act1_Exc1_College_Grades_Pivoted_Output_A.csv')
step_4_pivot('Act1_Exc1_College_Grades_Final.csv', 'Act1_Exc1_College_Grades_Pivoted_Output_B.csv')