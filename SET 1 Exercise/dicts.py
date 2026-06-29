Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(Shoes["size"])
Shoes["brand"] = "Adidas"
print(Shoes)
Shoes["type"] = "sneakers"
print(Shoes)
print(list(Shoes.keys()))
print(list(Shoes.values()))
print("size" in Shoes)
for key, value in Shoes.items():
    print(key, value)
Shoes.pop("color")
print(Shoes)
Shoes.clear()
print(Shoes)
myDict = {"name": "Josephine", "age": 22}
copyDict = myDict.copy()
print(copyDict)
family = {
    "child1": {"name": "Alice", "age": 5},
    "child2": {"name": "Bob", "age": 7}
}
print(family)
