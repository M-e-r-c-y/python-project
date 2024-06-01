#Option 4
print("meow\n" * 3, end="") 
    # print("meow" * 3) #prints meowmeowmeow

'''
#Option 1
for i in [0, 1, 2]: # [] represents a list (data type)
    print("meow")
#con: not ideal design for large list

#Option 2
for i in range(3): 
    print("meow")
    #con: we don't really use variable i (just used for counting, not used later)
    #improvment: for _ in range(3)

#Option 3
for _ in range(3): 
    print("meow")  

'''