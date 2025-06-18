Question1: The following program contains several syntactic errors. Please fix the program.
*Wrong State*                                                   *Correct State*
number = input("Please type in a number: ")                     number = int(input("Please type in a number: "))
  if number>100                                                 if number>100:
    print("The number was greater than one hundred")                 print("The number was greater than one hundred")
    number - 100                                                     number -= 100
    print("Now its value has decreased by one hundred)               print("Now its value has decreased by one hundred")
     print("Its value is now"+ number)                               print("Its value is now"+ str(number))
 print(number + " must be my lucky number!")                      print(str(number) + " must be my lucky number!")
 print("Have a nice day!)                                         print("Have a nice day!")

Question2: Please write a program which asks the user for a word and then prints out the number of characters, if there was more than one typed in.
word=input("Please type in a word: ")
if len(word)>1:
    print("There are",len(word),"letters in the word",word)
    print("Thank you!")
else:
    print("Thank you!")

Question3: Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. Use the Python int function.
number = float(input("Please type in a number: "))
integer_part = int(number)
decimal_part = number - integer_part
print("Integer part:", integer_part)
print("Decimal part:", decimal_part)
