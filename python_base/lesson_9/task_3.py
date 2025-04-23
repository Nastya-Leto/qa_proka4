
def square_numbers(list_numbers):
    list_square_numbers = []
    for number in list_numbers:
        list_square_numbers.append(number**2)
    return list_square_numbers

print(square_numbers([2,4,6]))