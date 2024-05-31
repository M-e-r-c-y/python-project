'''
#Deep Thought
#Instruction:
- prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
- outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. 
- Otherwise output No.
'''
prompt = input("What's the answer to the Great Question of Life, the Universe and Everything? ")

'''
#Option #1
if prompt == "42" or prompt.lower() == "forty-two" or prompt.lower() == "forty two":
    print("Yes!")
else:
    print("No!")
'''

#Option #2
match prompt.lower():
    case "42" | "forty-two" | "forty two":
        print("YES!")
    case _:
        print("NO")