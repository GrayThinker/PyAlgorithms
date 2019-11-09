import random
import timeit


def bubble_sort(nums):
    n = len(nums)
    while n > 1:
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                temp = nums[i]
                nums[i] = nums[i-1]
                nums[i-1] = temp
        n -= 1
    return nums
