# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# PROCESSING: Load and process birth data from text files in a directory
def load_birth_data(directory):
    # Define the column names for the resulting DataFrame
    columns = ["Name", "Gender", "Count", "Year"]
    births_data = pd.DataFrame(columns=columns)

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            year = int(filename[3:7])
            file_path = os.path.join(directory, filename)
            # Load the file data
            data = pd.read_csv(file_path, names=["Name", "Gender", "Count"])
            data["Year"] = year
            # Append the data to the master DataFrame
            births_data = pd.concat([births_data, data], ignore_index=True)
    births_data.reset_index(drop=True, inplace=True)
    return births_data

# TASK 1: Plot trends for randomly selected names
def plot_random_names(data):
    # Randomly select 5 unique male and 5 unique female names
    male_names = data[data["Gender"] == "M"]["Name"].drop_duplicates().sample(5, random_state=1)
    female_names = data[data["Gender"] == "F"]["Name"].drop_duplicates().sample(5, random_state=1)

    # Combine selected names
    selected_names = pd.concat([male_names, female_names])
    # Filter data for the selected names
    selected_data = data[data["Name"].isin(selected_names)]

    # Group the data by Year and Name, summing the Count values
    grouped = selected_data.groupby(["Year", "Name"])["Count"].sum().unstack(fill_value=0)

    # Plot the data
    grouped.plot(title="Number of Babies Given Selected Names (1880-2010)", figsize=(12, 6))
    plt.xlabel("Year")
    plt.ylabel("Number of Babies")
    plt.legend(title="Names")
    plt.tight_layout()
    plt.show()

# TASK 2: Plot total births by gender over time
def plot_births_by_gender(data):
    # Group the data by Year and Gender, summing the Count values
    gender_grouped = data.groupby(["Year", "Gender"])["Count"].sum().unstack(fill_value=0)

    # Plot the data
    gender_grouped.plot(title="Total Births by Gender (1880-2010)", figsize=(12, 6))
    plt.xlabel("Year")
    plt.ylabel("Number of Births")
    plt.legend(title="Gender")
    plt.tight_layout()
    plt.show()

# Define a function to display the top names by gender for a specific year
def top_names_by_year(data, year_to_review):
    # Filter data for the specified year
    year_data = data[data["Year"] == year_to_review]
    year_data["Count"] = pd.to_numeric(year_data["Count"], errors="coerce")  # Ensure Count column is numeric

    # Get the top 3 male and female names based on Count
    top_male = year_data[year_data["Gender"] == "M"].nlargest(3, "Count")
    top_female = year_data[year_data["Gender"] == "F"].nlargest(3, "Count")

    # Print the results
    print("Top 3 Male Names in", year_to_review)
    print(top_male[["Name", "Count"]])
    print("Top 3 Female Names in", year_to_review)
    print(top_female[["Name", "Count"]])

# Main script
if __name__ == "__main__":
    # Define the directory containing the dataset
    directory = r'datasets/babynames'

    # Load the data
    data = load_birth_data(directory)

    # Task 1: Plot random names
    plot_random_names(data)

    # Task 2: Plot births by gender
    plot_births_by_gender(data)

    # Task 3: Display top names for a specific year
    top_names_by_year(data, year_to_review=2000)
