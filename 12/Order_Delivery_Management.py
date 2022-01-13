from Order_Management import SalesTransaction


class Sales_Order(SalesTransaction):
    def __init__(self):
        super(Sales_Order, self).__init__()
        self.delivery_order = {}

    def prepare_delivery_order(self, order_id):
        current_order = self.order_details[order_id]
        return {
            'sales_order': order_id,
            'customer_id': current_order['customer'],
            'stock_moves': current_order['order_lines'],
            'state': current_order['state']
        }

    def manage_delivery_order(self, order_id):
        user_input = self.prepare_delivery_order(order_id)
        self.create_delivery_order(user_input)

    def create_delivery_order(self, user_input):
        new_delivery_id = 'DO' + str(len(self.delivery_order) + 1)
        self.delivery_order[new_delivery_id] = user_input
        return new_delivery_id

    def set_order_state_to_confirm(self, order_id):
        current_order = self.order_details[order_id]
        super(Sales_Order, self).set_order_state_to_confirm(current_order)
        self.manage_delivery_order(order_id)

    def display_delivery_order(self):
        print("{:<18}{:<18}{:<18}{:<18}".format("Delivery Id", "Order Id", "Customer Id", "State"))
        print("==================================================================")
        for delivery_id, value in self.delivery_order.items():
            print("{:<18}{:<18}{:18}{:18}".format(delivery_id, value['sales_order'], value['customer_id'],
                                                  value['state']))

    def validate_delivery_order(self, delivery_order_id):
        current_delivery_order = self.delivery_order[delivery_order_id]
        order_id = current_delivery_order['sales_order']
        current_order = self.order_details[order_id]
        super(Sales_Order, self).set_order_state_to_done(order_id, current_order)
        for product in current_delivery_order['stock_moves']:
            product['state'] = 'done'
        current_delivery_order['state'] = 'done'

    def cancel_delivery_order(self, delivery_order_id):
        current_delivery_order = self.delivery_order[delivery_order_id]
        for product in current_delivery_order['stock_moves']:
            product['state'] = 'cancel'
        current_delivery_order['state'] = 'cancel'

    def change_delivery_order_state(self):
        self.display_delivery_order()
        delivery_id = input("Enter Delivery Id:  ")
        if delivery_id in list(self.delivery_order.keys()):
            delivery_status = {1: 'validate', 2: 'cancel'}
            current_delivery = self.delivery_order[delivery_id]
            current_state = list(delivery_status.values()).index(current_delivery['state']) + 1
            print("""
                1. Validate
                2. Cancel
            """)
            state = int(input("Select State:  "))
            if state > current_state:
                if state == 1:
                    self.validate_delivery_order(delivery_id)
                elif state == 2:
                    self.cancel_delivery_order(delivery_id)
                else:
                    print("Enter Valid State!")
            else:
                print("Sorry! ")
                print("Your Order is in", current_delivery['state'], " State,")
                print("And Cannot be shifted to ", delivery_status[state], " State!")
        else:
            print("Please, Enter valid Delivery Id!")


sales_order = Sales_Order()

while True:
    print("""
        1. Add Product
        2. Update Product Stock
        3. Add Customer
        4. Generate Sales Order
        5. Change Order State
        6. Change Delivery Order State
        7. Print all Dictionaries
        8. Display Product, Customer, Order, Delivery Data
        9. Exit
    """)
    option = int(input("Select option: "))

    if option == 1:
        sales_order.manage_product()
    elif option == 2:
        sales_order.update_product_stock()
    elif option == 3:
        sales_order.manage_customer()
    elif option == 4:
        sales_order.generate_sales_order()
    elif option == 5:
        sales_order.change_order_state()
    elif option == 6:
        sales_order.change_delivery_order_state()
    elif option == 7:
        print("\n", sales_order.product_details)
        print("\n", sales_order.product_stock)
        print("\n", sales_order.customer_details)
        print("\n", sales_order.order_details)
        print("\n", sales_order.delivery_order)
    elif option == 8:
        sales_order.display_products()
        sales_order.display_customers()
        sales_order.display_sales_orders()
        sales_order.display_delivery_order()
    elif option == 9:
        break
    else:
        print("Select valid option!  ")