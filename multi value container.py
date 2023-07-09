#multi value container
#create operation
# tuple
numbers = 10, 20, 30, 40, 50

#read operations
print(numbers, id(numbers), type(numbers))

# list
data = [10, 10.2, "sam", "sumehar", 100]
print (data, id(data), type(data))

print(data[0], id(data[0]), type(data[0]))
print(data[1], id(data[1]), type(data[1]))
print(data[2], id(data[2]), type(data[2]))

#reference
new_data = data
print(new_data, id(new_data), type(new_data))
print(new_data[3])

new_data[2] = "gill"
print(new_data, id(new_data), type(new_data))

#delete operation
del new_data[3]
print(new_data, id(new_data), type(new_data))

print (data, id(data), type(data))