d = {
    'name': 'Pratik',
    'age': 20,
    'city': 'Kolhapur'
}

print(d)

d1 = d.copy()  
print(d1) 

d1.clear()
print(d1)

age = d.get('age')
print(age)  

items = d.items()
print(items) 

keys = d.keys()
print(keys)  

d.pop()
print(d)  

values = d.values()
print(values)  
