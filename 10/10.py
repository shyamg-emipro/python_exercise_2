from functools import reduce

find_sum_list = [[2, 4, 5], [4, 6, 8], [3, 6, 9]]

concat_lists = reduce(lambda a, b: a+b, find_sum_list)  # concat inner lists
filtered_even_number_list = list(filter(lambda item: True if item % 2 else False, concat_lists))  # filters even number

print("Total Sum:  ", sum(concat_lists))  # sum of all elements
print("Even number sum:  ", sum(filtered_even_number_list))  # sum of even elements
