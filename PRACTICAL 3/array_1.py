cars = ["Ford", "Volvo", "BMW"]
print(cars)

x = cars[0]
print(cars)

x = len(cars)
print("Length of array is ",x)

for x in cars:
  print(x)

cars.append("Honda") #add at end
print(cars)

cars.pop(1)
print(cars)

cars.reverse()
print(cars)

print(cars[0:2])