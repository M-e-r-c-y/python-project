def main():
    x = int (input("x is: "))
    print("x squared is: ", square(x))

def square(n):
    return pow(n, 2)
   
main()