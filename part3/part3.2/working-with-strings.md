# Part 3.2: Working with Strings

## 🧵 Basic string manipulation

In Python, strings are sequences of characters. You can:
- Access characters using indexing
- Iterate over them using loops
- Combine, modify, and analyze them using built-in methods

## 🔢 Indexing and Length

```
text = "hello"
print(text[0])     # h
print(len(text))   # 5
```
- Indexing starts at 0
- `len()` gives the number of characters

## 🔁 Iterating through strings
```
text = "hi"
for character in text:
    print(character)
```
- Loops go through each character one by one

## 🔤 String Methods
Some useful methods:  
- `upper()`: converts to uppercase
- `lower()`: converts to lowercase
- `strip()`: removes surrounding whitespace
- `find(substring)`: finds position of substring (returns -1 if not found)
- `replace(old, new)`: replaces occurrences
- `in`: checks if a substring exists
```
word = "Hello"
print(word.upper())       # HELLO
print("ell" in word)      # True
print(word.find("l"))     # 2
```
## ➕ String Concatenation
```
first = "Hello"
second = "World"
combined = first + " " + second
```
- `+` combines strings
- Use `" "` to include spaces

## 🔍 Substrings and Slicing
```
text = "Python"
print(text[1:4])   # yth
```
- `text[start:end]` gets characters from start to end-1

## 📚 Example Task
Prompt user for a string and print it character by character:
```
text = input("Please type in a string: ")
for character in text:
    print(character)
```
## ⚠️ Remember
- Strings are immutable in Python
- You cannot modify them directly (e.g., text[0] = "H" is invalid)
- Always use string methods or create new strings instead
