age = 12
if age > 31:
    print('You are old enough to vote')
elif age < 30 and age > 25:
    print('You can apply for vote card')
else:
    print('Not eligible to vote')

print('Have a nice day')

#Practice Exercise
milesData = int(input("How far would you like to travel in miles?"))
if milesData < 3:
    print('I suggest to walk to your destination')
elif milesData > 3 and milesData < 300:
    print('I suggest to drive to your destination')
else:
    print('I suggest to fly to your destination')