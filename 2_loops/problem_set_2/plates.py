'''
# Vanity Plates
Requirments: 
* All vanity plates must start with at least two letters.
* vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
* Numbers cannot be used in the middle of a plate; they must come at the end. 
    - For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
* The first number used cannot be a ‘0’.
* No periods, spaces, or punctuation marks are allowed.

Instruction:
- prompts the user for a vanity plate and then 
- output Valid if meets all of the requirements or Invalid if it does not. 
- Assume that any letters in the user’s input will be uppercase. 
- Structure your program per the below, 
    - wherein is_valid returns True if s meets all requirements and 
    - False if it does not. 
- Assume that s will be a str. 
- You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
'''
import string #for Req4

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

 # Assume that any letters is uppercase
 
def is_valid(s):
   
        # 1. start with at least two letters
    Req1 = (len(s) >= 2) and (s[0].isalpha() and s[1].isalpha())
        # 2. maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    Req2 = (2 <= len(s) <= 6)
    # Req3() defined in another function

        # 4. No periods, spaces, or punctuation marks are allowed
    Req4 = (any(char in string.punctuation for char in s)) # True is thre is punctuation 

    if Req1 and Req2 and Req3(s) and (not Req4):
        return True
    else:
        return False

# 3. Numbers cannot be used in the middle of a plate; they must come at the end. 
        ## The first number used cannot be a ‘0’.
def Req3(s):
        # Initialize state to track where in the sequence we are and the first digit seen
    seen_digit = False
    first_digit_seen = False

    # Iterate through each character in the plate
    for char in s:
        if char.isdigit():  # Check if the character is a digit
            if not first_digit_seen:  # Check if this is the first digit we've seen
                if char == '0':  # If the first digit is '0', return False
                    return False
                first_digit_seen = True  # Mark the first digit as seen
            seen_digit = True
        elif seen_digit and char.isalpha():  # A letter after a digit is invalid
            return False

    # If the loop completes without returning False, the plate is valid
    return True

main()