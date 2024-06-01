# Dictionaries
# Where a list is a list of multiple values, a dict associates a key with a value.

# Track who is what House

'''
#List:
students = ["Hermoine", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Griffindor", "Slytherin"]
'''
# Python dictionary: student = {"key1": "value1", "key2": "value2"}

students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for person in students:
    print(person, students[person], sep=": ")

'''
# Option 2: prints out all keys
for person in students:
    print(person)
'''

'''
# Option 1: prints out values of the keys we want
print(students["Hermoine"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
'''