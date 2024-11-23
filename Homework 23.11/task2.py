def even_squares_generator(numbers):
    for x in numbers:
        if x % 2 == 0:
            yield x ** 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_of_even = even_squares_generator(numbers)

print(list(squares_of_even))  


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares_of_even = []
for x in numbers:
    if x % 2 == 0:
        squares_of_even.append(x**2)

print(squares_of_even) 
