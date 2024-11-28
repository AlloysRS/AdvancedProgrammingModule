import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt

# Load data
db = json.load(open("datasets/usda_food/database.json"))

# Extract nutrients
all_nutrients = []
for item in db:
    nutrients = pd.DataFrame(item["nutrients"])
    nutrients["id"] = item["id"]
    nutrients["description"] = item["description"]
    all_nutrients.append(nutrients)
nutrients_df = pd.concat(all_nutrients, ignore_index=True)

# Step 1: Statistics for Cheese-Based Products
cheese_products = [item for item in db if "cheese" in item["description"].lower()]
cheese_nutrients = pd.concat([pd.DataFrame(prod["nutrients"]) for prod in cheese_products], ignore_index=True)

# Generate statistics
cheese_stats = cheese_nutrients.groupby("description").value.describe()
print("Cheese Nutrients Statistics:")
print(cheese_stats)

# I have no idea what is being asked for by "each element" so I cannot implement this...