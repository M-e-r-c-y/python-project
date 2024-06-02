'''
# camelCase
Instruction:
- prompts the user for the name of a variable in camel case and 
- outputs the corresponding name in snake case.
'''

def main():
    get_camelCase = input("camelCase: ")
    print(get_camelCase[0])
    print("snake_case:", snake_case(get_camelCase))

def snake_case(camelCase):
    # Initialize the result with the first lowercase letter
    result = [camelCase[0].lower()]

    # Iterate over the string starting from the second character
    for char in camelCase[1:]:
        if char.isupper():
            result.append('_' + char.lower()) 
        else:
            result.append(char)

    return ''.join(result)

main()







'''
#Works only is there are 2 word (doen't work for preferedFirstName)
def main():
    get_camelCase = input("camelCase: ")
    snake_case(get_camelCase)

def snake_case(camelCase):
    snake_case = split(camelCase).lower()
    print("snake_case:", snake_case)

def split(s):
    for i in range(len(s)):
        if s[i-1].islower() and s[i].isupper():
            return s[:i]+ '_' +s[i:] 
    return s

main()

'''