# Part 1.5: Conditional Statements

Conditional statements are used to control the flow of a program by making decisions based on certain conditions.

## `if` Statement

The basic conditional structure:  
```
if condition:
    # code block to run if condition is True
```
- The condition must evaluate to True or False.  
- Indentation defines the block of code inside the if.  
Example:
```
age = 20
if age >= 18:
    print("You are an adult")
```
## else Clause
Provides an alternative block if the condition is not met.
```
if condition:
    # if block
else:
    # else block
```
Example:
```
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")
```
## elif (Else If) Clause
Allows checking multiple conditions in sequence.
```
if condition1:
    # block 1
elif condition2:
    # block 2
else:
    # fallback block
```
- Python evaluates conditions top to bottom.
- Only the first True condition’s block will execute.
Example:
```
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C or below")
```
## Logical Operators
You can combine multiple conditions using logical operators:
### and – All conditions must be true
```
if age > 12 and age < 18:
    print("Teenager")
```
### or – At least one condition must be true
```
if age < 5 or age > 65:
    print("Eligible for discount")
```
### not – Reverses the condition
```
if not is_logged_in:
    print("Please log in")
```
## Nesting Conditions
You can nest if statements inside other if blocks.
```
if score >= 50:
    if score >= 90:
        print("Excellent")
    else:
        print("Passed")
```
## Common Pitfalls
- Indentation is critical. Each block must be consistently indented.
- Avoid writing if x == True:; instead, write if x:
- Use elif instead of multiple if statements when checking mutually exclusive conditions.

## Summary
- Use if to perform actions based on conditions.
- Add else and elif for more complex decision-making.
- Combine conditions using and, or, not.
- Structure your code with consistent indentation.
