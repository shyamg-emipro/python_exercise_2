class InventoryManagement:
    # Manages purchase sale and quantity of the product

    def __init__(self, product):
        # self.product is a dictionary
        # self.product has incremental indexed keys
        # self.product has another dictionary contains price, quantity, subtotal as a value of product

        # product dictionary contains {'price': <price>, 'quantity': <quantity>}

        self.product = {}
        for val in range(len(product)):
            product[val]['subtotal'] = product[val]['price'] * product[val]['quantity']
            self.product[val + 1] = product[val]
        print("\nInitially available products Entered through constructor.")
        print(self.product)

    def purchase_product(self, product):
        # product to purchase
        # Purchases and increase product quantity

        # product dictionary contains {'price': <price>, 'quantity': <quantity>}

        product['subtotal'] = product['price'] * product['quantity']
        self.product[len(self.product) + 1] = product
        print(self.product)

    def sell_product(self, no_of_product):
        # no_of_product to sale
        # Sell the product and deduct no_product from the product_qty

        first_product = self.product[next(iter(self.product))]
        if first_product['quantity'] == 0:
            self.product.pop(next(iter(self.product)))
            first_product = self.product[next(iter(self.product))]
        if first_product['quantity'] >= no_of_product:
            first_product['quantity'] -= no_of_product
            first_product['subtotal'] = first_product['price'] * first_product["quantity"]
            self.display_product_qty()
        else:
            print("\nNot enough product quantities to sell!")

    def display_product_qty(self):
        # Shows available product quantity

        print("Total available products in the Inventory")
        print(self.product)
        first_product = self.product[next(iter(self.product))]
        print("\n\nProduct Price          qty")
        print("___________________________")
        print("{:<18}{:<18}".format(first_product['price'], first_product['quantity']))

    def all_products_valuation(self):
        # shows valuation of all products
        # subtotal_sum sum of all subtotals all available products

        subtotal_sum = 0
        qty_sum = 0
        for key, value in self.product.items():
            subtotal_sum += value['subtotal']
            qty_sum += value['quantity']

        # valuation
        valuation = subtotal_sum / qty_sum
        print("Valuation :  ", valuation)


inventory_management = InventoryManagement([
    {"price": 400, "quantity": 10},
    {"price": 350, "quantity": 30}
])  # make object of InventoryManagement and Enters the initial values

while True:
    # shows menu can call Appropriate method according to option provided by the user

    print("""
        1. Purchase Product
        2. Sale Product
        3. View Available Product Quantities
        4. Show Valuation
        5. Exit
    """)
    option = int(input("Choose the option:  "))

    if option == 1:
        inventory_management.purchase_product({'price': int(input("price: ")), 'quantity': int(input("quantity: "))})

    elif option == 2:
        inventory_management.sell_product(int(input("Enter no. of product you want to sale: ")))

    elif option == 3:
        inventory_management.display_product_qty()

    elif option == 4:
        inventory_management.all_products_valuation()

    elif option == 5:
        break

    else:
        print("Please select right option!")
