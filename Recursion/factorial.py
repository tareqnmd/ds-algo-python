def factorial(n):
    assert int(n) == n and n >= 0, "The number must be positive only!"
    # if n == 0 or n == 1:
    if n in [0, 1]:
        return 1
    return n * factorial(n - 1)


factorial_value = factorial(5)
print(factorial_value)

# factorial_value_input = input("Enter factorial number: ")
# try:
#     factorial_value = factorial(int(factorial_value_input))
#     print(factorial_value)
# except:
#     print("Only positive integer are allowed!!")
