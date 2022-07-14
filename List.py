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

#Slice
some_toys = toysList[1:3]
print('Some toys are: {}' .format(some_toys))