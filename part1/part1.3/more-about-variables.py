Question1: You are given a piece of Python code that prints information about a jobseeker. The output must exactly match the sample provided — including spaces, punctuation, and line breaks. The current code works almost correctly, but it uses commas in print() statements, which adds extra spaces. You are asked to fix the formatting, preferably using f-strings, to ensure the output is identical to the required format.
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000
print(f"my name is {name}, I am {age} years old\n")
print("my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})\n")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

Question2: Complete the program so that it prints the results of addition, subtraction, multiplication, and division between two variables x and y in the exact format shown, and works correctly even if their values change.
x = 27
y = 15
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")

Question3: Please fix this program so that the entire calculation, complete with result, is printed out on a single line. Do not change the number of print commands used.
*Wrong State*                          *Correct State*
print(5)                               print(5,end="")
print(" + ")                           print(" + ",end="")
print(8)                               print(8,end="")
print(" - ")                           print(" - ",end="")
print(4)                               print(4,end="")
print(" = ")                           print(" = ",end="")
print(5 + 8 - 4)                       print(5 + 8 - 4)
