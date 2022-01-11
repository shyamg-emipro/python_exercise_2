class SalesTransaction:

    def __init__(self):
        self.product = {}
        self.customer = {}
        self.customer_address = {}
        self.sales_order = {}

    def prepare_product(self, product):
        new_element = len(self.product) + 1
        stock_keeping_unit = 'PRD' + str(new_element)
        self.product[stock_keeping_unit] = product
        print(self.product)

    def manage_product(self):
        pass

    def prepare_customer(self, customer, address):
        new_element = len(self.customer) + 1
        customer_id = 'c' + str(new_element)
        self.customer[customer_id] = customer
        self.customer_address[customer_id] = address
        print(self.customer)

    def prepare_order_lines(self, product):
        orderlines = []
        for id, qty in product:
            subtotal = self.product[id]['product_unit_price'] * qty
            orderlines.append({
                'product_sku': id,
                'unit_price': self.product[id]['product_unit_price'],
                'quantity': qty,
                'subtotal': subtotal,
                'state': 'draft'
            })
        return orderlines

    def prepare_sales_order(self, customer_id, order_date, state_of_order, product):
        new_element = len(self.sales_order) + 1
        order_id = 'SO' + str(new_element)
        self.sales_order[order_id] = {
            'customer': customer_id,
            'order_lines': self.prepare_order_lines(product),
            'order_date': order_date,
            'state': state_of_order,
            'order_total_amount': sum(item['subtotal'] for item in self.prepare_order_lines(product))
        }
        print(self.sales_order)


sales_transaction = SalesTransaction()


while True:
    print(""""
        1. Add Product
        2. Manage Product
        3. Add Customer
        4. Place Order
        5. Exit
    """)
    option = int(input("Select option:  "))
    if option == 1:
        product_name = input("Enter Product Name:  ")
        product_unit_price = int(input("Enter unit price of product:  "))
        product_cost_price = int(input("Enter cost price of product:  "))
        product_type = input("Enter product type:  ")
        stock = int(input("Enter quantity of the product:  "))
        sales_transaction.prepare_product({
            'name': product_name,
            'product_unit_price': product_unit_price,
            'product_cost_price': product_cost_price,
            'product_type': product_type,
            'stock': stock
        })

    elif option == 2:
        sales_transaction.manage_product()

    elif option == 3:
        customer_name = input("Name:  ")
        email = input("Email address:  ")
        phone = input("Phone no:  ")
        address1 = input("Address Line 1:  ")
        address2 = input("Address Line 2:  ")
        city = input("City:  ")
        zipcode = input("Zipcode:  ")
        state = input("State:  ")
        country = input("Country: ")
        sales_transaction.prepare_customer({
            'name': customer_name,
            'email': email,
            'phone': phone
        }, {
            'address1': address1,
            'address2': address2,
            'city': city,
            'zipcode': zipcode,
            'state': state,
            'country': country
        })

    elif option == 4:
        while option != 5:
            print("""
                1. Enter Customer Id: 
                5. Exit
            """)
            print(sales_transaction.customer)
            option = int(input("Enter Option:  "))
            if option == 1:
                customer_id = input("Enter Customer id:  ")
                if customer_id not in list(sales_transaction.customer.keys()):
                    print("Warning, Enter valid customer id! ")
                    continue
                else:
                    break
            else:
                option == 5
        else:
            break
        order_date = (int(input("Year:  ")), int(input("Month:  ")), int(input("Day:  ")))
        state_of_order = 'draft'
        print("")
        product = []
        while option != 5:
            print("""
                1. Enter Product
                2. Exit
            """)
            option = int(input("Enter option:  "))
            if option == 1:
                product_id = input("Enter Product id: ")
                if product_id not in list(sales_transaction.product.keys()):
                    print("Please enter valid product id!")
                    continue
                product_quantity = (int(input("Quantity:  ")))
                product.append((product_id, product_quantity))
                break

            else:
                break
        else:
            break
        sales_transaction.prepare_sales_order(customer_id, order_date, state_of_order, product)

    elif option == 5:
        break

    else:
        print("Please Select Valid option!")
