Question1: Please write a program which asks the user for a string and an amount. The program then prints out the string as many times as specified by the amount. The printout should all be on one line, with no extra spaces or symbols added.
word=input("Please type in a string:")
amount=int(input("Please type in an amount:"))
print(amount*word)

Question2: Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".
word1=input("Please type in string 1: ")
word2=input("Please type in string 2: ")
if len(word1) > len(word2):
  print(word1,"is longer.")
elif len(word2) > len(word1):
  print(word2,"is longer.")
else:
  
  print("The strings are equally long.")

Question3: Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line.
word=input("Please type in a string:")
index = len(word) - 1
while index >= 0:
    print(word[index])
    index -= 1

Question4: Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not.
word=input("Please type in a string:")
if word[1]==word[len(word)-2]:
  print("The second and the second to last characters are",word[1])
else:
  print("The second and the second to last characters are different.")

Question5: Please write a program which prints out a line of hash characters, the width of which is chosen by the user.
width=int(input("Width:"))
print("#" * width)

Question6: Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.
width=int(input("Width:"))
height=int(input("Height:"))
row=0
while row < height:
  print("#" * width)
  row+=1

Question7: Please write a program which asks the user for strings using a loop. The program prints out each string underlined as shown in the examples below. The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.
string=input("Please type in a string:")
while len(string)>0:
  print(string)
  print("-" * len(string))
  break

Question8: Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.
word=input("Please type in a string:")
while len(word)>0:
  print("*" * (20 - len(word)) + word)
  break

Question9: Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame. If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.
word=input("Please type in a string:")
print("*" * 30)
print("*"+int((28-len(word))/2) * " " + word + int((28-len(word))/2) * " " + "*")
print("*" * 30)

Question10: Please write a program which asks the user to type in a string. The program then prints out all the substrings which begin with the first character, from the shortest to the longest. 
word=input("Please type in a string:")
index=1
while index<=len(word):
  print(word[:index])
  index+=1

Question11: Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character, from the shortest to the longest.
word = input("Please type in a string: ")
index = len(word) - 1 
while index >= 0:
    print(word[index:])
    index -= 1

Question12: Please write a program which asks the user to input a string. The program then prints out different messages if the string contains any of the vowels a, e or o. You may assume the input will be in lowercase entirely.
text = input("Please type in a string: ")
if "a" in text:
    print("a found")
else:
    print("a not found")
if "e" in text:
    print("e found")
else:
    print("e not found")
if "o" in text:
    print("o found")
else:
    print("o not found")

Question13: Please write a program which asks the user to type in a string and a single character. The program then prints the first three character slice which begins with the character specified by the user. You may assume the input string is at least three characters long. The program must print out three characters, or else nothing. Pay special attention to when there are less than two characters left in the string after the first occurrence of the character looked for. In that case nothing should be printed out, and there should not be any indexing errors when executing the program.
word = input("Please type in a word: ")
char = input("Please type in a character: ")
i = 0
while i <= len(word) - 3:
    if word[i] == char:
        print(word[i:i+3])
        break
    i += 1

Question14: Please make an extended version of the previous program, which prints out all the substrings which are at least three characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long.
word = input("Please type in a word: ")
char = input("Please type in a character: ")
i = 0
while i < len(word):
    if word[i] == char:
        j = i + 3
        while j <= len(word):
            print(word[i:j])
            j += 1
    i += 1

Question15: Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.
text = input("Please type in a string: ")
sub = input("Please type in a substring: ")
count = 0 
index = 0 
while index <= len(text) - len(sub):
    if text[index:index+len(sub)] == sub:
        count += 1
        if count == 2:
            print("The second occurrence of the substring is at index", index)
            break
        index += len(sub) 
    else:
        index += 1
if count < 2:
    print("The substring does not occur twice in the string.")
