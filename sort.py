from matplotlib import pyplot as plt
import random
import timeit


def binary_search(val, ls):
    """

    :param val: value to find in list ls
    :param ls: list of numbers to search through
    :return: index of first instance of val found in ls
    """
    num = len(ls)
    half = num // 2
    cur = ls[half]
    if cur == val:
        return half
    elif val > cur:
        return half + binary_search(ls[cur:], val)
    elif val < cur:
        return binary_search(ls[:cur], val)


def bubble_sort(r_nums):
    not_sorted = False
    nums = r_nums[:]
    n = len(nums)
    while n > 1:
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                not_sorted = True
        if not not_sorted:
            # if the list is already sorted
            break
        not_sorted = False
        n -= 1
    return nums


def insertion_sort(r_ls):
    ls = r_ls[:]
    # Check if each element (i) is less than the prev while there is
    # a prev. If it is the let the prev take the current position
    # and repeat until the condition fails and put i in the final position
    for i in range(1, len(ls)):
        cursor = ls[i]
        pos = i
        while pos > 0 and ls[pos - 1] > cursor:
            # Swap the number down the list
            ls[pos] = ls[pos - 1]
            pos -= 1
        # Break and do the final swap
        ls[pos] = cursor
    return ls


def selection_sort(ls):
    nums = ls[:]
    n = 0
    while n < len(nums):
        min_index = n
        for i in range(n, len(nums)):
            if nums[i] < nums[min_index]:
                min_index = i
        nums[n], nums[min_index] = nums[min_index], nums[n]
        n += 1
    return nums


def pigeon_hole_sort(nums):
    """
    Best case: Number of key values = number of elements.
    Only works with integers.
    Memory intensive.
    :param nums: list to be sorted
    :return: sorted list
    """

    ls = nums[:]

    # 2D bucket list with list[0] holding the value and list[1]
    # holding the number of occurrences of list[0] in ls.
    pigeon_hole = []
    sorted_ls = []

    max_num = max(ls)
    min_num = min(ls)
    hole_size = max_num - min_num + 1

    # Create pigeonhole list with length hole_size
    for i in range(hole_size):
        pigeon_hole.append(0)

    # Each element is added to pigeon hole at index element - min_num
    # The number of elements in a given hole is incremented
    for n in ls:
        pigeon_hole[n - min_num] = n
        # pigeon_hole[n - min_num][1] += 1

    # Loop through each pigeon hole and pop out any values into sorted list
    for count in range(hole_size):
        sorted_ls.append(pigeon_hole[count])
        # Uncomment code and delete previous line if every element is NOT unique
        # while pigeon_hole[count][1] > 0:
        #     sorted_ls.append(pigeon_hole[count][0])
        #     pigeon_hole[count][1] -= 1

    return sorted_ls


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


def time_selection_sort(rep):
    """

    :param rep: number of repetitions to be made
    :return: average time for executing bubble sort in milliseconds
    """
    selection_time = timeit.timeit('selection_sort(numbers)',
                                'from __main__ import selection_sort, numbers',
                                number=rep) / rep
    return selection_time * 1000  # milliseconds


def time_pigeon_sort(rep):
    """

    :param rep: number of repetitions to be made
    :return: average time for executing bubble sort in milliseconds
    """
    pigeon_time = timeit.timeit('pigeon_hole_sort(numbers)',
                                'from __main__ import pigeon_hole_sort, numbers',
                                number=rep) / rep
    return pigeon_time * 1000  # milliseconds


def time_tim_sort(rep):
    tim_time = timeit.timeit('sorted(numbers)',
                             'from __main__ import numbers',
                             number=rep) / rep
    return tim_time * 1000


low = 10  # smallest number of elements
high = 1000  # highest number of elements
step = 10  # size difference

number_of_elements = list(range(low, high, step))
reps = 1000  # number of repetitions for timeit
bubble_times = []
tim_times = []
ins_times = []
sel_times = []
pigeon_times = []


for n in number_of_elements:
    numbers = list(range(n))
    random.shuffle(numbers)
    # bubble_times.append(time_bubble_sort(reps))
    tim_times.append(time_tim_sort(reps))
    # ins_times.append(time_insertion_sort(reps))
    # sel_times.append(time_selection_sort(reps))
    pigeon_times.append(time_pigeon_sort(reps))
    print(f'Progress ({low} to {high}): {n}')
print('done\n')

# plt.plot(number_of_elements, bubble_times, color='#444444', label='Bubble sort')
plt.plot(number_of_elements, tim_times, color='#5a7d9a', label='Tim sort')
# plt.plot(number_of_elements, ins_times, color='#adad3b', label='Insertion sort')
# plt.plot(number_of_elements, sel_times, color='#76FA12', label='Selection sort')
plt.plot(number_of_elements, pigeon_times, color='#b237a9', label='Pigeon hole sort')

# use plt.style.use('style name') for custom built in plot styles e.g 'fivethirtyeight'
# use plt.savefig('C:\path\filename') to save plot as filename.png at 'C:\path\'

plt.xlabel('Number of elements')
plt.ylabel('Time taken (ms)')
plt.legend()
plt.show()
