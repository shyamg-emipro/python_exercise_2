from openpyxl import Workbook

customer_data = {'SO001': {
    'customer': {'name': 'Mohit Patel', 'address1': 'Address 0002', 'address2': 'Address2 0001', 'city': 'Amritsar',
                 'country': 'United States of America', 'zipcode': '1720'},
    'orderlines': [{'sku': 'STARCD173501', 'price': '25', 'qty': '1'},
                   {'sku': 'STARCD173502', 'price': '30', 'qty': '2'},
                   {'sku': 'STARCD173503', 'price': '87', 'qty': '5'},
                   {'sku': 'STARCD173504', 'price': '45', 'qty': '4'}]}, 'SO003': {
    'customer': {'name': 'Ketan Desai', 'address1': 'Address 0011', 'address2': 'Address2 0030', 'city': 'Sydney',
                 'country': 'Australia', 'zipcode': '67806'},
    'orderlines': [{'sku': 'MALTAF104511', 'price': '45', 'qty': '7'},
                   {'sku': 'MALTAF104512', 'price': '94', 'qty': '1'},
                   {'sku': 'MALTAF104513', 'price': '97', 'qty': '2'},
                   {'sku': 'STARCF182801', 'price': '113', 'qty': '4'},
                   {'sku': '7PLUSF173202', 'price': '114', 'qty': '5'},
                   {'sku': 'STARCE172901', 'price': '136', 'qty': '4'},
                   {'sku': 'STARCE172902', 'price': '138', 'qty': '1'}]}, 'SO004': {
    'customer': {'name': 'Ankit Batra', 'address1': 'Address 0005', 'address2': 'Address2 0012', 'city': 'Hamburg',
                 'country': 'Spain', 'zipcode': '22589'},
    'orderlines': [{'sku': 'STARCD173501', 'price': '88', 'qty': '6'},
                   {'sku': 'MALTAF104511', 'price': '95', 'qty': '4'},
                   {'sku': 'ASTN173502', 'price': '102', 'qty': '5'},
                   {'sku': 'MSCE183104', 'price': '105', 'qty': '7'}]}, 'SO002': {
    'customer': {'name': 'Rajesh', 'address1': 'Address 0006', 'address2': 'Address2 0007', 'city': 'Dörrmoschel',
                 'country': 'Germany', 'zipcode': '67806'},
    'orderlines': [{'sku': '7PLUSF173201', 'price': '89', 'qty': '5'},
                   {'sku': '7PLUSF173201', 'price': '90', 'qty': '6'},
                   {'sku': '7PLUSF173201', 'price': '93', 'qty': '3'},
                   {'sku': 'ASTN173502', 'price': '100', 'qty': '4'},
                   {'sku': '7PLUSF174501', 'price': '141', 'qty': '5'},
                   {'sku': 'MALTAE150301', 'price': '144', 'qty': '6'},
                   {'sku': 'MALTAE150301', 'price': '146', 'qty': '2'}]}, 'SO006': {
    'customer': {'name': 'Mihir Tanna', 'address1': 'Address 0008', 'address2': 'Address2 0016', 'city': 'New York',
                 'country': 'United Kingdom', 'zipcode': '1720'},
    'orderlines': [{'sku': '7PLUSF173201', 'price': '91', 'qty': '4'}, {'sku': 'ASTN173502', 'price': '99', 'qty': '6'},
                   {'sku': 'MSCE183104', 'price': '104', 'qty': '7'}, {'sku': 'MSCE183105', 'price': '106', 'qty': '5'},
                   {'sku': 'MSCE183109', 'price': '108', 'qty': '6'},
                   {'sku': 'STARCE172901', 'price': '134', 'qty': '2'},
                   {'sku': 'STARCE172902', 'price': '137', 'qty': '7'}]}, 'SO005': {
    'customer': {'name': 'Prashant Singh', 'address1': 'Address 0015', 'address2': 'Address2 0015',
                 'city': 'Hamburg Sülldorf', 'country': 'Italy', 'zipcode': '22589'},
    'orderlines': [{'sku': 'MALTAF104511', 'price': '98', 'qty': '3'}]}, 'SO010': {
    'customer': {'name': 'Ajit Kapoor', 'address1': 'Address 0029', 'address2': 'Address2 0035', 'city': 'Peru',
                 'country': 'Italy', 'zipcode': '28778'},
    'orderlines': [{'sku': 'STARCF182801', 'price': '112', 'qty': '2'},
                   {'sku': '7PLUSF173202', 'price': '118', 'qty': '4'}]}}

fields = ['Order No', 'Customer', 'SKU', 'QTY', 'Price', 'Address1', 'Address2', 'Zipcode', 'City', 'Country']

rows = []

for order_id, values in customer_data.items():
    for items in values['orderlines']:
        rows.append([
            order_id,
            values['customer']['name'],
            items['sku'],
            items['qty'],
            items['price'],
            values['customer']['address1'],
            values['customer']['address2'],
            values['customer']['zipcode'],
            values['customer']['city'],
            values['customer']['country']
        ])

workbook = Workbook()

worksheet = workbook.create_sheet("Customer Orders", 0)

worksheet.append(fields)

for row in rows:
    worksheet.append(row)

workbook.save(filename="Orders.xls")
workbook.close()

print("File Created Successfully!")
