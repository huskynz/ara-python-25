# Print List

FruitList = ['Apple', 'Banana' ,'Plum']


UserFruit = input("Please enter the name of a fruit: ").strip().capitalize()

FruitList.insert(0,UserFruit)

print(f"Item {1}: {FruitList[0]}")
print(f"Item {2}: {FruitList[1]}")
print(f"Item {3}: {FruitList[2]}")
print(f"Item {4}: {FruitList[3]}")