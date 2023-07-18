"""

1. think of an object
restaurant: name,phone,email,operating_hours,ratings,category
2. create its class
3. from class create real objects in memory
"""
#2. create its class
class restaurant:
    pass
#3. from class create real objects in memory
restaurant1 = restaurant()
restaurant2 = restaurant()

#reference copy
restaurant3 = restaurant1
#lhs is reference variable
#rhs is creating an object in heao in ram

print("restaurant is:", restaurant1 , id(restaurant1), type(restaurant1), hex(id(restaurant1)))
print("restaurant is:", restaurant2 , id(restaurant2), type(restaurant2), hex(id(restaurant2)))
print("restaurant is:", restaurant3 , id(restaurant3), type(restaurant3), hex(id(restaurant3)))
print("data inside object", vars(restaurant1))
print("data inside object", vars(restaurant2))
print("data inside object", vars(restaurant3))
#operations on object
# 1. write operation

restaurant1.name = "table by basant"
restaurant1.phone = "99999 11111"
restaurant1.email = "table@basant.com"
restaurant1.operating_hours = "11:00 - 23:00 hrs"
restaurant1.rating = "4.5"
restaurant1.category = "indian,chinese,veg"
print("data inside object", vars(restaurant1))

restaurant2.name = "mc donalds"
restaurant2.phone = "99999 11111"
restaurant2.email = "mcdonalds@mcd.com"

print("data inside object", vars(restaurant2))
print("data inside object", vars(restaurant3))