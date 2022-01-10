import csv

file_name = "data.csv"
fields = []
customer_data = {}
with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    fields = next(csv_reader)
    for row in csv_reader:
        customer_data.update({
            row[0]: {
                'customer': {
                    'name': row[1],
                    'address1': row[5],
                    'address2': row[6],
                    'city': row[8],
                    'country': row[9],
                    'zipcode': row[7]
                },
                'orderlines': []
            }
        })
print(fields)
# for k, v in customer_data.items():
#     print(k, ": ")
#     for i, j in v:
#         print(i, ": ")
#         for l, m in j:
#             print(l, ": ", m)
print(customer_data)
print(len(customer_data))