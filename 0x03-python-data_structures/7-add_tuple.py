def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two elements from each tuple, using 0 for missing values
    a1, a2 = tuple_a[:2] + (0, 0)
    b1, b2 = tuple_b[:2] + (0, 0)

    # Perform addition
    result = (a1 + b1, a2 + b2)

    return result

# Example usage:
tuple_1 = (1, 2)
tuple_2 = (3, 4)
result = add_tuple(tuple_1, tuple_2)
print(result)
