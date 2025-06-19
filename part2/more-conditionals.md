# Part 2.2: More Conditionals

## 🎯 Learning objectives
- Create multiple branches in conditional statements using `elif` and `else`  
- Understand how only one branch in an `if-elif-else` chain is executed  
- Use the modulo operator `%` in conditional expressions

## 🔹 `if` and `else`

- `else` provides an alternative when the `if` condition is not met.
- Only one of the two branches (`if` or `else`) is executed.
- `else` must always follow an `if`.

### Example: Negative vs Non-negative
```
number = int(input("Please type in a number: "))
if number < 0:
    print("The number is negative")
else:
    print("The number is positive or zero")
```
### Example: Even or Odd
```
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
```
### Example: Password Check
```
correct = "kittycat"
password = input("Please type in the password: ")
if password == correct:
    print("Welcome")
else:
    print("No admittance")
```
In all of these examples, exactly one branch is executed.  

## 🔹 The `elif` Keyword
- `elif` stands for “else if”.
- It allows checking multiple conditions in sequence.
- Only the first true condition's block is executed.
- You can have multiple elif clauses.
- `else` is optional and can be added at the end as a fallback.

### Example: Football Match Outcome
```
goals_home = int(input("Home goals scored: "))
goals_away = int(input("Away goals scored: "))
if goals_home > goals_away:
    print("The home team won!")
elif goals_away > goals_home:
    print("The away team won!")
else:
    print("It's a tie!")
```
### Example: Holiday Calendar
```
print("Holiday calendar")
date = input("What is the date today? ")
if date == "Dec 26":
    print("It's Boxing Day")
elif date == "Dec 31":
    print("It's Hogmanay")
elif date == "Jan 1":
    print("It's New Year's Day")
print("Thanks and bye.")
```
In this example, there’s no else clause, so if none of the conditions match, nothing is printed from the if-elif structure.

## ✅ Summary
- Use if to check a condition.  
- Use elif to check additional conditions, only if previous ones failed.  
- Use else to define a fallback action when no previous conditions were true.  
- Only one block in an if-elif-else structure is executed.  
- The modulo operator % is useful for checking even/odd or divisibility.
