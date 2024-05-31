# variables are containers for some value that can change over time

#Gussing Game: user can guess some number and tell them if they guess correct or not
def get_guess():
    user_input = int (input("Enter your guess: ")) #int() converts the input to integer variable not string
    return user_input

def main():
    guess = get_guess()
    if guess == 5:
        print("Correct!")
    else:
        print("Incorresct :'(")

main()

'''
Simple way:
    # assign a variable value
x = 5
    # ask user for their guess
guess = int (input("guess a number: "))
    # check if guess matches variable and print if correct or not
if guess == x:
    print("Correct!") 
else:
    print("Incorrect :(") 
'''

