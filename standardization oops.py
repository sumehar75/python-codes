#standardisation in oops
class dish:
    #constructor
    def __init__(self, name ="", price= 0, ratings= 0):
        self.name = name
        self.price =  price
        self.ratings=  ratings
    def show(self):
        print("*************************")
        print("name is:", self.name)
        print("price is:", self.price)
        print("rating is:", self.ratings)
        print("*************************" )


dish1 = dish("noodles", 300, 4)
dish2 = dish("burger", 150, 4.5)
dish3 = dish("pasta", 450, 3.5)

dish1.show()
dish2.show()
dish3.show()
