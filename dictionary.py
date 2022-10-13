populations = {
    "Toronto": "3490000",
    "New York": "4550000",
    "London": "5560000",
    "Paris": "6570000",
    "Lahore": "7560000",
}

for key, value in populations.items():
    print([key, value])
    list_value = []
for key, value in populations.items():
    list_value += [value]
print(list_value)
print(max(list_value))
print(min(list_value))
