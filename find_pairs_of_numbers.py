'''Write a python function, find_pairs_of_numbers() which accepts a list of positive integers with no repetitions and returns count of pairs of numbers in the
list that adds up to n. The function should return 0, if no such pairs are found in the list.'''

def find_pairs_of_numbers(num_list,n):
    count = 0
    for i in range(len(num_list)):
        for j in range(i,len(num_list)):
            if num_list[i] == num_list[j]:
                continue
            elif num_list[i] + num_list[j] == n:
                count+=1
    if count == 0:
        return 0
    return count
num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_number(num_list,n))
