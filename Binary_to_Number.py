def binary_array_to_number(array):
    array.reverse()
    a = [i for i, value in enumerate(arr) if value == 1]
    b = [2 ** i for i in a]
    return sum(b)