def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * (i+1))

if __name__ == "__main__": # main() function is called only when the script is executed directly.
    main()

# print(i, end=" ") to check what i value is
# breakpoints