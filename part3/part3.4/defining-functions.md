# Part 3.4: Defining Functions

This section introduces how to define and use functions in Python, highlighting their structure, parameters, return values, and basic usage.

## 🛠 What is a Function?

- A **function** is a named block of reusable code designed to perform a specific task.
- Functions help **avoid repetition** and make programs easier to read and maintain.
- Python has many built-in functions (e.g., `print()`, `input()`, `len()`), and you can define your own.

## 🔹 Defining a Function

Syntax:
```
def function_name(parameters):
    # function body
    # optional return statement
```
- Use the `def` keyword, followed by the function name and parentheses.
- Parameters (also called arguments) are optional.
- The function body is indented under the definition.  
Example:
```
def greet():
    print("Hello!")
```
## 🔹 Calling a Function
To run the function, write its name followed by parentheses:
```
greet()
```
## 🔹 Parameters and Arguments
- Functions can accept input values called parameters.
- When calling the function, you provide arguments for these parameters.  
Example:
```
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
```
## 🔹 Return Values
- Functions can return a value using the `return` statement.
- Returning values lets you use the result elsewhere in your program.
Example:
```
def add(x, y):
    return x + y
result = add(3, 4)
print(result)  # Output: 7
```
## 🔹 Functions without Return
- If a function doesn't have a `return` statement, it returns `None` by default
- Functions can perform actions (like printing) without returning a value.

## 📌 Summary
- Functions are building blocks of code that improve readability and reusability.
- Use `def` to define functions with optional parameters.
- Call functions by their name with parentheses, passing arguments if needed.
- Use `return` to send back results from functions.
