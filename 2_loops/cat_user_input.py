# ask user how many times the cat should meow

#Option: using defining functions
def main():
    '''
    n = get_number() 
    meow(n)
    '''
    meow(get_number()) 

def get_number():
    while True:
        user_input = int(input("What's n? "))
        if user_input > 0:
            return user_input # we can do break here and then use 'return' after the while loop

def meow(n):
    for _ in range(n):
        print("meow")

main()

'''
#Option 1:  Loop indefinitely until the user provides a valid input
# if you want to get user input that matches certain expectation, use "while True: " - w/c induce infinite loop
#E.g: if user doesn't give you positive number(n>0), keep asking the user for input 

while True:
    n = int(input("What's n? ")) #keep asking 
    if n > 0:
        break #break out of the infinit loop of asking for n when (n>0)
    
    ### OR other option
    if n < 0:
        continue #continue prompting user if n<0 or negative
    else:
        break #break out of the infinit loop of getting asked for n when (n<0) is false
    ###
for _ in range(n):
    print("meow")
''' 