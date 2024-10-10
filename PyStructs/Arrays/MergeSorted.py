def merge_sorted_easy(arr1: list[int], arr2: list[int]) -> list[int]:
    assert isinstance(arr1, list) and isinstance(arr2, list), 'Inputs must be lists'
    assert (all(isinstance(item, int)
                and not isinstance(item, bool) for item in arr1)
            and all(isinstance(item, int)
                    and not isinstance(item, bool) for item in arr2)), 'Inputs must contain only integers'
    temp_array = arr1 + arr2
    temp_array.sort()
    return temp_array

def merge_sorted(arr1, arr2):
    if not(isinstance(arr1, list) and isinstance(arr2, list)):
        return 'Invalid Input'
    if len(arr1) == 0 or len(arr2) == 0:
        return arr1 + arr2
    temp_array = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            temp_array.append(arr1[i])
            i+=1
        else:
            temp_array.append(arr2[j])
            j+=1
    return temp_array + arr1[i:] + arr2[j:]


r1, r2 = [0, 3, 4, 31], [1, 2, 3, 4, 5]
print(merge_sorted_easy(r1, r2))

# r1, r2 = [1, 2, 3, 7], 0
# print(merge_sorted(r1, r2))