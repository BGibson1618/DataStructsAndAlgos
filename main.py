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


inlist = [0, 0, 1]
move_zeroes2(inlist)
print(inlist)

