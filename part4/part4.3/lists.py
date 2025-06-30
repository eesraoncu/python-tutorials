Question1: Please write a program which initialises a list with the values [1, 2, 3, 4, 5]. Then the program should ask the user for an index and a new value, replace the value at the given index, and print the list again. This should be looped over until the user gives -1 for the index. You can assume all given index values will fall within your list.
numbers = [1, 2, 3, 4, 5]
while True:
    index = int(input("Index: "))
    if index == -1:
        break
    new_value = int(input("New value: "))
    numbers[index] = new_value
    print(numbers)

Question2: Please write a program which first asks the user for the number of items to be added. Then the program should ask for the given number of values, one by one, and add them to a list in the order they were typed in. Finally, the list is printed out.
items = []
count = int(input("How many items: "))
for i in range(1, count + 1):
    value = int(input("Item",i,": "))
    items.append(value)
print(items)

Question3: Please write a program which asks the user to choose between addition and removal. Depending on the choice, the program adds an item to or removes an item from the end of a list. The item that is added must always be one greater than the last item in the list. The first item to be added must be 1.
my_list = []
print("The list is now",my_list)
while True:
    choice = input("a(d)d, (r)emove or e(x)it: ")
    if choice == "d":
        if my_list:
            next_value = my_list[-1] + 1
        else:
            next_value = 1
        my_list.append(next_value)
        print("The list is now,"my_list)
    elif choice == "r":
        my_list.pop()
        print("The list is now,"my_list)    
    elif choice == "x":
        print("Bye!")
        break
Question4: Please write a program which asks the user for words. If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.
words = []
while True:
    word = input("Word: ")
    if word in words:
        print(f"You typed in",len(words),"different words")
        break
    words.append(word)

Question5: Please write a program which asks the user to type in values and adds them to a list. After each addition, the list is printed out in two different ways:
- in the order the items were added
- ordered from smallest to greatest
The program exits when the user types in 0.
items = []
while True:
    value = int(input("New item: "))
    if value == 0:
        print("Bye!")
        break
    items.append(value)
    print("The list now:", items)
    print("The list in order:", sorted(items))

Question6: Please write a function named length which takes a list as its argument and returns the length of the list.
def lenght_of_array(my_list):
 result=len(my_list)
 print("the lenght is ",result)
lenght_of_array([4,8,9,7,5,6]) 

Question7: Please write a function named mean, which takes a list of integers as an argument. The function returns the arithmetic mean of the values in the list.
def arithmetic_mean(my_list):
    mean=sum(my_list)/len(my_list)
    print("mean value is ",mean)
arithmetic_mean([4,8,9,7,5,6]) 

Question8: Please write a function named range_of_list, which takes a list of integers as an argument. The function returns the difference between the smallest and the largest value in the list.
def range_of_list(my_list):
    range=max(my_list)-min(my_list)
    print("the range is ",range)
range_of_list([4,8,9,7,5,6])
