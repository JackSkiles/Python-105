
groceries = []

counter = 0
counter1 = 1

 # To exit out of the loop enter ctlr-c
while counter != counter1:
    user_input = input("PLease enter an item in the groceries list: ")
    groceries.append(user_input)
    print(groceries)
    counter += 1
    counter1 += 1