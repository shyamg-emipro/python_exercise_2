import csv
from operator import itemgetter

file_name = "data.csv"
fields = []
customer_data = {}

with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    fields = next(csv_reader)
    csv_data = sorted(csv_reader, key=itemgetter(0))
    countries = {'USA': 'United States of America', 'AU': 'Australia', 'DE': 'Germany', 'ES': 'Spain',
                 'UK': 'United Kingdom', 'IT': 'Italy'}

    for row in csv_data:
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

print(customer_data)