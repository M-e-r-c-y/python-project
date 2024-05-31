'''
Instruction: 
- prompts the user for input and then 
- outputs that same input in lowercase. 
- Punctuation and whitespace should be outputted unchanged.
* You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.


#function to prompt the user
def get_input():
    prompt = input("Enter text: ")
    return prompt 

#function to change to lowercase
def lower_case():
    input = get_input()
    input = input.lower()
    return input

#print output
print(lower_case())
'''
#Very short method of doing the above:

prompt = input("Enter text: ").lower()
print (prompt)