'''Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change'''


def encrypt_sentence(sentence):
    string = sentence.split()
    v = set("aeiouAEIOU")
    a = []
    for i, j in enumerate(string):
        if i % 2 != 0:
            vowel = ""
            conso = ""
            for k in list(j) :
                if k in v:
                    vowel+=k
                else:
                    conso+=k
            a.append(conso+vowel)
        else:
            a.append(j[::-1])
    a = " ".join(a)
    return a
  
sentence="The sun rises in the east"
print(encrypt_sentence(sentence))
