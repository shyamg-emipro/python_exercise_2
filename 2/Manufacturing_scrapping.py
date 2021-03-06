class Manufacturing:

    def __init__(self, raw_material, product_name, ratio_qty):
        # This function initializes the properties of the class
        # raw_material is a dict that should have raw material name as Key and raw_material qty as Value
        # product_name
        # ratio_qty is a dict that should have name of raw material as Key and raw material required to build 1 product as a value

        self.product_qty = 0
        self.raw_material = raw_material
        self.product_name = product_name
        self.ratio_qty = ratio_qty

    def produce(self, no_of_products):
        # no_of_products no of product to be produced

        if self.raw_material >= no_of_products * self.ratio_qty:
            # Verifies that there is enough qty to produce the product
            self.raw_material -= no_of_products * self.ratio_qty  # deduct the used raw material in the process of producing
        else:
            # Error msg if there isn't enough raw material available
            print("\n\nNot enough raw material available to produce the product, please do the purchase!")
            return False
        self.product_qty += no_of_products  # Increase product count
        print("\n\nProduct Produced Successfully")  # Success msg


class Purchase(Manufacturing):

    def purchase_raw_material(self, new_raw_material):
        # Purchase new Raw Material
        # Loop through passed dict and add value of each item in respective raw_material item value
        self.raw_material += new_raw_material
        print("Material purchased successfully")


class Scrapping(Manufacturing):

    def scrap_the_raw_material(self, no_of_raw_material):
        if self.raw_material >= no_of_raw_material:
            self.raw_material -= no_of_raw_material
            print("Raw Material Scrapped successfully!")
        else:
            print("There are no Raw Materials available in the stock!")

    def scrap_the_product(self, no_of_product):
        if self.product_qty >= no_of_product:
            self.product_qty -= no_of_product
            print("Product Scrapped successfully!")
        else:
            print("There are no Products available in the stock!")


class Product(Purchase, Scrapping):

    def __init__(self, raw_material, product_name, ratio_qty):
        Manufacturing.__init__(self, raw_material, product_name, ratio_qty)

    def display_raw_material_stock(self):
        # Display Raw Material Quantity
        # Loop Through raw_material to display qty of each item

        print("\n\nRaw Material", "   qty")
        print("________________________")
        print("{:<18}{:<18}".format("Wheels", self.raw_material))

    def display_final_product_stock(self):
        # Display Product name using product_name
        # Display Product Quantity using product_qty

        print("\n\nProduct Name        qty")
        print("________________________")
        print("{:<18}{:<18}".format(self.product_name, str(self.product_qty)))


manufacturing_scrapping = Product(
    10,
    'bicycle',
    2
)

while True:
    print("""
             1. Purchase Raw Material Product
             2. Manufacture Finish Product
             3. Show Raw Material Quantity
             4. Show Actual Product Quantity
             5. scrapping the raw material product
             6. scrapping the actual product
             7. Exit""")

    option = int(input("Select and option to Continue:  "))
    if option == 1:
        wheels = int(input("Wheels:  "))
        manufacturing_scrapping.purchase_raw_material(wheels)

    elif option == 2:
        no_of_product = int(input("Enter no of product to be produced:  "))
        manufacturing_scrapping.produce(no_of_product)

    elif option == 3:
        manufacturing_scrapping.display_raw_material_stock()

    elif option == 4:
        manufacturing_scrapping.display_final_product_stock()

    elif option == 5:
        no_of_raw_material = int(input("Enter no. of Raw Materials to be scrapped: "))
        manufacturing_scrapping.scrap_the_raw_material(no_of_raw_material)

    elif option == 6:
        no_of_product = int(input("Enter no. of Products to be scrapped: "))
        manufacturing_scrapping.scrap_the_product(no_of_product)

    elif option == 7:
        break

    else:
        print("Please Select valid Option")
