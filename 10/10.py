from functools import reduce

list1 = [[2, 4, 5], [4, 6, 8], [3, 6, 9]]

concat_lists = reduce(lambda a, b: a+b, list1)
filtered_even_number_list = list(filter(lambda item: True if item % 2 else False, concat_lists))

print("Total Sum:  ", sum(concat_lists))
print("Even number sum:  ", sum(filtered_even_number_list))