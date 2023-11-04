def gcd(first, sec):
    assert (
        int(first) == first and int(sec) == sec
    ), "The exponent must be positive integer only"
    if first < 0:
        first = -1 * first
    if sec < 0:
        sec = -1 * sec
    if sec == 0:
        return first
    return gcd(sec, first % sec)


first = 10
second = 12
gcd_result = gcd(first, second)
abs_multiply = abs(first * second)
result = int(abs_multiply / gcd_result)
print(result)
