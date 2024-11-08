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

#Rotate in Place
def rotate2(nums: list[int], k: int) -> None:
    for _ in range(k):
        num = nums.pop()
        nums.insert(0, num)
    return None

#Rotate Using Reverse
def rotate3(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    nums.reverse()
    reverse(0, k -1)
    reverse(k, n -1 )