# Part 4.6: Strings and Lists
This section covers common operations and good practices when working with strings and lists in Python.
## 🔸 Strings Are Immutable
Strings cannot be changed in-place.  
You cannot assign to an index in a string:
```
s = "hello"
s[0] = "H"  # ❌ Error
```
Instead, you must create a new string:
```
s = s.replace("h", "H")
```
## 🔸 Common String and List Methods
`.count(x)` returns how many times x appears:
```
"banana".count("an")  # → 2
[1, 2, 1].count(1)     # → 2
```
`.replace(old, new)` replaces all occurrences:
```
"hi hi".replace("hi", "hello")  # → 'hello hello'
```
## 🔸 Global vs Local Variables
- Avoid using global variables inside functions.
- Always pass necessary data via parameters and return values.
Example of bad practice:
```
my_list = [1, 2, 3]
def modify():
    my_list.append(4)  # Not recommended
```
Better:
```
def modify(lst):
    lst.append(4)
    return lst
```
## 🔸 Avoid Hidden Dependencies
Define main code inside:
```
if __name__ == "__main__":
    ...
```
- Keep testing and runtime behavior separate.
- TMC (test system) runs only the code inside functions, not the `main`.
## 🔸 Functional Program Structure
Split your program into small, testable helper functions:
Input:
```
def input_list():
    ...
    return list_of_numbers
```
Processing:
```
def average(lst):
    ...
    return result
```
Output:
```
def print_result(avg):
    print(f"The average is {avg}")
```
Main:
```
def main():
    nums = input_list()
    avg = average(nums)
    print_result(avg)
```
## 🧩 Summary
- Strings are immutable; any operation creates a new one.
- Use `.count()` and `.replace()` for both strings and lists.
- Avoid global variables. Use parameters and return values.
- Write modular code: break large tasks into helper functions.
- Use `if __name__ == "__main__":` to separate execution from testing logic.
