# Part 2.4: Simple Loops

## 🎯 Learning objectives
- Understand the concept of loops
- Use `while` loops to repeat actions
- Control loop execution with conditions

## 🔹 What is a loop?

- A loop repeats a block of code multiple times.
- Useful when you want to perform repetitive tasks without writing the same code again.

## 🔹 The `while` loop syntax

```
while condition:
    # code to repeat
```
- The code inside the loop runs as long as the condition is True.
- When the condition becomes False, the loop ends.

### 🔹 Example: Counting from 0 to 4
```
i = 0
while i < 5:
    print(i)
    i = i + 1
```
- The loop prints numbers 0, 1, 2, 3, 4.
- Variable i is incremented inside the loop to eventually stop it.

## 🔹 Infinite loops
If the condition never becomes False, the loop runs forever.
Example of infinite loop:
```
while True:
    print("This loop never ends!")
```
To avoid infinite loops, make sure the loop condition eventually becomes False.

## 🔹 Loop with user input
Example: Ask the user repeatedly until they type "exit":
```
command = ""
while command != "exit":
    command = input("Type something (or 'exit' to quit): ")
    print("You typed:", command)
```
## 🔹 Common loop mistakes
- Forgetting to update variables that affect the condition leads to infinite loops.
- Make sure variables used in the condition are updated inside the loop.

## ✅ Summary
- Use while loops to repeat code based on a condition.
- Always ensure the loop condition can become False to stop the loop.
- Loops simplify repetitive tasks.
- Be cautious to avoid infinite loops.
