import csv

file_name = "data.csv"
fields = []
customer_data = {}

with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    fields = next(csv_reader)
    countries = {'USA': 'United States of America', 'AU': 'Australia', 'DE': 'Germany', 'ES': 'Spain',
                 'UK': 'United Kingdom', 'IT': 'Italy'}

    for row in csv_reader:
        if not customer_data.get(row[0]):
            customer_data.update({
                row[0]: {
                    'customer': {
                        'name': row[1],
                        'address1': row[5],
                        'address2': row[6],
                        'city': row[8],
                        'country': countries[row[9]],
                        'zipcode': row[7]
                    },
                    'orderlines': []
                }
            })
        customer_data[row[0]]['orderlines'].append({'sku': row[2], 'price': row[4], 'qty': row[3]})
    csv_file.close()

for order_id, value in customer_data.items():
    print(order_id, ": ")
    for name, details in value.items():
        print("  ", name, ": ")
        for item in details:
            if name == 'customer':
                print("    ", item, ": ", details[item])
            else:
                print("    ", item)
    print("\n")
