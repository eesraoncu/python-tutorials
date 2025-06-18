# 🧠 Part 1.3 – More About Variables

## 🎯 Learning Objectives
- Use variables in different contexts  
- Understand what types of data can be stored  
- Distinguish between strings, integers, and floats  

## 1. What Are Variables?
Variables store information that is needed later in a program.
They are created using the `=` operator:

```
name = "Ada"
age = 25
```
Variables can be:  
- Constants  
- Based on user input  
- Expressions  

## 2. Hard‑Coding & Concatenation
```
given_name = "Paul"
family_name = "Python"
name = given_name + " " + family_name
print(name)
```
You can combine (concatenate) strings with the + operator.

## 3. Changing Variable Values
Variables can be reassigned:
```
word = input("Please type in a word: ")
word = input("And another word: ")
word = "third"
print(word)
```

Variables can also be updated based on their own value:
```
word = input("Type a word: ")
word = word + "!!!"
print(word)
```

## 4. Naming Conventions
- Use meaningful, lowercase names with underscores: first_name, user_age  
- Must start with a letter  
- Can include letters, numbers, and underscores  
- Python is case-sensitive: name, Name, and NAME are different variables  

## 5. Data Types
### Integers  
Whole numbers like -15, 0, 42:
```
age = 24
print(age)
```
Type Matters!
```
number1 = 100          # integer  
number2 = "100"        # string  
print(number1 + number1)  # 200 (addition)  
print(number2 + number2)  # "100100" (concatenation)
```

## 6. Mixing Types in Print Statements
This will cause an error:
```
result = 10
print("The result is " + result)  # ❌ TypeError
```
✅ Correct Ways:  
1. Using str() conversion:
print("The result is " + str(result))  
2. Using a comma:    
print("The result is", result)

## 7. F‑Strings (Python 3.6+)
F‑strings allow you to embed variables directly into strings:
```
result = 10 * 25
print(f"The result is {result}")
```

## 8. Floating‑Point Numbers (Floats)
Decimals like 2.5, -1.25, or 3.62:
```
mean = (2.5 + -1.25 + 3.62) / 3
print(f"Mean: {mean}")
```

## ✅ Summary
- Variables can store strings, integers, and floats.  
- You can reassign and manipulate them.  
- Data types affect operations (e.g., string vs integer addition).  
- Use meaningful names and proper formatting when printing values.  
- F‑strings offer a clean, modern way to format output.
