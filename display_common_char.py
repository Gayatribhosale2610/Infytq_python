'''Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.'''

def find_common_characters(msg1,msg2):
    common_characters = ""
    for i in msg1:
        if i in msg2 and i not in common_characters:
            if i == " ":
                pass
            else:
                common_characters += i            
    if common_characters == "":
        return -1
    return (common_characters)       
msg1="moto"
msg2="moto"
print(find_common_characters(msg1,msg2))
