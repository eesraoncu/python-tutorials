# Part 5.1: More Lists
This section introduces additional list operations and concepts beyond the basics.
## 🔹 Modifying Lists
Lists can be modified after creation.
Assigning to an index changes the element at that position:
```
numbers = [1, 2, 3]
numbers[0] = 100
print(numbers)  # [100, 2, 3]
```
## 🔹 Adding Elements
Use `append()` to add an element at the end:
```
numbers.append(4)
```
Use `insert(index, element)` to add at a specific position:
```
numbers.insert(1, 50)
```
## 🔹 Removing Elements
Use `remove(element)` to remove first occurrence of an element.  
Use `pop()` to remove last element or `pop(index)` to remove element at index.

## 🔹 Finding Elements
Use `index(element)` to find the index of first occurrence.
Use `in` keyword to check membership:
```
if 3 in numbers:
    print("Found 3")
```
## 🔹 List Length
Use `len(list)` to get the number of elements.

## 🔹 Looping Over Lists
Loop using `for element in list`:
```
for number in numbers:
    print(number)
```
## 🔹 List Slicing
Use slicing `list[start:end]` to get a sublist.  
Omitting start or end uses defaults (start=0, end=len(list)).

## 🔹 List Comprehensions (Brief Intro)
Create new lists using expressions:
```
squares = [x*x for x in range(5)]
```
## 📌 Summary
- Lists are mutable and flexible.
- Modify, add, remove, find elements easily.
- Use loops and slicing for processing.
- List comprehensions provide concise syntax to create new lists.
