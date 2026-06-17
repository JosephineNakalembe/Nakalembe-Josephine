names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(names[1])
names[0] = "Josephine"
print(names)
names.append("Frank")
print(names)
names.insert(2, "Bathel")
print(names)
names.pop(3)
print(names)
print(names[-1])
new_list = ["one", "two", "three", "four", "five", "six", "seven"]
print(new_list[2:5])
countries = ["Uganda", "Kenya", "Tanzania"]
countries_copy = countries.copy()
print(countries_copy)
for country in countries:
    print(country)
animals = ["zebra", "lion", "elephant", "giraffe", "antelope"]
print(sorted(animals))
print(sorted(animals, reverse=True))
for animal in animals:
    if "a" in animal:
        print(animal)
first_names = ["Alice", "Bob"]
second_names = ["Smith", "Johnson"]
full_names = first_names + second_names
print(full_names)
