'''
#Einstein
Instruction:
- prompts the user for mass as an integer (in kilograms) and then 
- outputs the equivalent number of Joules as an integer. 
- Assume that the user will input an integer

E = mc^2
 E - represents energy (measured in Joules), 
 m - represents mass (measured in kilograms), and 
 c - represents the speed of light (measured approximately as 300000000 meters per second)

#Method 1
m = int(input("mass: "))
c = 300000000
e = m* (c**2) # or e = m* (pow(c,2))
print("E = ", e)

'''
#Method 2
def main():
    mass = int(input("mass: "))
    print("E = ", calculate(mass))

def calculate(m):
    c = 300000000
    e = m* (c**2)
    return e

main()