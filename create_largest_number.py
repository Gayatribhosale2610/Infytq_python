'''Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers.
Note: Assume that all the numbers are two digit numbers.'''

def create_largest_number(number_list):
    largest_numbers = ''
    number_list.sort()
    n = len(number_list)
    for i in number_list[::-1]:
        largest_numbers += str(i)
    return int(largest_numbers)

number_list=[23,95,67]
largest_number=create_largest_number(number_list)
print(largest_number)
