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


def insertion_sort(ls):
    """

    :param ls: list to be sorted
    :return: sorted list
    """
    for i in range(len(ls)):
        cursor = ls[i]
        pos = i

        while pos > 0 and ls[pos - 1] > cursor:
            # Swap the number down the list
            ls[pos] = ls[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        ls[pos] = cursor
    return ls


def binary_search(val, ls):
    """

    :param val: value to find in list ls
    :param ls: list of numbers to search through
    :return: indec of first instance of val found in ls
    """
    num = len(ls)
    half = num // 2
    cur = ls[half]
    if cur == val:
        return half
    elif val < cur:
        return half + binary_search(ls[cur:], val)
    elif val > cur:
        return binary_search(ls[:cur], val)


def time_bubble_sort(rep):
    """

    :param rep: number of repetitions to be made
    :return: average time for executing bubble sort in milliseconds
    """
    bubble_time = timeit.timeit('bubble_sort(numbers)',
                                'from __main__ import bubble_sort, numbers',
                                number=rep) / rep
    return bubble_time * 1000  # milliseconds


def time_insertion_sort(rep):
    ins_time = timeit.timeit('insertion_sort(numbers)',
                             'from __main__ import insertion_sort, numbers',
                             number=rep) / rep
    return ins_time * 1000


def time_tim_sort(rep):
    tim_time = timeit.timeit('sorted(numbers)',
                             'from __main__ import numbers',
                             number=rep) / rep
    return tim_time * 1000


low = 10; high = 100; step = 10  # not very pythonic eh
number_of_elements = list(range(low, high, step))
reps = 10000  # number of repetitions for timeit
bubble_times = []
tim_times = []
ins_times = []

for n in number_of_elements:
    numbers = list(range(n))
    random.shuffle(numbers)
    bubble_times.append(time_bubble_sort(reps))
    tim_times.append(time_tim_sort(reps))
    ins_times.append(time_insertion_sort(reps))
    print(f'Progress ({low} to {high}): {n}')
print('done\n')

plt.plot(number_of_elements, bubble_times, color='#444444', label='Bubble sort')
plt.plot(number_of_elements, tim_times, color='#5a7d9a', label='Tim sort')
plt.plot(number_of_elements, ins_times, color='#adad3b', label='Insertion sort')

# use plt.style.use('style name') for custom built in plot styles e.g 'fivethirtyeight'
# use plt.savefig('C:\path\filename') to save plot as filename.png at 'C:\path\'

plt.xlabel('Number of elements')
plt.ylabel('Time taken (ms)')
plt.legend()
plt.show()
