movie = {"name": "The Holy Grail",
         "year": "1975",
         "price": "9.99"}
# Built-in constructors for creating dictionaries and lists
# converts the keys of a dictionary to a list and sorts them
codes = list(movie.keys())
codes.sort()
for code in movie:
    print(code + " " + movie[code])

# converts a two-dimensional list to a dictionary
countries = [["GB", "United Kingdom"],
             ["NL", "Netherlands"],
             ["DE", "Germany"]]
countries = dict(countries)
print(countries)
