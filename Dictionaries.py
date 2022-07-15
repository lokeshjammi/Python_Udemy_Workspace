my_details = {'Name': 'Lokesh', 'age': 28, 'Places': ['Chennai', 'Hyderabad']}
print(my_details)
print(my_details['Name'])

my_details['Name'] = 'Lokesh Jammi'
print(my_details)

my_details['Job_Role'] = 'QA Test Engineer'
print(my_details)

if 'Name' in my_details:
    print('Person\'s name is: '+my_details['Name'])

if 'Places' in my_details:
    print('Person\'s current location is: '+my_details['Places'][1])

for place in my_details.items():
    print('Places in the list are {}' .format(my_details['Places']))

print(len(my_details))

print('Lokesh Jammi' in my_details.values())

#Practice Exercise
people_interesting_facts = {
    'Jeff': 'Is afraid of clowns',
    'David': 'Plays the piano',
    'Jason': 'Can fly an airplane'
}

for person in people_interesting_facts:
    print(person+"'s interesting fact is: "+people_interesting_facts[person])

people_interesting_facts['Jill'] = 'Can hula dance'

for person in people_interesting_facts:
    print(person+"'s interesting fact is: "+people_interesting_facts[person])