'''
Instruction:
- implement a function called convert that accepts a str as input and 
- returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and 
- any :( converted to 🙁 (otherwise known as a slightly frowning face). 
- All other text should be returned unchanged.

- Then, in that same file, implement a function called main that 
- prompts the user for input, calls convert on that input, and prints the result. 

'''
def convert(text):
    converted = text.replace(":)", "🙂").replace(":(", "🙁")
    return converted

def main():
    prompt = input("Enter Text: ")
    print(convert(prompt))

main()