# print a row horizontally: ###

def main():
    print_row(3)

def print_row(width):
    print("?" * width)     

main()



'''
# Alternative:
 
for _ in range(3):
    print("#", end="")
print()    # this line does end="\n"
'''
