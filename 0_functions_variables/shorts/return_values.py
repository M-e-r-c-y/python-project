#Return Values

#function to check if there is 'hello' in input 

def greet(input):
    if "hello" in input:
        return "Hello, there" #returns "hello, there" but not stored 
    else:
        return "please, use the word 'hello' in your greeting"

name = input("what's your name? ")
print("say hello, don't be shy, ", name)
prompt = input()
# greet(prompt) will not show any value b/c return value not stored
greetings = greet(prompt) #here we are storing return value in a variable named 'greetings'
print("Hm, ", greetings, name) 