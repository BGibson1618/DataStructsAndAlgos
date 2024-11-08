#Using Loops
def rotate(nums: list[int], k: int) -> None:
    shift = k % len(nums)
    pivot = len(nums) - shift
    temp_list = []
    for i in range(shift):
        temp_list.append(nums[i + pivot])
    for j in range(pivot):
        temp_list.append(nums[j])
    for m in range(len(nums)):
        nums[m] = temp_list[m]
    return None

#Using Reverse Method


inlist = [1,2,3,4,5,6,7]
x = 3
rotate(inlist, x)
print(inlist)