#shopping cart using oops
#one shopping cart has many items
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.menu = {
            "dal": Item("dal", 300),
            "parantha": Item("parantha", 40),
            "noodles": Item("noodles", 250),
            "burger": Item("burger", 150),
            "fries": Item("fries", 100),
            "cola": Item("cola", 50),
        }
        self.items = []

    def add_item(self, item_name, quantity):
        item = self.menu.get(item_name)
        if item:
            self.items.append((item, quantity))
        else:
            print("Item not found in the menu.")

    def calculate_total_amount(self):
        total_amount = 0
        for item, quantity in self.items:
            total_amount += item.price * quantity
        return total_amount

    def display_menu(self):
        print("MENU:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for item in self.menu.values():
            print(f"{item.name}: \u20b9{item.price}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def apply_promo_code(self, promo_code):
        amount = self.calculate_total_amount()

        if promo_code == "WELCOME50":
            if amount >= 159:
                print("Promo Code Applied Successfully...")
                discount = min(0.50 * amount, 100)
                amount_to_pay = amount - discount
                print("Please Pay: \u20b9", amount_to_pay)
            else:
                print("Amount is Lesser for Promo Code...")
                print("Please Pay: \u20b9", amount)

        elif promo_code == "ZOMPAYTM":
            if amount >= 299:
                print("Promo Code Applied Successfully...")
                discount = min(0.20 * amount, 50)
                amount_to_pay = amount - discount
                print("Please Pay: \u20b9", amount_to_pay)
                print("You will get a cashback of: \u20b9 25")
            else:
                print("Amount is Lesser for Promo Code...")
                print("Please Pay: \u20b9", amount)
        else:
            print("Promo Code Invalid")
            print("Please Pay: \u20b9", amount)

def main():
    cart = ShoppingCart()

    cart.display_menu()

    while True:
        item_name = input("Enter Dish Name to add in Cart: ")
        quantity = int(input("Enter Dish Quantity: "))
        cart.add_item(item_name, quantity)

        choice = input("Do You wish to add more items? (yes/no)")
        if choice == "no":
            break

    for item, quantity in cart.items:
        print(f"{item.name} - Quantity: {quantity}")

    amount = cart.calculate_total_amount()
    print("TOTAL AMOUNT: \u20b9", amount)

    message = """
        Welcome to Zomato
        OFFERS FOR TODAY

        WELCOME50
        Get 50% OFF up to ₹100
        Valid on total value of items worth ₹159 or more.


        ZOMPAYTM
        Get 20% OFF up to ₹50 and ₹25 Paytm cashback using Paytm
        Valid on total value of items worth ₹299 or more.
    """

    print(message)
    promo_code = input("Enter Promo Code: ")
    cart.apply_promo_code(promo_code)


if __name__ == "__main__":
    main()