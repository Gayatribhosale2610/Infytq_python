'''Write a Python function to find all the Strong numbers in a given list of numbers.
Write another function to find and return the factorial of a number. Use it to solve the problem.'''


def factorial(number):
    f = 1
    while number > 0:
        f = f * number
        number -= 1
    return f

def find_strong_numbers(num_list):
    list = []
    for i in num_list:
        number = i
        sum = 0
        if i == 0:
            pass
        else:
            while(i > 0):
                d = i % 10
                fact = factorial(d)
                sum += fact
                i = i // 10
            if sum == number:
                list.append(number)
    return list
        
num_list=[145,375,0,100,2]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
