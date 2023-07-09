#single value container
#create operation - RAM
instagram_user_name= "sumehar"
# read operation
print(instagram_user_name, id(instagram_user_name))
print(instagram_user_name, hex(id(instagram_user_name)))
print(instagram_user_name, oct(id(instagram_user_name)))
print(instagram_user_name, bin(id(instagram_user_name)))
print(type(instagram_user_name))


user_name = "sam"
print(user_name, id(user_name), type(user_name))
# user_name is a reference variable which will be created in STACK
# Value sam is created within a storage container of type string in HEAP

user = "sumehar"
print(user, id(user), type(user))

#reference copy operation
another_user = user
print(another_user, id(another_user), type(another_user))

#update operation
user = "riva"
print(user, id(user), type(user))

# delete operation
del user
#print(user, id(user), type(user))

del another_user
# print(another_user, id(another_user), type(another_user))  # error
print(user_name, id(user_name), type(user_name))
