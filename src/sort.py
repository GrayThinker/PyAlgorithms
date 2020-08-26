"""
TODO: Radix sort, gravity sort, sedge sort,
double selection sort, shell sort, comb sort,
odd even sort, smooth sort, gnome sort, weak-heap sort
funnel sort, cube sort, cache-oblivious distribution sort, 
multi-key quick sort, tournament sort, splay sort.

TODO: Memory profiler
"""
import random

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


def bubble_sort(l_arr):
    """
    Worst-case: O(n^2) comparisons, O(n^2) swaps
    Best-case: O(n) comparisons, O(1) swaps
    Worst-case space: O(n) total, O(1) auxiliary
    """
    arr = l_arr[:]
    is_sorted = True
    n = len(arr)
    while n > 1:
        for i in range(1, n):
            if arr[i] < ar[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                is_sorted = False
        if is_sorted: break
        is_sorted = True
        n -= 1
    return arr


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
    if len(arr) <= 1: return arr

    for i in range(1, len(arr)):
        pointer = i
        while pointer > 0 and arr[pointer] < arr[pointer - 1]:
            arr[pointer], arr[pointer - 1] = arr[pointer - 1], arr[pointer]
            pointer -= 1

    return arr


def merge(list_a, list_b):
    """lists must already be sorted."""
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


def rec_merge_sort(l_arr):
    arr = l_arr[:]
    if len(arr) <=1: 
        return arr
    
    half = len(arr)//2
    return merge(merge_sort(arr[:half]), merge_sort(arr[half:]))


def merge_sort(l_arr):
    arr = l_arr[:]

    if len(arr) <= 1: return arr  # empty/single value list

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


def pigeon_hole_sort(l_arr):
    """
    Worst-case: O(N+n) where N = max(l_arr)-min(l_arr) and n  = len(l_arr)
    Best case: Number of key values = number of elements.
    Memory intensive.
    """

    arr = l_arr[:]
    if len(arr) <= 1: return arr
    s_arr = []

    max_num = max(arr)
    min_num = min(arr)
    hole_size = max_num - min_num + 1
    pigeon_hole = [[0, 0] for i in range(hole_size)]

    # Each element is added to pigeon hole at index element - min_num
    # The number of elements in a given hole is incremented
    for n in arr:
        pigeon_hole[n - min_num][0] = n
        pigeon_hole[n - min_num][1] += 1

    # Loop through each pigeon hole and pop out any values into sorted list
    for hole_index in range(hole_size):
        while pigeon_hole[hole_index][1] > 0:
            s_arr.append(pigeon_hole[hole_index][0])
            pigeon_hole[hole_index][1] -= 1

    return s_arr


def selection_sort(ls):
    """
    worst case: O(n^2) comparisons, O(n) swaps
    best case: O(n) comparisons, O(1) swaps
    Average: O(n^2) comparisons, O(n) swaps
    Worst space: O(1) auxiliary
    """
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



