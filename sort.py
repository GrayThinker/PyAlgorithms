from matplotlib import pyplot as plt
import random
import timeit


def bubble_sort(nums):
    """

    :param nums: list of numbers to be sorted
    :return: sorted list of numbers
    """
    n = len(nums)
    while n > 1:
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                temp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = temp
        n -= 1
    return nums


def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor
    return arr


def binary_search(ls, val):
    num = len(ls)
    half = num // 2
    cur = ls[half]
    if cur == val:
        return half
    elif val < cur:
        return half + binary_search(ls[cur:], val)
    elif val > cur:
        return binary_search(ls[:cur], val)


def time_bubble_sort(num):
    bubble_time = timeit.timeit('bubble_sort(numbers)',
                                'from __main__ import bubble_sort, numbers',
                                number=num) / num
    return bubble_time


def time_tim_sort(num):
    tim_time = timeit.timeit('sorted(numbers)',
                             'from __main__ import numbers',
                             number=num) / num
    return tim_time


number_of_elements = list(range(10, 100, 10))
reps = 1000  # number of repetitions for timeit
bubble_times = []
tim_times = []
for n in number_of_elements:
    numbers = list(range(n))
    random.shuffle(numbers)
    bubble_times.append(time_bubble_sort(reps))
    tim_times.append(time_tim_sort(reps))

plt.plot(number_of_elements, bubble_times, label='Bubble sort times')
plt.plot(number_of_elements, tim_times, label='Tim sort times')
plt.xlabel('Number of elements')
plt.ylabel('Time taken')
plt.legend()
plt.show()

# numb = 7
# index = binary_search(numbers, numb)
# print(f"binary search for {num} is at index {index}")
# numbers.sort()
# print(numbers)
# print(f"insertion sort time: {timeit.timeit('insertion_sort(numbers)',
# 'from __main__ import insertion_sort, numbers', number=num_times)/num_times}")


