# Part 4.2: More Functions

This section expands on user-defined functions in Python. It introduces default parameters, return values, helper functions, and how to write cleaner, modular code.

## 🔹 Default Parameter Values

- You can define **default values** for parameters.
- If an argument isn't passed, the default is used.

```
def greet(name="friend"):
    print(f"Hello, {name}!")
```
- Calling `greet()` prints `Hello, friend!`
- Calling `greet("Alice")` prints `Hello, Alice!`

## 🔹 Returning Values
Functions can send results back using `return`.
```
def double(number):
    return number * 2
result = double(5)  # result is 10
```
Once `return` is executed, the function exits immediately.

## 🔹 Functions Calling Functions
You can use one function inside another.
```
def add(a, b):
    return a + b
def square_sum(x, y):
    return add(x, y) ** 2
```
This improves modularity and code reuse.

## 🔹 Keeping Functions Short and Simple
- Each function should do one clear thing.
- Long code should be broken into smaller helper functions.
- This improves readability, testing, and debugging.

## 🔹 Naming Conventions
- Use descriptive names for functions and variables.
- Follow `snake_case` style in Python.
Bad example:
```
def f(x):
    return x * 3
```
Better:
```
def triple(number):
    return number * 3
```
## 🧪 Testing Your Functions
- Use `print()` to test output during development.
- Modular functions are easier to test.

## 📌 Summary
- Functions may have default parameter values.
- Functions can return values and call other functions.
- Clean, modular code is easier to read and maintain.
- Write short, specific functions with good names.
