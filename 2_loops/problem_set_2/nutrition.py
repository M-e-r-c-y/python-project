'''
# Nutrition Facts
Instruction:
- prompts users to input a fruit (case-insensitively) and then 
- outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. 
- Capitalization aside, assume that users will input fruits exactly as written in the poster 
    - (e.g., strawberries, not strawberry). 
- Ignore any input that isn’t a fruit.

'''

def main():
    fruit_input = (input("Item: ")).lower()
    print("Calories:", calories(fruit_input))

def calories(fruit):
    fruits_calories = {
        "apple": "130",
        "banana": "110",
        "grapes": "90",
        "lemon": "15",
    }
    
    return fruits_calories[fruit]

main()
