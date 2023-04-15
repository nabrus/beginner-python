# List Compressions - creating lists in a concise way
numbers = [1, 2, 3, 4, 5]

# List compression
numbers_power_2 = [n**2 for n in numbers]

print(numbers_power_2)  # [1, 4, 9, 16, 25]

# Same example using a loop
numbers_power_two = []
for n in numbers:
    numbers_power_two.append(n**2)

print(numbers_power_two)  # [1, 4, 9, 16, 25]

# Same example using `map`
numbers_power_too = list(map(lambda n: n**2, numbers))

print(numbers_power_too)  # [1, 4, 9, 16, 25]
