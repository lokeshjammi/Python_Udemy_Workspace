toysList = ['Car', 'Jeep', 'Teddy']
print(toysList[0])

toysList[0] = 'Pig'

print(toysList)

print(toysList[-1])

toysList[-1] = 'Car'
print(toysList)

more_toys = ['Bike', 'Bus']
toysList.extend(more_toys)
print(toysList)

toysList.insert(0, 'ABC')
print(toysList)

toysList.sort()
print(toysList)

new_toy_list = ['Bag', 'Skatescooter']
print(toysList + new_toy_list)

#Slice
some_toys = toysList[1:3]
print('Some toys are: {}' .format(some_toys))

firstTwoToys = toysList[0:2]
print('First two toys in the List is: {}' .format(firstTwoToys))

again_first_two_toys = toysList[:2]
print('First two toys in the list is: {}' .format(again_first_two_toys))

#String slice
part_of_the_string = 'horse'[:3]
print(part_of_the_string)

#Exception handling
try:
    school_index = toysList.index('School')
except:
    school_index = 'No School is found'
print(school_index)

#Practice Exercise
list_of_actions = []
finished = False
while not finished:
    user_data = input("Enter a task for your to-do list: ")
    if len(user_data) == 0:
        finished = True
    else:
        list_of_actions.append(user_data)
        print("Task Added")
print(list_of_actions)