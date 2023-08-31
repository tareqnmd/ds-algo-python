def fibonacci_number(n):
    assert int(n) == n and n >= 0, "The number must be positive only!"
    if n in [0, 1]:
        return n
    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


fibonacci_numbers = fibonacci_number(6)
print(fibonacci_numbers)
