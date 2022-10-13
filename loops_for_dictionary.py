numbers = {"1": "One", "2": "Two", "3": "Three",
           "4": "Four", "5": "Five"}
# for loop for the dictionaries
for code in numbers.keys():
    print(code + " " + numbers[code])
print("end of loop on keys\n")

# Another way to get the same result since the default iterator contains keys
for code in numbers:
    print(code + " " + numbers[code])
print("end of loop on dictionary\n")

# Code that unpacks a tuple as it loops through all keys and values
for code, name in numbers.items():
    print(code + " " + name)
print("end of loop through all keys and values\n")

# loops through all values
for number in numbers.values():
    print(number)
