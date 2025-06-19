# Part 2.3: Combining conditions

## 🎯 Learning objectives
- Use the logical operators **and**, **or**, and **not** in conditions.
- Write nested conditional statements.

## 🔹 Logical operators

You can combine boolean expressions:

- **and**: All conditions must be true.
- **or**: At least one condition must be true.
- **not**: Negates a condition.

### Examples
```
number = int(input("Please type in a number: "))
if number >= 5 and number <= 8:
    print("The number is between 5 and 8")
if number < 5 or number > 8:
    print("The number is not within the range of 5 to 8")
if not (number >= 5 and number <= 8):
    print("The number is not within the range of 5 to 8")
```
### Boolean truth table

a      b      a and b   a or b
False  False  False     False
True   False  False     True
False  True   False     True
True   True   True      True
and not simply reverses True ↔ False. 

## 🔹 Simplified range check
Python allows a mathematical shorthand for range inclusion:
```
if  a <= x <= b:
    # same as x >= a and x <= b
```
This is equivalent to the longer form with and, just more concise. 

## 🔹 Combining and chaining conditions
To find the greatest of four numbers:
```
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
n4 = int(input("Number 4: "))
if n1 > n2 and n1 > n3 and n1 > n4:
    greatest = n1
elif n2 > n3 and n2 > n4:
    greatest = n2
elif n3 > n4:
    greatest = n3
else:
    greatest = n4
print(f"{greatest} is the greatest of the numbers.")
```
The and ensures all comparisons are true before selecting the greatest. 

## 🔹 Nested conditionals
Example of nested if/else:
```
number = int(input("Please type in a number: "))
if number > 0:
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative or zero")
```
- Indentation matters: controls which else belongs to which if.
- Same behavior can be achieved with combined conditions too. 

## ✅ Summary
- `and`: requires all conditions to be true.
- `or`: true if any condition is true.
- `not`: reverses the truth value.
- Python supports chained comparisons (a <= x <= b).
- Nested if ensures structured decision logic.
- Correct indentation is essential for nesting.
