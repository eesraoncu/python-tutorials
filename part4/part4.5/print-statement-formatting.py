Question1: Please write a function named formatted, which takes a list of floating point numbers as its argument. The function returns a new list, which contains each element of the original list in string format, rounded to two decimal points. The order of the items in the list should remain unchanged.
def formatted(numbers):
    return [f"{num:.2f}" for num in numbers]
my_list = [1.234, 0.3333, 0.11111, 3.446]
new_list = formatted(my_list)
print(new_list)
