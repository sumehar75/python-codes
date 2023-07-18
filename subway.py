#conditional constructs
#decision making
#if/else
#subwayoffers

message = """"
            welcome to zomato
              subway offers
               
            WELCOME50
            get 50% off up to 100
            valid on total value of items worth 159 or more
            
            ZOMPAYTM
            get 20% OFF up to 50 and 25 paytm cashback using paytm
            valid on total value of items worth 299 or more
            
        """
print(message)
amount = int(input("enter total amount:"))
promo_code = input("enter promo code:")

""""
#simple or regular if else
if amount>=159:
    print("promo code applied")
else:
    print("promo code cannot be applied")
"""
"""
if amount >= 159:
    if promo_code == "WELCOME50":
        print("promo code applied sucessfuly")

        discount = 0.50 * amount

        if discount >= 100:
            discount = 100

        amount_to_pay= amount-discount
        print("pay amount: \u20b9", amount_to_pay)
    else:
        print("invalid promo code")
        print("pay amount:\u20b9", amount)
else:
    print("you cannot apply promo code")

"""
#IF/ELSE LADDER


if promo_code == "WELCOME50":
    if amount >= 159:
        print("promo code applied sucessfuly")

        discount = 0.50 * amount

        if discount >= 100:
            discount = 100

        amount_to_pay= amount-discount
        print("pay amount: \u20b9", amount_to_pay)
    else:
        print("amount is less to apply thiS promo code")
        print("pay amount:\u20b9", amount)
elif promo_code == "ZOMPAYTM":
    if amount >= 299:
        print("promo code applied sucessfully")

        discount = 0.20 * amount


        if discount >= 50:
            discount = 50
        amount_to_pay = amount - discount
        print("amount to pay: \u20b9", amount_to_pay)
        print("you will get a cashbacK of \u20b9 25")
    else:
        print("amount is less to apply this promo code")
        print("amount to pay: \u20b9")

else:
    print("promo code invalid")
    print("amount to pay:\u20b9",amount)





