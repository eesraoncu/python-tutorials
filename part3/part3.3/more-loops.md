# Part 3.3: More Loops

This section deepens the understanding of loop structures in Python by exploring `while` loops, nested loops, and loop control mechanisms like `break` and `continue`.

## 🌀 While Loops

The `while` loop repeats a block of code as long as a condition remains `True`.
```
number = 1
while number < 5:
    print(number)
    number += 1
```
- Be careful of infinite loops! Ensure the condition will eventually become False.

## 🔁 Loop Control: break and continue
`break`
Used to exit a loop prematurely.
```
while True:
    number = int(input("Give a number: "))
    if number == 0:
        break
    print(number)
continue
```
Skips the rest of the loop block and goes to the next iteration.
```
for i in range(5):
    if i == 2:
        continue
    print(i)
```
## 🔂 Nested Loops
Loops can be nested inside each other.
```
for i in range(3):
    for j in range(2):
        print(f"{i}, {j}")
```
Useful in:  
- Grid-based problems
- Comparing elements in lists
- Generating combinations

## 🧮 Accumulating with Loops
Example: summing user input values
```
total = 0
while True:
    num = int(input("Number: "))
    if num == 0:
        break
    total += num
print("Sum:", total)
```
## 📌 Summary
- `while` loops are used when the number of iterations is not known in advance.
- `break` exits a loop immediately, while `continue` skips the current iteration.
- Nested loops are powerful for working with multi-dimensional data.

Carefully controlling loop conditions avoids infinite loops.

Loops are essential tools for building interactive programs and handling repetitive tasks.

