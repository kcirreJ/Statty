string = input()


def new_string(string):
    new = ""
    string = string

    for letter in range(len(string)):
        if string[letter] != " ":
            new += string[letter]
    return new

def reverse(string):
    string = string
    new = new_string(string)
    reversed_string = ""

    for i in range(len(new) - 1,-1,-1):
        reversed_string += new[i]

    return reversed_string

def palindrome(string):
    string = string
    string_one = new_string(string)
    strting_two = reverse(string)

    if string_one == strting_two:
        return f"{string} is a palindrome"
    else:
        return f"{string} is not a palindrome"

print(palindrome(string))