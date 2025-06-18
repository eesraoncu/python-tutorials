# Part 2.1: Programming Terminology

This section introduces key programming concepts and terminology that are essential for understanding how Python (and programming in general) works.

## **Expressions and Statements**

- **Expression**: A piece of code that produces a value.
  - Example: `3 + 4`, `len("hello")`, `x * 2`
- **Statement**: A complete instruction that performs an action.
  - Example: `print("Hi")`, `x = 5`  
Every expression can be used in a statement, but not every statement is an expression.

## **Functions and Function Calls**

- A **function** is a reusable piece of code that performs a specific task.
- Functions can be built-in (e.g., `print`, `len`) or user-defined.
- **Calling a function** means using it to perform its action, usually with parentheses:
  - Example: `print("Hello!")` or `len("word")`

## **Parameters and Arguments**

- **Parameter**: A variable listed in a function definition.
- **Argument**: The actual value passed to the function when calling it.

Example:
```
def greet(name):  # 'name' is a parameter
    print("Hello", name)
greet("Alice")    # "Alice" is the argument
```

## Return Values
Some functions return a result, which can be stored or used.  
Example: length = len("hello")  
Others (like print()) perform an action but return nothing meaningful (technically None in Python).

## Side Effects
Side effect: When a function does something visible like printing or changing a variable, rather than returning a value.  
Example: print("Hi") has a side effect (producing output).

## Built-in Functions
Python provides many built-in functions, such as:  
`print()`  
`len()`  
`type()`  
`int()`, `float()`, `str()`  
These can be used directly without needing to define them first.

## Naming and Variables
Variable names should describe the data they hold.
Follow standard naming conventions:  
- Use lowercase letters and underscores: `total_score`, `user_name`  
- Avoid using reserved keywords like `if`, `for`, `print`  

## Summary
- Expressions produce values; statements do actions.  
- Functions are reusable blocks of code.  
- Arguments are inputs; parameters are placeholders.  
- Functions may return values or cause side effects.  
- Good naming makes your code more readable and understandable.
