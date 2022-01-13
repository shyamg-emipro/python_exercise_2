from datetime import date


class SalesTransaction:
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
        product_types = {1: "stockable", 2: "consumable", 3: "service"}
        while True:
            print("""
            Enter Product Type
                1. stockable
                2. consumable
                3. service
                4. Exit
            """)
            product_type = int(input("Enter product type or press 4 to Exit:  "))
            if product_type == 4:
                return False
            elif product_types[product_type]:
                break
            else:
                print("Enter valid product type! ")
        user_input.update({
            'product_type': product_type,
            'stock': int(input("Enter Stock:  "))
        })
        return user_input

    def manage_product(self):
        user_input = self.prepare_product()
        if user_input:
            self.create_product(user_input)
        else:
            return False

    def create_product(self, user_input):
        new_sku = "PRD" + str(len(self.product_details) + 1)
        self.product_stock[new_sku] = user_input.pop('stock')
        self.product_details[new_sku] = user_input
        self.display_products()
        return new_sku

    def display_products(self):
        print("{:<15}{:<20}{:<10}".format("Product Id", "Product Name", "Stock"))
        print("==========================================")
        for sku, value in self.product_details.items():
            print("{:<15}{:<20}{:<10}".format(sku, value['name'], self.product_stock[sku]))

    def update_product_stock(self):
        self.display_products()
        sku = input("Enter product sku id:  ")
        if sku in list(self.product_stock.keys()):
            self.product_stock[sku] += int(input("Enter Additional stock quantity:  "))
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

    def display_customers(self):
        print("{:<15}{:<20}".format("Customer Id", "Customer Name"))
        print("==============================")
        for customer_id, value in self.customer_details.items():
            print("{:<15}{:<20}".format(customer_id, value['name']))

    def prepare_order_lines(self):
        orderlines = []
        while True:
            print("""
                1. Add Product
                2. Exit
            """)
            option = int(input("Select option:  "))
            if option != 1:
                break
            self.display_products()
            sku = input("Enter Product Id:  ")
            if sku in list(self.product_stock.keys()):
                product_unit_price = self.product_details[sku]['product_unit_price']
                product_quantity = int(input("Enter Product Quantity:  "))
                if self.product_stock[sku] >= product_quantity:
                    # self.product_stock[sku] -= product_quantity
                    for product in orderlines:
                        if sku == product['product_sku']:
                            product['quantity'] += product_quantity
                            product['unit_price'] += product_unit_price
                            product['subtotal'] += product_unit_price * product_quantity
                            break
                    else:
                        orderlines.append({
                            'product_sku': sku,
                            'unit_price': product_unit_price,
                            'quantity': product_quantity,
                            'subtotal': product_quantity * product_unit_price,
                            'state': 'draft'
                        })
                else:
                    print("Not enough product quantity available! ")
            else:
                print("Enter Valid Product Id!")
        if len(orderlines) == 0:
            return False
        else:
            return orderlines

    def prepare_sales_order(self):
        user_input = {}
        while True:
            print("""
                1. Enter Customer Id:
                2. Terminate Order:
            """)
            option = int(input("Select option: "))
            if option == 1:
                self.display_customers()
                customer_id = input("Enter Customer Id:  ")
                if customer_id in list(self.customer_details.keys()):
                    break
                else:
                    print("Enter Valid Customer Id!")
            else:
                return False

        orderlines = self.prepare_order_lines()
        if not orderlines:
            return False

        order_date = date(
            int(input("Enter Year (yyyy):")),
            int(input("Enter Month (mm):")),
            int(input("Enter Day (dd):"))
        )
        user_input = {
            'customer': customer_id,
            'order_lines': orderlines,
            'order_date': order_date,
            'state': 'draft',
            'order_total_amount': sum([product['subtotal'] for product in orderlines])
        }
        return user_input

    def generate_sales_order(self):
        user_input = self.prepare_sales_order()
        self.create_sales_order(user_input)

    def display_sales_orders(self):
        print("{:<18}{:<18}{:<18}{:<18}".format("Order Id", "Customer Id", "Date", "Total Amount"))
        print("==================================================================")
        for order_id, value in self.order_details.items():
            print("{:<18}{:<18}{:18}{:18}".format(order_id, value['customer'], str(value['order_date']), str(value['order_total_amount'])))

    def create_sales_order(self, user_input):
        order_id = 'SO' + str(len(self.order_details) + 1)
        self.order_details[order_id] = user_input
        return order_id

    def generate_invoice(self, order_id):
        order = self.order_details[order_id]
        customer_details = self.customer_details[order['customer']]
        customer_address = self.customer_address[order['customer']]
        orderlines = order['order_lines']
        print("{:<35}{:<35}".format("Order No: " + str(order_id), "Order Date: " + str(order['order_date'])))
        print("{:<35}".format("Order Status: " + order['state']))
        print("{:<35}{:<35}".format("Customer: " + order['customer'] + "  " + customer_details['name'], customer_address['address1']))
        print("{:<35}{:<35}".format(customer_details['phone'], customer_address['address2']))
        print("{:<35}{:<35}".format(customer_details['email'], customer_address['city']))
        print("{:<35}{:<35}".format(" ", customer_address['zipcode']))
        print("{:<35}{:<35}".format(" ", customer_address['country']))

        print("\n\n{:<25}{:<25}{:<25}{:<25}".format("Product Name", "Product Price", "Product Quantity", "Subtotal"))
        print("==========================================================================================")
        for product in orderlines:
            product_name = self.product_details[product['product_sku']]['name']
            product_quantity = str(product['unit_price'])
            product_price = str(product['quantity'])
            product_subtotal = str(product['subtotal'])
            print("{:<25}{:<25}{:<25}{:<25}".format(product_name, product_price, product_quantity, product_subtotal))

    @staticmethod
    def set_order_state_to_draft(current_order):
        for product in current_order['order_lines']:
            product['state'] = 'draft'
        current_order['state'] = 'draft'

    @staticmethod
    def set_order_state_to_confirm(current_order):
        for product in current_order['order_lines']:
            product['state'] = 'confirm'
        current_order['state'] = 'confirm'

    def set_order_state_to_done(self, order_id, current_order):
        for product in current_order['order_lines']:
            product['state'] = 'done'
            self.product_stock[product['product_sku']] -= product['quantity']
        current_order['state'] = 'done'
        self.generate_invoice(order_id)

    @staticmethod
    def set_order_state_to_cancel(current_order):
        for product in current_order['order_lines']:
            product['state'] = 'cancel'
        current_order['state'] = 'cancel'

    def change_order_state(self):
        self.display_sales_orders()
        order_id = input("Enter Order id:  ")
        if order_id in list(self.order_details.keys()):
            order_states = {1: 'cancel', 2: 'draft', 3: 'confirm', 4: 'done'}
            current_order = self.order_details[order_id]
            current_state = list(order_states.values()).index(current_order['state']) + 1
            print("""
                   1. Set to Cancel
                   2. Set to Draft
                   3. Set to Confirm
                   4. Set to Done
               """)
            state = int(input("Select order state: "))
            if current_state != 4:
                if state == 1:
                    self.set_order_state_to_cancel(current_order)
                if current_state + 1 == state:
                    if state == 2:
                        self.set_order_state_to_draft(current_order)
                    if state == 3:
                        self.set_order_state_to_confirm(current_order)
                    if state == 4:
                        self.set_order_state_to_done(order_id, current_order)
            elif current_state == 4:
                print("Sorry! ")
                print("Your Order is in", current_order['state'], " State,")
                print("And Cannot be shifted to ", order_states[state], " State!")
            else:
                print("Please, Select right State!")
