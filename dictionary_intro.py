countries = {"CA": "Canada",
             "US": "United States",
             "MX": "Mexico",
             "india": "delhi",
             "Pakistan": "Lahore",
             "GB": "Great Britain",
             }
# printing the dictionary
print(countries)

# accessing a value
print(countries['CA'])
# sets a value if the key is in the dictionary
countries["Pakistan"] = "Islamabad"
print(countries)
# adds a key/value pair if the key isn’t in the
countries["BAN"] = "Dhaka"
print(countries)
#  checks the key before getting its value
code = "IE"
if code in countries:
    country = countries[code]
    print(country)
else:
    print("There is no country for this code: " + code)
    # get()method of a dictionary object
    # get(key[, default_value])
    # use of the get() method
get_country = countries.get("MX")
print(get_country)
# get country with a default value
get_country = countries.get("GER", "UNKNOWN")
print(get_country)
# syntax for deleting an item
# del dictionary_name[key]
# delete an item
del countries["MX"]
print(countries)
# checks a key before deleting the item
city = "toronto"
if city in countries:
    city = countries[city]
    del countries[city]
    print(city + " was deleted")
else:
    print("There is no city for this city: " + city)
# Two dictionary methods for deleting items
# pop(key[, default_value])
# clear()

# pop() method to delete an item
country = countries.pop("US")
default_country = countries.pop("IE", "Unknown")
print(countries)
# prevents a KeyError from by providing default value
code = "IE"
country_default = countries.pop(code, "Unknown country")
print(country + " was deleted.")

#  clear() method to delete all items
countries.clear()
print(countries)

