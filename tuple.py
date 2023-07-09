# Multi Value Container

# TUPLE
# Tuples are indexed
# Tuples are IMMUTABLE

names = ("sumehar", "taran", "pebby", "mannat", "dillu")
print(names)
print(names[2])

#immutable egs
#names[2] = "ranbir"
#del names[1]

print(id(names))
#indexed eg
print(id(names[0]))

instagram_user_name = "sumehar"
print(instagram_user_name, id(instagram_user_name))

#comparing
print(instagram_user_name == names[0])