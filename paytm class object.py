#standarisation in paytm
class Mobile_Bill:
    # CONSTRUCTOR
    def __init__(self, Type="", Mobile_number=0, Operator="", Amount=0):
        self.Type = Type
        self.Mobile_number = Mobile_number
        self.Operator = Operator
        self.Amount = Amount

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Type:", self.Type)
        print("Mobile_number:", self.Mobile_number)
        print("Operator:", self.Operator)
        print("Amount:", self.Amount)
        print("~~~~~~~~~~~~~~~~~~~~~~~~")

Mobile_Bill1 = Mobile_Bill("Prepaid", 8976556789, "airtel", 500)
Mobile_Bill2 = Mobile_Bill("Postpaid", 6789543247, "airtel", 500)
Mobile_Bill3 = Mobile_Bill("Postpaid", 8888822222, "BsnlRecharge", 1500)

Mobile_Bill1.show()
Mobile_Bill2.show()
Mobile_Bill3.show()

#print(vars(Mobile_Bill1))
#print(vars(Mobile_Bill2))
#print(vars(Mobile_Bill3))

"""
Mobile_Bill1 = Mobile_Bill()
Mobile_Bill2 = Mobile_Bill()
Mobile_Bill1 = Mobile_Bill()

Mobile_Bill1.Type = "Prepaid"
Mobile_Bill1.Mobile_number = 8976556789
Mobile_Bill1.Operator = Airtel
Mobile_Bill1.Amount = 500

Mobile_Bill2.Type = "Postpaid"
Mobile_Bill2.Mobile_number = 6789543247
Mobile_Bill2.Operator = Airtel
Mobile_Bill2.Amount = 500

Mobile_Bill2.Type = "Postpaid"
Mobile_Bill2.Mobile_number = 8888822222
Mobile_Bill2.Operator = BsnlRecharge
Mobile_Bill2.Amount = 1500
"""
