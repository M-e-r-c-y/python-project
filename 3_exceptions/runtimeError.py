"""
#Runtime Error:

##### 1. Value Error #####

x = int(input("what's x? "))
print(f"x is {x}")
    # The above gives value error if user inputs string (Eg: 'cat')
    # ValueError: invalid literal for int() with base 10: 'cat'

#solution #1:
try:
    x = int(input("what's x? "))
except ValueError:
    print("x is not an integer")
print(f"x is {x}")

##### 2. Name Error ##### 
# solution #1 solves the 'valueError' but will create NameError
    # NameError: name 'x' is not defined
    #If input is not int, the assignment of the value of x never occurs. Therefore, there is no x to print on our final line of code.

# Solution #2:
try:
    x = int(input("what's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")


# prompt the user again anad again if they don't give rigth value
while True:
    try:
        x = int(input("what's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")
"""
"""
#### Creating a Function to Get an Integer ####

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x

main()


#1. Refine  get_int()
def get_int():
    while True:
        try:
             return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

#2. Refine with get_int() With "PASS"
def get_int():
    while True:
        try:
             return int(input("What's x? "))
        except ValueError:
            pass
"""
#3. Last Refinement
def main():
    x = get_int("what's is x?")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
             return int(input(prompt))
        except ValueError:
            pass

main()