Question1: Please write a program which asks the user for a positive integer number. The program then prints out a list of multiplication operations until both operands reach the number given by the user.
number=int(input("Please type in a number:"))
for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(i,"x",j,"=",i * j)

Question2: Please write a program which asks the user to type in a sentence. The program then prints out the first letter of each word in the sentence, each letter on a separate line.
sentence = input("Please type in a sentence: ")
words = sentence.split()
for word in words:
    if word:
        print(word[0])

Question3: Please write a program which asks the user to type in an integer number. If the user types in a number equal to or below 0, the execution ends. Otherwise the program prints out the factorial of the number.
number=int(input("Please type in a number:"))
if number<=0:
  print("Thanks and bye!")
else:
  fact = 1
  for i in range(1, number + 1):
      fact *= i
  print("The factorial of the number", number, "is", fact)

Question4: Please write a program which asks the user to type in a number. The program then prints out all the positive integer values from 1 up to the number. However, the order of the numbers is changed so that each pair or numbers is flipped. That is, 2 comes before 1, 4 before 3 and so forth.
number = int(input("Please type in a number: "))
i = 1
while i <= number:
    if i + 1 <= number:
        print(i + 1)
        print(i)
        i += 2
    else:
        print(i)
        i += 1

Question5: Please write a program which asks the user to type in a number. The program then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range.
number = int(input("Please type in a number: "))
start = 1
end = number
while start <= end:
    print(start)
    start += 1
    if start <= end:
        print(end)
        end -= 1
