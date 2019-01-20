age = int(input("Enter your age: "))
restingHR = int(input("Enter your resting heart rate: "))
trainingHR = (0.7 * (220 - age) + 0.3 * restingHR)
print ("Training heart rate: %d beats/min." % trainingHR)


wattage = int(input("Enter wattage: "))
kWh = int(input("Enter number of hours used: "))
price = float(input("Enter price per kWh in cents: "))
cost = (wattage * kWh) / (1000 * price)
print ("Cost of electricity: $%.2f" % cost)
