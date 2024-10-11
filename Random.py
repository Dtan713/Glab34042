import random

# Example 1: Generate Random Floats
print("Random float between 0.0 and 1.0:")
print(random.random())

# Example 2: Generate Random Integers
print("\nRandom integers between 1 and 100:")
print(random.randint(1, 100))
print(random.randint(1, 100))

# Example 3: Generate Random Numbers Within Range
print("\nRandom numbers within a specified range:")
print(random.randrange(1, 10))  # Random number between 1 and 9
print(random.randrange(1, 10, 2))  # Random odd number between 1 and 9
print(random.randrange(0, 101, 10))  # Random number in multiples of 10 from 0 to 100

# Example 4: Select Random Elements
print("\nRandomly selected elements from a sequence:")
print(random.choice('computer'))  # Random character from the string
print(random.choice([12, 23, 45, 67, 65, 43]))  # Random integer from the list
print(random.choice((12, 23, 45, 67, 65, 43)))  # Random integer from the tuple

# Example 5: Select Random Items from Data Set
# Example 5.1: Select multiple items from a list without repetition
print("\nRandom sample of 3 items from the list:")
aList = [20, 40, 80, 100, 120]
sampled_list = random.sample(aList, 3)
print(sampled_list)

# Example 5.2: Generate the sampled list of random integers
print("\nSampled list of 5 unique random integers from 0 to 99:")
num_list = random.sample(range(100), 5)
print(num_list)
