
groceries = []
 # To exit out of the loop enter ctlr-c
while len(groceries) < 3:
    user_input = input("PLease enter an item in the groceries list: ")
    groceries.append(user_input)
   
groceries2 = []
while len(groceries2) < 3:
    user_input2 = input("Please enter some items for a second list: ")
    groceries2.append(user_input2)

new_groceries = groceries + groceries2

#print(new_groceries)
indexes = range(len(new_groceries))
for i in indexes:
    item = new_groceries[i]
    print(f'{i}: {item}')

index_to_replace = int(input('What index would you like to replace?: '))

new_item = input('Please enter new item: ')

new_groceries[index_to_replace] = new_item

print(new_groceries)