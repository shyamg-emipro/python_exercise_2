class InventoryManagement:
    # Manages purchase sale and quantity of the product

    def __init__(self, product_name, product_qty):
        # product_name
        # product_qty
        # Initialises these two variables

        self.product_name = product_name
        self.product_qty = product_qty

    def purchase_product(self, no_of_product):
        # no_of_product to purchase
        # Purchases and increase product quantity

        self.product_qty += no_of_product

    def sell_product(self, no_of_product):
        # no_of_product to sale
        # Sell the product and deduct no_product from the product_qty

        if self.product_qty >= no_of_product:
            self.product_qty -= no_of_product
            self.display_product_qty()
        else:
            print("\nNot enough product quantities to sell!")

    def display_product_qty(self):
        # Shows available product quantity

        print("\n\nProduct Name          qty")
        print("___________________________")
        print("{:<18}{:<18}".format(self.product_name, self.product_qty))


inventory_management = InventoryManagement(
    "Bycycle",
    15
)  # make object of InventoryManagement and Enters the initial values

while True:
    # shows menu can call Appropriate method according to option provided by the user

    print("""
        1. Purchase Product
        2. Sale Product
        3. View Available Product Quantities
        4. Exit
    """)
    option = int(input("Choose the option:  "))

    if option == 1:
        inventory_management.purchase_product(int(input("Enter no. of product you want to purchase: ")))

    elif option == 2:
        inventory_management.sell_product(int(input("Enter no. of product you want to sale: ")))

    elif option == 3:
        inventory_management.display_product_qty()

    elif option == 4:
        break

    else:
        print("Please select right option!")
