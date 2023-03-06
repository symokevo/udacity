cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
print("Done!")

# using range() in python
for i in range(3):
    print("Hello!")

# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
    print(capitalized_cities)

# Another way to modify cities
for index in range(len(cities)):
    cities[index] = cities[index].title()
    print(cities)
    
# Here's an example of a for loop in Python that will print out every whole number that is a multiple of 5 and less than or equal to 30:
for i in range(5, 31, 5):
    print(i)
