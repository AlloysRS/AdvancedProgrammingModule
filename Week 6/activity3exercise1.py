import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Function to create random data
def generate_random_data():
    np.random.seed(42)
    data = {
        "Category": np.random.choice(["A", "B", "C", "D"], size=100),
        "Values1": np.random.randn(100),
        "Values2": np.random.rand(100) * 100,
    }
    return pd.DataFrame(data)

# Chart functions
def line_chart():
    data = generate_random_data()
    plt.figure()
    plt.plot(data.index, data["Values1"], label="Values1")
    plt.title("Line Chart")
    plt.xlabel("Index")
    plt.ylabel("Values")
    plt.legend()
    plt.show()

def bar_chart():
    data = generate_random_data()
    aggregated = data.groupby("Category").mean()
    plt.figure()
    aggregated["Values2"].plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Bar Chart")
    plt.ylabel("Average Value")
    plt.show()

def scatter_plot():
    data = generate_random_data()
    plt.figure()
    plt.scatter(data["Values1"], data["Values2"], alpha=0.7)
    plt.title("Scatter Plot")
    plt.xlabel("Values1")
    plt.ylabel("Values2")
    plt.show()

def heatmap():
    data = np.random.rand(10, 10)
    plt.figure()
    sns.heatmap(data, annot=True, cmap="coolwarm")
    plt.title("Heatmap")
    plt.show()

def box_plot():
    data = generate_random_data()
    plt.figure()
    sns.boxplot(x="Category", y="Values1", data=data, palette="Set3")
    plt.title("Box Plot")
    plt.show()

# Main application window
def main():
    root = tk.Tk()
    root.title("Chart Viewer")

    tk.Label(root, text="Click a button to view a chart:", font=("Helvetica", 14)).pack(pady=10)

    # Buttons for each chart type
    tk.Button(root, text="Line Chart", command=line_chart, width=20).pack(pady=5)
    tk.Button(root, text="Bar Chart", command=bar_chart, width=20).pack(pady=5)
    tk.Button(root, text="Scatter Plot", command=scatter_plot, width=20).pack(pady=5)
    tk.Button(root, text="Heatmap", command=heatmap, width=20).pack(pady=5)
    tk.Button(root, text="Box Plot", command=box_plot, width=20).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
