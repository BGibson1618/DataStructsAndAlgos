#Two Sum
def two_sum_slow(nums: list[int], target: int) -> list[int]:
    temp_list = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                temp_list = [i, j]
                return temp_list


def two_sum_fast(nums:list[int], target: int) -> list[int]:
    temp_dict = {}
    for i, num in enumerate(nums):
        if (target - num) in temp_dict:
            return [temp_dict[target - num], i]
        temp_dict[num] = i