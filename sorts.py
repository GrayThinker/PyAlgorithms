"""
TODO: Radix sort, gravity sort, sedge sort,
double selection sort, shell sort, comb sort,
odd even sort, smooth sort, gnome sort, weak-heap sort
funnel sort, cube sort, cache-oblivious distribution sort, 
multi-key quick sort, tournament sort, splay sort.

"""
import math
import random
from timeit import timeit
from matplotlib import pyplot as plt


def main(low=0, high=100, step=1, reps=1, min_num=0, max_num=100):
    """
    Plot each sorting function time over a range of list sizes.
    :param low: smallest list size.
    :param high: largest list size.
    :param step: size difference between subsequent lists.
    :param reps: number of repititions for timeit.
    :param min_num: smallest number in list to be sorted.
    :param max_num: largest number in list to be sorted.
    """

    bogo_times = []
    bubble_times = []
    cocktail_times = []
    insertion_times = []
    merge_times = []
    pigeon_times = []
    selection_times = []
    quick_times = []
    number_of_elements = list(range(low, high, step))

    for num in number_of_elements:
        numbers = [random.randint(min_num, max_num) for _ in range(num)]

        if(not test_sort(cocktail_sort, numbers)):  # for testing current sort
            print("Error")
            continue

        # bogo_times.append(time_sort('bogo_sort', numbers, reps))
        bubble_times.append(time_sort('bubble_sort', numbers, reps))
        cocktail_times.append(time_sort('cocktail_sort', numbers, reps))
        # insertion_times.append(time_sort('insertion_sort', numbers, reps))
        # selection_times.append(time_sort('selection_sort', numbers, reps))
        # merge_times.append(time_sort('merge_sort', numbers, reps))
        # pigeon_times.append(time_sort('pigeon_hole_sort', numbers, reps))
        # quick_times.append(time_sort('quick_sort', numbers, reps))
        print(f'Progress ({low} to {high}): {num}')

    print('done\n')
    
    # plt.plot(number_of_elements, bogo_times, color='#444232', label='Bogo sort')
    plt.plot(number_of_elements, bubble_times, color='#444444', label='Bubble sort')
    plt.plot(number_of_elements, cocktail_times, color='#C7D98E', label='Cocktail sort')
    # plt.plot(number_of_elements, insertion_times, color='#76FA12', label='Insertion sort')
    # plt.plot(number_of_elements, selection_times, color='#adad3b', label='Selection sort')
    # plt.plot(number_of_elements, pigeon_times, color='#b237a9', label='Pigeon hole sort')
    # plt.plot(number_of_elements, merge_times, color='#41F2c4', label='Merge sort')
    # plt.plot(number_of_elements, quick_times, color='#4444F2', label='Quick sort')
    plt.xlabel('Number of elements')
    plt.ylabel('Time taken (ms)')
    plt.legend()
    plt.show()


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


def bogo_sort(l_arr, optimize=True):
    arr = l_arr[:]
    if optimize:
        n = 0
        s_arr = sorted(arr)
        while(n < len(arr)):
            copy = arr[n:]
            random.shuffle(copy)
            arr[n:] = copy
            if arr[n] == s_arr[n]:
                n += 1
        return arr

    while(arr != sorted(l_arr)):
        random.shuffle(arr)

    return arr


def bubble_sort(unsorted_list):
    sorted_list = unsorted_list[:]
    is_sorted = True
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

def cocktail_sort(l_arr):
    arr = l_arr[:]
    n = 0
    m = len(arr) - 1

    while n < m:
        is_sorted = True
        for i in range(n, m):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = False
        if is_sorted: break
        m -= 1
        is_sorted = True
        for j in range(m, n, -1):
            if arr[j] < arr[j -1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                is_sorted = False
        if is_sorted: break
        n += 1
    return arr

def insertion_sort(l_arr):
    arr = l_arr[:]

    for i in range(1, len(l_arr)):
        pointer = i
        while pointer != 0 and arr[pointer] < arr[pointer - 1]:
            arr[pointer], arr[pointer - 1] = arr[pointer - 1], arr[pointer]
            pointer -= 1

    return arr

def merge(list_a, list_b):
    # lists must already be sorted.
    new_list = []
    i = 0
    j = 0
    while (i < len(list_a) and j < len(list_b)):
        if(list_a[i] < list_b[j]):
            new_list.append(list_a[i])
            i += 1
        else:
            new_list.append(list_b[j])
            j += 1
    new_list += list_a[i:]
    new_list += list_b[j:]

    return new_list


def merge_sort(l_arr):
    arr = l_arr[:]

    if len(arr) <= 1: return arr  # empty/sinlge value list

    # break list into groups of 2
    broken_list = [arr[i:i + 2] for i in range(0, len(arr), 2)]

    # sort each group
    for n in broken_list:
        if (len(n) == 2 and n[0] > n[1]):
            n[0], n[1] = n[1], n[0]

    # while there exists multiple groups
    while len(broken_list) != 1:
        arr = []
        for i in range(0, len(broken_list), 2):
            if i == len(broken_list)-1:  # last group
                arr.append(broken_list[i])
                break
            arr.append(merge(broken_list[i], broken_list[i+1]))
            
        broken_list = arr
    return broken_list[0]


def pigeon_hole_sort(nums):
    """
    Best case: Number of key values = number of elements.
    Only works with integers.
    Memory intensive.
    :param nums: list to be sorted
    :return: sorted list
    """

    ls = nums[:]
    if len(ls) <= 1: return ls  # empty/single valued list
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
    for hole_index in range(hole_size):
        while pigeon_hole[hole_index][1] > 0:
            sorted_ls.append(pigeon_hole[hole_index][0])
            pigeon_hole[hole_index][1] -= 1

    return sorted_ls


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


if __name__ == "__main__":
    main(max_num=100, min_num=0, high=500, step=1, low=0)