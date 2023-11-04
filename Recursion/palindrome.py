def palindrome(string):
    string = str(string)
    if len(string) == 0:
        return True
    if string[0] != string[len(string) - 1]:
        return False
    return palindrome(string[1:-1])


result = palindrome('11')
print(result)
