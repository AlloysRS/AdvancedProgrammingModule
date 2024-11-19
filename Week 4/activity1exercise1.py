import numpy as np

# Step 1: Generate 10,000 random numbers in a 2D array
random_array = np.random.rand(100, 100)
# random_array = np.random.random((100, 100)) # Also does the same thing

# Step 2: Calculate the square root for each value in the array
sqrt_array = np.sqrt(random_array)

# Step 3: Sum all the square root values
total_sum = np.sum(sqrt_array)

# Print result
print("The sum of the square roots is:", total_sum)
