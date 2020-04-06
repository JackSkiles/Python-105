# Creates empty grocery list
groceries1 = []
# While loop should loop unless empty space of some kind is entered. Each loop the user should enter a new object to be added to the list.
while True:
    grocery_input = input('Please enter a grocery you would like to add: ')
    if grocery_input == '':
        break
    elif grocery_input == ' ':
        break
    elif grocery_input == '   ':
        break
    groceries1.append(grocery_input)
    
# Prints the range of the list using a for loop.
indexes = range(len(groceries1))
for i in indexes:
    item = groceries1[i]
    print(f'{i}: {item}')

# Prompts the user to enter begining and ending parameters.
user_prompt = int(input('please enter where you would like the new list to begin: '))
user_prompt2 = int(input('Please enter where you would like the new list to end: '))

# If else that checks if user entered same number twice
if user_prompt == user_prompt2:
    new_item = input('What is the new item? ')


    groceries1[user_prompt] = new_item
# creates a second list and a while loop that appends new items like the first loop. The only difference is that the second list will be assigned to the user specified points of the
# first list after it is finished.
else:
    second_list = []
    while True:
        new_item = input('What is the new item? ')
        if new_item == '':
            break
        second_list.append(new_item)
    groceries1[user_prompt:user_prompt2] = second_list
#counter = 0
#while counter < len(groceries1)
#second_list = []
# #while True:
#     item_prompt = input('Please entier items you would like to replace the old ones with: ')#.split(',')
#         if item_prompt == '':
#             break
#         elif item_prompt == ' ':
#             break
#         elif item_prompt == '   ':
#             break
#     second_list.append(item_prompt)
# groceries1[user_prompt:user_prompt2] = [second_list]
#print( groceries1[0])]
# Prints list one last time.
for i in indexes:
    item = groceries1[i]
    print(f'{i}: {item}')