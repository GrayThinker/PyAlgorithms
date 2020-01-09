"""
TODO: Radix sort, gravity sort, cocktail sort sedge sort,
double selection sort, shell sort, comb sort,
odd even sort, smooth sort, gnome sort, weak-heap sort
funnel sort, cube sort, cache-oblivious distribution sort, 
multi-key quick sort, tournament sort, splay sort.

"""
import math
import random
from timeit import timeit
from matplotlib import pyplot as plt


def bubble_sort(unsorted_list):
    """
    is_sorted checks if a swap was performed in the prev
    iteration/sweep. If not then the list is already sorted
    and the while loop is broken.
    """
    is_sorted = True
    sorted_list = unsorted_list[:]
    num_elements = len(sorted_list)
    while num_elements > 1:
        for i in range(1, num_elements):
            if sorted_list[i] < sorted_list[i - 1]:
                sorted_list[i], sorted_list[i - 1] = \
                    sorted_list[i - 1], sorted_list[i]
                is_sorted = False
        if is_sorted: break
        is_sorted = True
        num_elements -= 1
    return sorted_list


def insertion_sort(unsorted_list):
    sorted_list = unsorted_list[:]
    # Check if each element (i) is less than the prev while there is
    # a prev. If it is then let the prev take the current position
    # and repeat until the condition fails and put i in the final position
    for i in range(1, len(sorted_list)):
        cursor = sorted_list[i]
        pos = i
        while pos > 0 and sorted_list[pos - 1] > cursor:
            # Swap the number down the list
            sorted_list[pos] = sorted_list[pos - 1]
            pos -= 1
        # Break and do the final swap
        sorted_list[pos] = cursor
    return sorted_list


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

    sorted_ls = []

    max_num = max(ls)
    min_num = min(ls)
    hole_size = max_num - min_num + 1
    pigeon_hole = [[0, 0] for i in range(hole_size)]

    # Each element is added to pigeon hole at index element - min_num
    # The number of elements in a given hole is incremented
    for n in ls:
        pigeon_hole[n - min_num][0] = n
        pigeon_hole[n - min_num][1] += 1

    # Loop through each pigeon hole and pop out any values into sorted list
    for count in range(hole_size):
        while pigeon_hole[count][1] > 0:
            sorted_ls.append(pigeon_hole[count][0])
            pigeon_hole[count][1] -= 1

    return sorted_ls


def merge(list_a, list_b):
    # lists must already be sorted.
    new_list = []
    i = 0
    j = 0
    while (i < len(list_a) and j < len(list_b)):
        if(list_a[i] < list_b[j]):
            new_list.append(list_a[i])
            i += 1
            # what if both values are the same
        else:
            new_list.append(list_b[j])
            j += 1
    new_list += (list_a[i:])
    new_list += (list_b[j:])

    return new_list


def merge_sort(arr):
    broken_list = [arr[i:i + 2] for i in range(0, len(arr), 2)]
    for n in broken_list:
        if (len(n) == 2 and n[0] > n[1]):
            n[0], n[1] = n[1], n[0]

    depth = int(math.log(len(arr), 2)) + 1
    while(depth):
        temp_list = []
        for i in range(0, len(broken_list), 2):
            if (i != len(broken_list) - 1):
                temp_list.append(merge(broken_list[i], broken_list[i+1]))
            else: broken_list = temp_list.append(broken_list[i])
        broken_list = temp_list
        depth -= 1
    return broken_list[0]


def quick_sort(l_arr):
    arr = l_arr[:]
    if len(arr) <= 1: return arr
    less_ls, equal_ls, greater_ls = [], [], []
    pivot = arr[-1]
    for val in arr:
        if val < pivot: less_ls.append(val)
        elif val == pivot: equal_ls.append(val)
        else: greater_ls.append(val)
    return quick_sort(less_ls) + equal_ls + quick_sort(greater_ls)


def bogo_sort(l_arr):
    arr = l_arr[:]
    while(arr != sorted(l_arr)):
        random.shuffle(arr)

    return arr


def opt_bogo_sort(l_arr):
    arr = l_arr[:]
    n = 0
    s_arr = sorted(arr)
    while(n < len(arr)):
        copy = arr[n:]
        random.shuffle(copy)
        arr[n:] = copy
        if arr[n] == s_arr[n]:
            n += 1
    return arr


def shell_sort(l_arr):
    """
    Based on insertion sort. Has a worst time compexity of polynomial
    time. 
    """
    pass


def gravity_sort(l_arr):
    pass



def time_sort(sort, numbers, reps=10):
    # FIXME: What if numbers was *number i.e. *args so this works
    # on any function, not just sorts. Then main_code would be
    # main_code = f"{sort}({[n for n in numbers[0]]})"
    main_code = f"{sort}({numbers})"
    # TODO: adding setup_code="" parameter. 
    # setup_code = f"from __main__ import {sort}, {numbers}"

    time_taken = timeit(stmt=main_code,
                        number=reps,
                        globals=globals()) / reps
    
    return time_taken * 1000  # milliseconds


def test_sort(sort, numbers, show=False):
    sorted_numbers = sorted(numbers)
    test_numbers = sort(numbers)
    if(show): print(f'result: {test_numbers}')

    if (sorted_numbers == test_numbers): return True
    
    return False


if __name__ == "__main__":
    low = 1  # smallest number of elements
    high = 50  # highest number of elements
    step = 1  # size difference
    reps = 1  # number of repetitions for timeit (must > 0)
    
    number_of_elements = list(range(low, high, step))
    bubble_times = []
    selection_times = []
    insertion_times = []
    pigeon_times = []
    merge_times = []
    quick_times = []
    bogo_times = []
    opt_bogo_times = []

    for num in number_of_elements:
        numbers = list(range(num))
        numbers += list(range(num//5))
        numbers += list(range(num//3, num))
        numbers += list(range(num//2))
        random.shuffle(numbers)
        # print(f'numbers: {numbers}')
        if(not test_sort(opt_bogo_sort, numbers)):  # for testing current sort
            print("ERROR")
            break
        # bogo_times.append(time_sort('bogo_sort', numbers, reps))
        # opt_bogo_times.append(time_sort('opt_bogo_sort', numbers, reps))
        # bubble_times.append(time_sort('bubble_sort', numbers, reps))
        # selection_times.append(time_sort('selection_sort', 'numbers', reps))
        # insertion_times.append(time_sort('insertion_sort', 'numbers', reps))
        # pigeon_times.append(time_sort('pigeon_hole_sort', 'numbers', reps))
        # merge_times.append(time_sort('merge_sort', 'numbers', reps))
        # quick_times.append(time_sort('quick_sort', 'numbers', reps))
        print(f'Progress ({low} to {high}): {num}')
    print('done\n')
    
    # plt.plot(number_of_elements, bogo_times, color='#444232', label='Bogo sort')
    # plt.plot(number_of_elements, opt_bogo_times, color='#76D232', label='Opt Bogo sort')
    # plt.plot(number_of_elements, bubble_times, color='#444444', label='Bubble sort')
    # plt.plot(number_of_elements, selection_times, color='#adad3b', label='Selection sort')
    # plt.plot(number_of_elements, insertion_times, color='#76FA12', label='Insertion sort')
    # plt.plot(number_of_elements, pigeon_times, color='#b237a9', label='Pigeon hole sort')
    # plt.plot(number_of_elements, merge_times, color='#41F2c4', label='Merge sort')
    # plt.plot(number_of_elements, quick_times, color='#4444F2', label='Quick sort')
    # plt.xlabel('Number of elements')
    # plt.ylabel('Time taken (ms)')
    # plt.legend()
    # plt.show()
