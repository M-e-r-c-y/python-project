# print n by n square of bricks#

# Option 3 #
def main():
    print_square(3)

def print_square(size):
    for _ in range(size):  # prints column
        print_row(size)

def print_row(width):
    print("#" * width)

main()

'''
# Option 2 #
def main():
    print_square(3)

def print_square(size):
    for _ in range(size):
        print("#" * size)

main()
'''

'''
# Option 1 #

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

main()
'''