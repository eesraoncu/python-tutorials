# Part 4.3: Lists
This section introduces lists in Python, how to work with them, and how to write functions that manipulate lists.

## 🔹 What is a List?
- A list is an ordered collection of values.
- Lists are mutable, meaning you can change their contents.
- Lists are created using square brackets:
```
numbers = [1, 2, 3, 4]
names = ["Alice", "Bob", "Charlie"]
```
## 🔹 Accessing Elements
Elements are accessed by zero-based index:
```
print(names[0])  # Alice
```
You can also modify elements:
```
names[1] = "Bobby"
```
Use len(list) to get the number of items.

## 🔹 Adding Items
- Use .append(item) to add an item at the end.
- Use .insert(index, item) to add at a specific position.
```
names.append("Diana")
names.insert(1, "Eve")
```
## 🔹 Removing Items
- Use .pop(index) to remove and return an item at a specific index.
- Use .remove(value) to remove the first occurrence of a value.
 ```
removed = names.pop(2)
names.remove("Bobby")
```
Always check if the item exists before removing to avoid errors.

## 🔹 Useful Built-in Functions
- len(list) — number of items.
- sum(list) — sum of numeric items.
- min(list), max(list) — smallest and largest items.
- sorted(list) — returns a new sorted list.
- .sort() — sorts the list in place.

## 🔹 Functions and Lists
You can pass lists as arguments and return lists from functions.
```
def print_list(lst):
    for item in lst:
        print(item)
 ```
Example: a function to find the median of a list.
```
def median(numbers):
    numbers.sort()
    mid = len(numbers) // 2
    return numbers[mid]
```
## 📌 Summary
- Lists hold ordered collections and are mutable.
- Access elements by index, modify, add, and remove items with list methods.
- Use built-in functions to analyze and sort lists.
- Pass lists to and from functions to write modular and reusable code.
