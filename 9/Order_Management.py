from datetime import date
class Sales_Transaction:

    def __init__(self):
        self.product_details = {}
        self.product_stock = {}
        self.customer_details = {}
        self.customer_address = {}
        self.order_details = {}

    @staticmethod
    def prepare_product():
        user_input = {
            'name': input("Name of Product:  "),
            'product_unit_price': int(input("Product Unit Price:  ")),
            'product_cost_price': int(input("Product Cost Price:  "))
        }
        while True:
            print("""
            Enter Product Type
                1. stockable
                2. consumable
                3. service
                4. Exit
            """)
            product_type = input("Enter product type or press 4 to Exit:")
            if product_type == '4':
                return False
            elif product_type in ('stockable', 'consumable', 'service'):
                break
            else:
                print("Enter valid product type! ")
                continue
        user_input.update({
            'product_type': product_type,
            'stock': int(input("Enter Stock:  "))
        })
        return user_input

    def manage_product(self):
        user_input = self.prepare_product()
        self.create_product(user_input)

    def create_product(self, user_input):
        new_sku = "PRD" + str(len(self.product_details) + 1)
        self.product_stock[new_sku] = user_input.pop('stock')
        self.product_details[new_sku] = user_input

        self.display_products()
        return new_sku

    def display_products(self):
        product_sku_list = list(self.product_stock.keys())
        print("{:<15}{:<20}{:<10}".format("Product Id", "Product Name", "Stock"))
        print("==========================================")
        for sku in product_sku_list:
            print("{:<15}{:<20}{:<10}".format(sku, self.product_details[sku]['name'], self.product_stock[sku]))

    def update_product_stock(self):
        self.display_products()
        sku = input("Enter product sku id")
        if sku in list(self.product_stock.keys()):
            self.product_stock[sku] += int(input("Add stock quantity to ", sku, " :  "))
            self.display_products()
            return sku
        else:
            print("Product not found!")
            return False

    @staticmethod
    def prepare_customer():
        user_input = {
            'name': input("Name:  "),
            'email': input("Email:  "),
            'phone': input("Phone no:  "),
            'address1': input("Address Line 1:  "),
            'address2': input("Address Line 2:  "),
            'city': input("City:  "),
            'zipcode': input("Zipcode:  "),
            'state': input("State:  "),
            'country': input("Country:  ")
        }
        return user_input

    def manage_customer(self):
        user_input = self.prepare_customer()
        self.create_customer(user_input)

    def create_customer(self, user_input):
        new_customer_id = 'cust_' + str(len(self.customer_details) + 1)
        self.customer_details[new_customer_id] = ({
            'name': user_input.pop('name'),
            'email': user_input.pop('email'),
            'phone': user_input.pop('phone')
        })
        self.customer_address[new_customer_id] = user_input
        return new_customer_id

    def display_customer(self):
        customer_id_list = list(self.customer_details.keys())
        print("{:<15}{:<20}".format("Customer Id", "Customer Name"))
        print("==========================================")
        for customer_id in customer_id_list:
            print("{:<15}{:<20}".format(customer_id, self.product_details[customer_id]['name']))

    def prepare_order_lines(self):
        orderlines = []
        while True:
            print("""
                1. Add Product
                2. Exit
            """)
            option = int(input("Select option:  "))
            if option == 1:
                self.display_products()
                sku = input("Enter Product Id:  ")
                if sku in list(self.product_stock.keys()):
                    product_quantity = int(input("Enter Product Quantity:  "))
                    product_unit_price = self.product_details[sku]['product_unit_price']
                    orderlines.append({
                        'product_sku': sku,
                        'unit_price': product_unit_price,
                        'quantity': product_quantity,
                        'subtotal': product_quantity * product_unit_price,
                        'state': 'draft'
                    })
                    continue
                else:
                    print("Enter Valid Product Id!")
                    continue
            else:
                if len(orderlines) == 0:
                    return False
                else:
                    return orderlines

    def prepare_sales_order(self):
        order_id = 'SO' + str(len(self.order_details) + 1)
        user_input = {}
        while True:
            print("""
                1. Enter Customer Id:
                2. Terminate Order:
            """)
            option = int(input("Select option: "))
            if option == 1:
                self.display_customer()
                customer_id = input("Enter Customer Id:  ")
                if customer_id in list(self.customer_details.keys()):
                    break
                else:
                    print("Enter Valid Customer Id!")
                    continue
            else:
                return False

        if self.prepare_order_lines():
            orderlines = self.prepare_order_lines()
        else:
            return False

        order_date = date(
            int(input("Enter Year (yyyy):")),
            int(input("Enter Month (mm):")),
            int(input("Enter Day (dd):"))
        )
        user_input[order_id] = {
            'customer': customer_id,
            'order_lines': orderlines,
            'order_date': order_date,
            'state': 'draft',
            'order_total_amount': sum(product['subtotal'] for product in orderlines)
        }
        return user_input

    def generate_sales_order(self):
        user_input = self.prepare_sales_order()
        self.create_sales_order(user_input)

    def create_sales_order(self, user_input):
        self.order_details = user_input


sales_transaction = Sales_Transaction()

while True:
    print("""
        1. Add Product
        2. Update Product Stock
        3. Add Customer
        4. Generate Sales Order
    """)
    option = int(input("Select option: "))

    if option == 1:
        sales_transaction.manage_product()