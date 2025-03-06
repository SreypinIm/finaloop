class ShoppingCart1:
    def __init__(self, item, cart_name, cart_price):
        self.item = item
        self.cart_name = cart_name
        self.cart_price = cart_price

    def __str__(self):
        return f"\n{self.cart_name}:\nItem: {self.item}\nTotal Price: ${self.cart_price:.2f}\n"

    def __add__(self, other):
        return ShoppingCart1(self.item + " and "+ other.item, self.cart_name + " and " + other.cart_name, self.cart_price + other.cart_price)

    def __eq__(self, other):
        if self.item == other.item:
            return f"{self.cart_name} is equal to {other.cart_name}."
        else:
            return f"{self.cart_name} is not equal to {other.cart_name}."

    def __del__(self):
        print(f"{self.cart_name} was deleted.")


cart1 = ShoppingCart1("Apple", "Cart1", 10.0)
cart2 = ShoppingCart1("Banana", "Cart2", 15.0)
# cart3 = ShoppingCart("longan", "Cart3", 9.0)

print(cart1)
print(cart2)
print(cart1 == cart2)
print(cart1 + cart2)
del cart1

#let do another one okkkkk
del cart2


#hi i am sana i am 2years old i have 2 teeth.
#hiihgfgit pull

#hello phea phea haha ot jg add jol
#sana and pin jolmjit phea yy derm jessica 
#dfgf