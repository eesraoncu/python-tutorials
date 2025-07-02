# Part 4.4: Definite Iteration
This section covers how to loop over items when the number of repetitions is known in advance. Python’s `for` loop is ideal for definite iteration.

## 🔹 Iterating Over Lists
Instead of manually using an index with a `while` loop:
``` 
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1
``` 
You can use a cleaner `for` loop:
``` 
for number in numbers:
    print(number)
``` 
It’s simpler, more readable, and less error-prone.

## 🔹 The `for` Loop Structure
A `for` loop works like:
``` 
for item in collection:
    # do something with item
``` 
Example:
``` 
for char in "hello":
    print(char)
``` 
## 🔹 Using `range()`
The `range()` function is used to generate sequences of numbers.
- `range(n)` → 0 to n-1
- `range(a, b)` → a to b-1
- `range(a, b, step)` → use a custom step (can be negative)

Examples:
``` 
for i in range(1, 5):
    print(i)  # 1 2 3 4
for i in range(5, 0, -1):
    print(i)  # 5 4 3 2 1
``` 
## 🔹 Converting `range` to a List
You can turn a `range` into a list:
``` 
numbers = list(range(2, 6))  # [2, 3, 4, 5]
``` 
## 🔹 Looping to Find Best or Worst
Use a loop to search for a maximum/minimum:
``` 
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
``` 
## 🔹 Best Practices for Loops
- Use `for` when the number of iterations is known.
- Prefer direct iteration over elements instead of using indices.
- `range()` is useful for numeric loops.
- Keep loop logic clear and simple.

## 📌 Summary
- Use `for` loops for definite iteration.
- Loop through lists, strings, or ranges.
- `range()` helps generate number sequences.
- Clear looping logic makes code easier to read and debug.
