def decimal_to_primary(num):
    assert int(num) == num, "The number must be positive only!"
    if num == 0:
        return 0
    quotient = int(num / 2)
    res = num % 2 + 10 * decimal_to_primary(quotient)
    return res


result = decimal_to_primary(10)
print(result)
