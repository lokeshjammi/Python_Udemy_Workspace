#operate server cost per day & Month
charge = 0.51
costPerDay = 0.51 * 24
costPerMonth = costPerDay * 30
print("Server cost per day: "+str(costPerDay))
print("Server cost per month: "+str(costPerMonth))
#One day cost to operate 20 servers
twentyServerCostPerDay = costPerDay * 20
twentyServerCostPerMonth = costPerMonth * 20
print("20 Server cost per day is: "+str(twentyServerCostPerDay))
print("20 Server cost per month is: "+str(twentyServerCostPerMonth))
daysCount = 918/costPerDay
print(str(daysCount)+" days a server can be maintained with the amount")