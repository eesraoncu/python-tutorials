Question1: Please write a function named everything_reversed, which takes a list of strings as its argument. The function returns a new list with all of the items on the original list reversed. Also the order of items should be reversed on the new list.
def everything_reversed(lst):
    lst_copy = lst[:] 
    lst_copy.reverse()
    new_list = []
    for item in lst_copy:
        new_list.append(item[::-1])
    return new_list
my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)

Question2: Please write a function named most_common_character, which takes a string argument. The function returns the character which has the most occurrences within the string. If there are many characters with equally many occurrences, the one which appears first in the string should be returned.
def most_common_character(string):
    counts = {}
    for char in string:
        if char not in counts:
            counts[char] = string.count(char)
    max_count = max(counts.values())
    for char in string:
        if counts[char] == max_count:
            return char
first_string = "abcdbde"
print(most_common_character(first_string))

Question3: Please write a function named no_vowels, which takes a string argument. The function returns a new string, which should be the same as the original but with all vowels removed. You can assume the string will contain only characters from the lowercase English alphabet a...z.
def no_vowels(string):
    vowels = "aeiou"
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    return result
my_string = "this is an example"
print(no_vowels(my_string))

Question4: Please use the isupper method to write a function named no_shouting, which takes a list of strings as an argument. The function returns a new list, containing only those items from the original which do not consist of solely uppercase characters.
def no_shouting(strings):
    result = []
    for s in strings:
        if not s.isupper():
            result.append(s)
    return result
my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
pruned_list = no_shouting(my_list)
print(pruned_list)

Question5: Please write a function named longest_series_of_neighbours, which looks for the longest series of neighbours within the list, and returns its length. For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be [5, 4, 3, 4], with a length of 4.
def longest_series_of_neighbours(numbers):
    if not numbers:
        return 0
    max_length = 1
    current_length = 1
    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i - 1]) == 1:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 1 
    return max_length
my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))

Question6: In this exercise you will write a program for printing out grade statistics for a university course. The program asks the user for results from different students on the course. These include exam points and numbers of exercises completed. The program then prints out statistics based on the results. Exam points are integers between 0 and 20. The number of exercises completed is an integer between 0 and 100. The program keeps asking for input until the user types in an empty line. You may assume all lines contain valid input, which means that there are two integers on each line, or the line is empty.
def convert_exercises_to_points(exercises):
    return exercises // 10
def calculate_grade(exam_points, exercise_points):
    if exam_points < 10:
        return 0
    total_points = exam_points + exercise_points
    if total_points <= 14:
        return 0
    elif total_points <= 17:
        return 1
    elif total_points <= 20:
        return 2
    elif total_points <= 23:
        return 3
    elif total_points <= 27:
        return 4
    else:
        return 5
def gather_results():
    exam_points = []
    exercise_counts = []
    grades = []
    while True:
        row = input("Exam points and exercises completed: ")
        if row == "":
            break
        parts = row.split()
        exam = int(parts[0])
        exercises = int(parts[1])
        exercise_points = convert_exercises_to_points(exercises)
        grade = calculate_grade(exam, exercise_points)
        exam_points.append(exam)
        exercise_counts.append(exercises)
        grades.append(grade)
    return exam_points, exercise_counts, grades
def print_statistics(exam_points, exercise_counts, grades):
    count = len(grades)
    if count == 0:
        print("No data entered.")
        return
    total_points_sum = 0
    pass_count = 0
    for i in range(count):
        total_points_sum += exam_points[i] + convert_exercises_to_points(exercise_counts[i])
        if grades[i] > 0:
            pass_count += 1
    avg_points = total_points_sum / count
    pass_percentage = (pass_count / count) * 100
    print("Statistics:")
    print("Points average:",avg_points:.1f)
    print("Pass percentage:",pass_percentage:.1f)
    print("Grade distribution:")
    for grade in range(5, -1, -1):
        stars = "*" * grades.count(grade)
        print(f"  {grade}: {stars}")
exam_points, exercise_counts, grades = gather_results()
print_statistics(exam_points, exercise_counts, grades)                                                                                                                                                                                                                                                                                                                                                                                                                                      
