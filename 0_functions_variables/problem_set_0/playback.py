'''
Instruction:
- prompt the user for input and then 
- outputs that same input, replacing each space with ... (i.e., three periods)

'''
text = input("Enter text: ").replace(" ", "...")
print(text)


'''
#if we want output with only first 2 whitespace replaced 
text = input("Enter text: ").replace(" ", "...", 2)
print(text)

'''