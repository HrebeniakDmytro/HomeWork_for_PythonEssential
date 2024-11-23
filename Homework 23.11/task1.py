def reverse_generator(lst):
    for item in lst[::-1]:
        yield item

# Приклад використання:
my_list = [1, 2, 3, 4, 5]
for item in reverse_generator(my_list):
    print(item)
