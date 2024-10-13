#Dynamic / Kadane's
def find_max_sub1(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    if all(i >= 0 for i in nums):
        return sum(nums)
    if all(i < 0 for i in nums):
        return max(nums)
    temp_list = list(nums)
    for i in range(1, len(nums)):
        temp_list[i] = max(nums[i], nums[i] + temp_list[i - 1])
    return max(temp_list)

#Divide and Conquer
def max_closed_sum(nums: list[int], low: int, mid: int, high: int) -> int:
    cur_sum = 0
    left_sum = -10000
    for i in range(mid, low -1, -1):
        cur_sum += nums[i]

        if cur_sum > left_sum:
            left_sum = cur_sum

    cur_sum = 0
    right_sum = -10000
    for i in range(mid, high + 1):
        cur_sum += nums[i]

        if cur_sum > right_sum:
            right_sum = cur_sum

    return max(left_sum + right_sum - nums[mid], left_sum, right_sum)

def find_max_sub2(nums: list[int], low: int, high: int):
    if low > high:
        return -10000
    if low == high:
        return nums[low]
    else:
        pivot = (low + high)//2
    return max(find_max_sub2(nums, low, pivot -1), find_max_sub2(nums, pivot + 1, high),
               max_closed_sum(nums, low, pivot, high))

inlist = [5,4,-1,7,8]
print(find_max_sub2(inlist, 0, len(inlist) - 1))

