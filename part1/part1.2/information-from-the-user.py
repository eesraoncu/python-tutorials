Question1: Please write a program which asks for the user's name and then prints it twice, on two consecutive lines.
name=input("Please enter your name: ")
print(name)
print(name)

Question2: Please write a program which asks for the user's name and then prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, another between the two names and a third one at the end of the line.
name=input("Please enter your name: ")
print("!"+name+"!"+name+"!")

Question3: Please write a program which asks for the user's name and address.
given_name=input("Please enter your first name: ")
family_name=input("Please enter your last name: ")
street_address=input("Please enter street address: ")
city_and_postal_code=input("Please enter city and postal code: ")

Question4: Here is a program which should ask for three utterances and print them out.
part1=input("Please enter the first word: ")
part2=input("Please enter the second word: ")
part3=input("Please enter the third word: ")
print(part1+"-"+part2+"-"+part3+"!")

Question5: Please write a program which prints out the following story. The user gives a name and a year, which should be inserted into the printout.
name=input("Please enter a name: ")
year=int(input("Please enter a year: "))
print(name,"is a valiant knight, born in the year",year,". One morning",name,"woke up to an awful racket: a dragon was approaching the village. Only", name,"could save the village's residents.")
