# Part 4.5: Print Statement Formatting
This section teaches you how to control how output is printed using various techniques.
## 🔹 String Concatenation with `+`
```
name = "Mark"
age = 37
print("Hi " + name + " your age is " + str(age) + " years")
```
Works only with strings, so you need `str()` to convert non-string types. 

## 🔹 Separate Print Arguments
```
print("Hi", name, "you are", age, "years")
```
Python inserts spaces automatically between arguments.  
You can customize this using `sep`:
```
print("Hi", name, age, sep="_")
```
## 🔹 Controlling Endings
By default, `print()` appends a newline `(\n)`.  
Use `end=""` to prevent it:
```
print("Hi ", end="")
print("there!")
```
Result: `Hi there!` 

## 🔹 F-strings (Formatted String Literals)
```
name = "Erkki"
age = 39
print(f"Hi {name}, you are {age} years old")
```
The cleanest and most modern approach.  
Advanced formatting with f-strings:
```
number = 1/3
print(f"The number is {number:.2f}")  # → 0.33
```
`.2f` formats a float with two decimal places.

## 🔹 Field Width and Alignment
```
names = ["Steve", "Jean", "Katherine", "Paul"]
for name in names:
    print(f"{name:15} centre {name:>15}")
```
Reserves a 15-character field.  
- `{name:15}` is left-aligned (default).
- `{name:>15}` is right-aligned.
  
## 🔹 F-strings Aren’t Just for Print
You can assign formatted strings to variables:
```
greeting = f"Hi {name}, you are {age}"
print(greeting + f", and live in {city}")
```
– Works anywhere strings are used. 

## 📌 Summary
- Three main ways to format output: `+`, comma-separated `print()`, and f-strings.
- Use `sep` and `end` to fine-tune spacing and line breaks.
- F-strings provide flexible formatting—number precision, alignment—directly inside string literals.
- Ideal for clean, readable, and concise output formatting.
