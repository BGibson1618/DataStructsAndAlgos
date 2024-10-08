array1, array2 = ['x', 'y', 'z'], ['a', 'b', 'x']

def contains_common1(arr1, arr2):
    for i in arr1:
        for j in arr2:
            if i == j:
                return True
    return False

def contains_common2(arr1, arr2):
    for item in arr2:
        if item in arr1:
            return True
    return False