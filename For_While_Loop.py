list_of_toys = ['Car', 'Bus', 'Van', 'Bike', 'Teddy']
for toyInTheList in list_of_toys:
    print(toyInTheList)

listLength = len(list_of_toys)
print("Length of list is: "+str(listLength))
for toyInTheList in range(len(list_of_toys)-1):
    print(list_of_toys[toyInTheList])

print('---------------')

for toyInTheList in range(0, len(list_of_toys), 3):
    print(list_of_toys[toyInTheList])

index = 0
while index < len(list_of_toys):
    print("Printing list of toys using while loop: "+list_of_toys[index])
    index = index + 1

for number in range(1, 3):
    print(number)