#Brute Force
def move_zeroes1(nums: list[int]) -> None:
    temp_list = []
    for i in range(len(nums)):
        if nums[i] == 0:
            temp_list.append(0)
    for j in range(len(temp_list)):
        nums.remove(0)
    nums.extend(temp_list)

#Using Sort Method
def key_func(num: int) -> bool:
    return num == 0

def move_zeroes2(nums: list[int]) -> None:
    nums.sort(key = key_func)

#Multiple Swaps
def move_zeroes3(nums: list[int]) -> None:
    swap = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[swap] = nums[swap], nums[i]
            swap += 1
    return None


inlist = [0, 0, 1]
move_zeroes3(inlist)
print(inlist)

