# Dictionary with more data [List of dictionaries]
    # [] = list   # {} = dictionary
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
for person in students:
    print(person["name"], person["house"], person["patronus"], sep="| ")