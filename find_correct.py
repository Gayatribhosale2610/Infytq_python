'''Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. '''


def find_correct(word_dict):
    c1,c2,c3,c = 0,0,0,0
    for key, value in word_dict.items():
        if key == value:
            c1 += 1
        elif(len(key) != len(value)):
            c3 += 1
        else:
            for i in range(len(value)):
                if value[i] != key[i]:
                    c += 1
            if c < 3:
                c2 += 1
            else:
                c3 += 1
            c = 0
    list = [c1,c2,c3]
    return list
word_dict={'MOST': 'MICE', 'COME': 'COME', 'GET': 'GOT', 'THREE': 'TRICE'}
print(find_correct(word_dict))
