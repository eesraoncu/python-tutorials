# Part 3.1: Loops with Conditions

## 🎯 Learning Objectives
- Combine loops with conditional statements
- Use `if`, `else`, and `while` together for complex control flows
- Create programs that react differently based on user input during loops

## 🔁 Conditional Logic Inside Loops

### Example: Only print even numbers

```
number = 0
while number < 10:
    number += 1
    if number % 2 != 0:
        continue
    print(number)
```
- `continue` skips to the next loop iteration
- Only even numbers are printed: 2, 4, 6, 8, 10

## ❌ Skipping values with `continue`
- Use continue to skip the rest of the loop block and go to the next iteration.
- Useful when a condition should ignore certain input values.

## ✅ Exiting loops early with `break`
Example: Exit on specific input
```
while True:
    word = input("Please type in a word: ")
    if word == "end":
        break
    print(word)
```
- This loop continues until the user types "end"

## 🔄 Counting and Conditions Combined
Example: Count positive numbers
```
count = 0
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    if number > 0:
        count += 1
print("Positive numbers:", count)
```
- Reads numbers from user
- Increments count only when number is positive

## 🧠 Loop Logic Summary
- Loops can be controlled by conditions inside (if, break, continue)
- Complex behaviors emerge when you combine loops and conditions
- Always ensure the loop has a way to exit (break or condition becoming False)
