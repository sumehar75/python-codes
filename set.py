#multi value container
#set
#output is unordered
#it dpoes not support indexing
#it works on hashing

sumehar_followers = {"pebby","taran","mannat","ranbir","harman"}
print(sumehar_followers, type(sumehar_followers), id(sumehar_followers))

riva_followers = {"vanshaj","apoorva","pebby","taran","mannat"}
print(riva_followers, type(riva_followers), id(riva_followers))

mutual_followers = sumehar_followers.intersection(riva_followers)
print(mutual_followers, type(mutual_followers), id(mutual_followers))

mutual_list = list(mutual_followers)
print(mutual_list, type(mutual_list), id(mutual_list))

