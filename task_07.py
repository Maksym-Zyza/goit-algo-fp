import numpy as np
import matplotlib.pyplot as plt

# Number of rolls
num_rolls = 100_000

# Simulate rolling two dice
dice1 = np.random.randint(1, 7, num_rolls)
dice2 = np.random.randint(1, 7, num_rolls)

# Calculate the sums of the two dice
sums = dice1 + dice2
sum_counts = {i: 0 for i in range(2, 13)}
for s in sums:
    sum_counts[s] += 1

# Calculate probabilities
probabilities = {key: count / num_rolls for key, count in sum_counts.items()}

# Print the probability table
print("Sum  | Probability")
print("--------------------")
for sum_value in range(2, 13):
    print(f"{sum_value}    | {probabilities[sum_value] * 100:.2f}%")

# Plotting the probabilities
sum_values = list(probabilities.keys())
probability_values = list(probabilities.values())

plt.bar(sum_values, probability_values, color='blue', alpha=0.7, label='Monte Carlo Method')
plt.xlabel('Sum')
plt.ylabel('Probability')
plt.title('Probability of Sums when Rolling Two Dice (Monte Carlo Method)')
plt.xticks(sum_values)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
