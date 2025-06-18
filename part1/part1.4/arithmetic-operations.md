# Part 1.4: Arithmetic Operations

## 🎯 Learning Objectives
- Perform arithmetic operations with variables.  
- Read numeric input from the user.  
- Convert string input to integers or floats.  

## ➕ Arithmetic Operators in Python

Python supports standard arithmetic operators:  
| Operator | Meaning          | Example      | Result |
|----------|------------------|--------------|--------|
| `+`      | Addition          | `3 + 4`      | `7`    |
| `-`      | Subtraction       | `10 - 3`     | `7`    |
| `*`      | Multiplication    | `2 * 5`      | `10`   |
| `/`      | Division (float)  | `8 / 2`      | `4.0`  |
| `//`     | Floor Division    | `9 // 2`     | `4`    |
| `%`      | Modulo (remainder)| `9 % 2`      | `1`    |
| `**`     | Exponentiation    | `2 ** 3`     | `8`    |

> ⚠️ Division with `/` always returns a float, even when divisible (e.g., `4 / 2` returns `2.0`).

## 📌 Order of Operations (Precedence)

Python follows standard mathematical precedence:  
1. Exponentiation `**`  
2. Multiplication `*`, Division `/`, Floor Division `//`, Modulo `%`  
3. Addition `+`, Subtraction `-`  

Use parentheses `()` to control the order:
```
print(2 + 3 * 4)       # 14
print((2 + 3) * 4)     # 20
```

## 🔄 Using Variables in Arithmetic
You can store numbers in variables and use them in operations:
```
x = 10
y = 4
print(x + y)       # 14
print(x * y)       # 40
print(x / y)       # 2.5
```
You can also update variables:
```
x = 3
x = x + 2     # x becomes 5
x = x * 3     # x becomes 15
```

## 🎯 User Input and Type Conversion
input() returns a string, so you must convert it before arithmetic.  
Convert input to integer:
```
x = int(input("Enter a number: "))
print(x * 2)
```
Convert input to float:
```
height = float(input("Enter your height in meters: "))
```
You can also combine input and conversion in a single line:
```
year = int(input("Enter a year: "))
```

## 🧮 Example: BMI Calculation
```
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2)
print("Your BMI is", bmi)
```

## ➕➖ Variable Reuse in Summation Example
You can reuse a variable to store intermediate sums:
```
total = int(input("Enter number: "))
total = total + int(input("Enter another: "))
total = total + int(input("One more: "))
print("Sum:", total)
```

## 📝 Summary
- Use standard arithmetic operators to perform calculations.  
- Always convert user input before performing math.  
- Use int() and float() to cast strings to numbers.  
- Use parentheses to control operation order.  
- % and // are useful for more advanced arithmetic.  
- Practice with different inputs and expressions to get familiar with Python math operations!
