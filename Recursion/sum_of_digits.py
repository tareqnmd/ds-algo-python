def sum_of_digits(n):
    assert n >= 0
    if n < 10:
        return n
    return int(n % 10) + sum_of_digits(int(n / 10))


input_number = input("Enter your number: ")
try:
    input_number_int = int(input_number)
    sum_digits = sum_of_digits(input_number_int)
    print(sum_digits)
except:
    print("Please enter positive number only")
