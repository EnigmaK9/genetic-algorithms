import random

strings = ["string1", "string2", "string3", "string4", "string5", "string6", "string7", "string8", "string9", "string10"]
probabilities = [0.1, 0.2, 0.05, 0.15, 0.11, 0.07, 0.04, 0.00, 0.12, 0.16]

# Create a list of cumulative probabilities
cumulative_probabilities = []
cumulative_probability = 0
for probability in probabilities:
    cumulative_probability += probability
    cumulative_probabilities.append(cumulative_probability)

# Spin the wheel 1000 times
selections = [0] * len(strings)
for _ in range(1000):
    r = random.random() # Generates a random float between 0 and 1
    for i, cumulative_probability in enumerate(cumulative_probabilities):
        if r < cumulative_probability:
            selections[i] += 1
            break

# Print the number of selections for each string
for string, selection in zip(strings, selections):
    print(f"{string}: {selection}")

