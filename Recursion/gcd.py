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


result = gcd(196, 84)
print(result)
