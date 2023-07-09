# Multi Value Container

# LIST
# LIST is indexed
# LIST is MUTABLE
names = ["sumehar", "taran", "pebby", "mannat", "ranbir"]
print(names)
print(names[4])
names[2] = "dillu" # OK
print(names)
del names[1]
print(names)

names.append("harman")
names.append("sam")
names.append("ranbir")
print(names)