class Manufacturing:
    product_qty = 0

    def __init__(self, raw_material, product_name, ratio_qty):
        # This function initializes the properties of the class
        # raw_material is a dict that should have raw material name as Key and raw_material qty as Value
        # product_name
        # ratio_qty is a dict that should have name of raw material as Key and raw material required to build 1 product as a value

        self.raw_material = raw_material.copy()
        self.product_name = product_name
        self.ratio_qty = ratio_qty.copy()

    def produce(self, no_of_products):
        # no_of_products no of product to be produced

        temp = self.raw_material.copy()
        for name, qty in self.ratio_qty.items():
            # Loop through items in ratio_qty
            if self.raw_material[name] >= no_of_products * qty:
                # Verifies that there is enough qty to produce the product
                temp[name] -= no_of_products * qty  # deduct the used raw material in the process of producing
            else:
                # Error msg if there isn't enough raw material available
                print("\n\nNot enough raw material available to produce the product, please do the purchase!")
                return False
        self.raw_material = temp.copy()
        self.product_qty += no_of_products  # Increase product count
        print("\n\nProduct Produced Successfully")  # Success msg

    def display_raw_material_stock(self):
        # Display Raw Material Quantity
        # Loop Through raw_material to display qty of each item

        print("\n\nRaw Material", "   qty")
        print("________________________")
        for name, qty in self.raw_material.items():
            print("{:<18}{:<18}".format(name, qty))

    def display_final_product_stock(self):
        # Display Product name using product_name
        # Display Product Quantity using product_qty

        print("\n\nProduct Name        qty")
        print("________________________")
        print("{:<18}{:<18}".format(self.product_name, str(self.product_qty)))

    def purchase_raw_material(self, new_raw_material):
        # Purchase new Raw Material
        # Loop through passed dict and add value of each item in respective raw_material item value

        for name, qty in new_raw_material.items():
            self.raw_material[name] += qty
        print("Material purchased successfully")


man = Manufacturing(
    {'wheels': 10, 'chain': 5, 'handle': 5, 'frame': 5, 'gear': 5},
    'bicycle',
    {'wheels': 2, 'chain': 1, 'handle': 1, 'frame': 1, 'gear': 2}
)

while True:
    print("""
             1. Purchase Raw Material Product
             2. Manufacture Finish Product
             3. Show Raw Material Quantity
             4. Show Actual Product Quantity
             5. Exit""")

    option = int(input("Select and option to Continue:  "))
    if option == 1:
        man.purchase_raw_material({
            'wheels': int(input("Wheels:  ")),
            'chain': int(input("Chain:  ")),
            'handle': int(input("Handle-Bar:  ")),
            'frame': int(input("Frame:  ")),
            'gear': int(input("Gear:  "))})

    elif option == 2:
        man.produce(int(input("Enter no of product to be produced:  ")))
    elif option == 3:
        man.display_raw_material_stock()
    elif option == 4:
        man.display_final_product_stock()
    elif option == 5:
        break
    else:
        print("Please Select valid Option")
