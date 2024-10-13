#Using Set Method
def contains_dupes(nums: list[int]) -> bool:
    temp_list = set(nums)
    return len(nums) != len(temp_list)

#Using Hash Table
def contains_dupes2(nums: list[int]) -> bool:
    hset = dict()
    if  len(nums) < 2:
        return False
    for i in range(len(nums)):
        if nums[i] in hset:
            return True
        else:
            hset[nums[i]] = True
    return False


inlist = [1,1,1,3,3,4,3,2,4,2]
print(contains_dupes2(inlist))