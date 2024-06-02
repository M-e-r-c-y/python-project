'''
# Coke Machine

* Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and 
* only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

Instruction:
- prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
- Once the user has inputted at least 50 cents, output how many cents in change the user is owed.

*Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination. 
'''
def main():
    amount_due = 50 #initial_due
    amount_due_func(amount_due)

def amount_due_func(amount_due):
    print("Amount Due: ", amount_due)
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin in [25, 10, 5]: 
        updated_amount_due = amount_due - inserted_coin
        if updated_amount_due > 0:
            amount_due_func(updated_amount_due)
        else:
            print("Change Owed: ", (-1 * updated_amount_due))
    else: 
        amount_due_func(amount_due)

main()



'''

def main():
    amount_due = 50 #initial_due
    amount_due_func(amount_due)

def amount_due_func(amount_due):
    print("Amount Due: ", amount_due)
    inserted_coin = inserted_coin_func()
    updated_amount_due = amount_due - inserted_coin
    if updated_amount_due > 0:
        amount_due_func(updated_amount_due)
    else:
        print("Change Owed: ", (-1 * updated_amount_due))


def inserted_coin_func():
    while True:
        inserted_coin = int(input("Insert Coin: "))
        if inserted_coin in [25, 10, 5]:
            return inserted_coin

main()

'''