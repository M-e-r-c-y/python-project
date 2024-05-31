'''
# Math Interpreter
Instruction:
- prompts the user for an arithmetic expression and then 
- calculates and outputs the result as a floating-point value formatted to one decimal place. 
- Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, 
    wherein:
        x is an integer
        y is +, -, *, or /
        z is an integer
    - For instance, if the user inputs 1 + 1, your program should output 2.0. 
    - Assume that, if y is /, then z will not be 0.

*Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!
'''
def main():
    prompt = input("Expression: ") #prompt user
    print(math(prompt))

def math(expression):
    x, y, z = expression.split(" ") #if 1 + 2, will assign 1 to x, + to y, and 2 to z
    x = float(x)
    z = float(z)
    if y == "+":
        sum = float(x + z)
        return f"{sum:.1f}" #one decimal place
    elif y == "-":
        difference = float(x- z)
        return "%.1f" % difference #one decimal place
    elif y == "*":
        product = float(x * z)
        return "%.1f" % product
    elif y == "/" and z!=0:
        quotient = float(x / z)
        return "%.1f" % quotient
    else:
        return "Incorrect Expression"
    

main()