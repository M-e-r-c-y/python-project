'''
# Just setting up my twttr
Instructio:
- prompts the user for a str of text and then 
- outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
- whether inputted in uppercase or lowercase.
'''

def main():
    input_string = input("Input: ")
    print(remove_vowels(input_string))

def remove_vowels(input_string):
    for char in 'aeiouAEIOU':
        input_string = input_string.replace(char, '')
    return input_string

main()