#**📝 Part 1.2 – Getting Information from the User**
In this section, we learn how to get input from the user during program execution.
This allows us to make our programs interactive and dynamic.

###🔍 **The input() Function**
The input() function waits for the user to type something and press Enter.

It returns the input as a string.

✅ **Example**
name = input("Enter your name: ")
print("Hello,", name)

🧠 **Notes**
The prompt message (inside input()) is optional but helps the user know what to type.

Since input() returns a string, you may need to convert it to other types (like int or float) when needed.

🔄 **Type Conversion Example**
age = input("Enter your age: ")
age = int(age)  # Convert the input string to an integer
print("You are", age, "years old.")

📝 **Practice Task**
Create a Python file called user_input.py.

Ask the user for their name and age.

Print a message greeting them and telling their age.

✅ **What's Next?**
Next, we'll learn about variables and how to store data in them.
