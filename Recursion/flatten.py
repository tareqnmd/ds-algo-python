def flatten(arr):
    res = []
    for item in arr:
        if type(item) is list:
            res.extend(flatten(item))
        else:
            res.append(item)
    return res


res = flatten([1, [[1, [2]]]])
print(res)
