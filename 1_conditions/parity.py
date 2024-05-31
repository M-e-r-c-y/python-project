#even or odd
'''
#Method 1:
x = int(input("number: "))
if x%2 == 0:
    print("Even")
else:
    print("Odd")
'''

#Method 2:
def main():
    x = int(input("number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
# best Option
   return n%2 == 0

   '''
# Option 1:
   if n%2 == 0:
       return True 
   else:
       return False
    '''
# Option 2: return True if n%2 == 0 else False

main()


