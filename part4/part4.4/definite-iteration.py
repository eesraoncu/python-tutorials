Question1: Please write a program which asks the user to type in a string. The program then prints each input character on a separate line. After each character there should be a star (*) printed on its own line.
user_input = input("Please type in a string: ")
for char in user_input:
    print(char)
    print("*")

Question2: Please write a program which asks the user for a positive integer N. The program then prints out all numbers between -N and N inclusive, but leaves out the number 0. Each number should be printed on a separate line.
n = int(input("Please type in a positive integer: "))
for i in range(-n, n + 1):
    if i != 0:
        print(i)

Question3: Please write a function named list_of_stars, which takes a list of integers as its argument. The function should print out lines of star characters. The numbers in the list specify how many stars each line should contain.
def list_of_stars(numbers):
    for number in numbers:
        print("*" * number)
list_of_stars([3, 7, 1, 1, 2])

Question4: Please write a function named anagrams, which takes two strings as arguments. The function returns True if the strings are anagrams of each other. Two words are anagrams if they contain exactly the same characters.
def anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
print(anagrams("tame", "meta"))

Question5: Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome. Palindromes are words which are spelled exactly the same backwards and forwards.
def palindromes(word):
    return word == word[::-1]
while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

Question6: Please write a function named sum_of_positives, which takes a list of integers as its argument. The function returns the sum of the positive values in the list.
def sum_of_positives(numbers):
    return sum(num for num in numbers if num > 0)
my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)

Question7: Please write a function named even_numbers, which takes a list of integers as an argument. The function returns a new list containing the even numbers from the original list.
def even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)

Question8: Please write a function named list_sum which takes two lists of integers as arguments. The function returns a new list which contains the sums of the items at each index in the two original lists. You may assume both lists have the same number of items.
def list_sum(list1, list2):
    return [x + y for x, y in zip(list1, list2)]
a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b)) 

Question9: Please write a function named distinct_numbers, which takes a list of integers as its argument. The function returns a new list containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.
def distinct_numbers(numbers):
    return sorted(set(numbers))
my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list))

Question10: Please write a function named length_of_longest, which takes a list of strings as its argument. The function returns the length of the longest string.
def length_of_longest(strings):
    return max(len(s) for s in strings)
my_list = ["first", "second", "fourth", "eleventh"]
result = length_of_longest(my_list)
print(result) 

Question11: Please write a function named shortest, which takes a list of strings as its argument. The function returns whichever of the strings is the shortest. If more than one are equally short, the function can return any of the shortest strings (there will be no such situation in the tests). You may assume there will be no empty strings in the list.
def shortest(strings):
    return min(strings, key=len)
my_list = ["first", "second", "fourth", "eleventh"]
result = shortest(my_list)
print(result) 

Question12: Please write a function named all_the_longest, which takes a list of strings as its argument. The function should return a new list containing the longest string in the original list. If more than one are equally long, the function should return all of the longest strings.
def all_the_longest(strings):
    max_length = max(len(s) for s in strings)
    return [s for s in strings if len(s) == max_length]
my_list = ["first", "second", "fourth", "eleventh"]
result = all_the_longest(my_list)
print(result)  # ['eleventh']
