beverages = set(("tea", "coffee", "juice"))
print(beverages)
beverages.update(["water", "milk"])
print(beverages)
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in mySet)
mySet.remove("kettle")
print(mySet)
for item in mySet:
    print(item)
mySet2 = {"pen", "book", "bag", "chair"}
myList = ["table", "lamp"]
mySet2.update(myList)
print(mySet2)
ages = {20, 25, 30}
names = {"Alice", "Bob"}
joined = ages.union(names)
print(joined)
