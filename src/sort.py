"""
TODO: Radix sort, gravity sort, sedge sort,
double selection sort, shell sort, comb sort, bitonic, heap,
odd even sort, smooth sort, gnome sort, weak-heap sort, bucket,
funnel sort, cube sort, cache-oblivious distribution sort, 
multi-key quick sort, tournament sort, splay sort, tree sort.

TODO: Memory profiler
"""
import random
import copy
import math

def bitonic_sort(l_arr):
    #assert is_power_of_2(len(l_arr))
    arr = l_arr[:]    
    n = 0
    while 2**n < len(arr):
        temp_limit = n
        while(temp_limit >= 0):
            i = 0
            switch_compare = True
            switch_tracker = 0
            jump_tracker = 0
            gap = 2 ** temp_limit
            while i < len(arr) - gap:
                if (switch_compare):
                    arr[i], arr[i+gap] = min(arr[i], arr[i+gap]), max(arr[i], arr[i+gap])
                else:
                    arr[i+gap], arr[i] = min(arr[i], arr[i+gap]), max(arr[i], arr[i+gap])
                jump_tracker += 1
                switch_tracker += 1
                if(jump_tracker == gap):
                    jump_tracker = 0
                    i += gap
                    if (switch_tracker == 2**n):
                        switch_compare = not switch_compare
                i += 1
            temp_limit -= 1
        n += 1

    return arr


def bogo_sort(itr, optimize=True):
    """
    optimize: bool whether or not to optimize
    O(n!)
    """
    arr = itr[:]
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

    while(arr != sorted(itr)):
        random.shuffle(arr)

    return arr


def bubble_sort(itr):
    """
    Worst-case: O(n^2) comparisons, O(n^2) swaps
    Best-case: O(n) comparisons, O(1) swaps
    Worst-case space: O(n) total, O(1) auxiliary
    """
    arr = list(copy.copy(itr))
    is_sorted = True
    n = len(arr)
    while n > 1:
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                is_sorted = False
        if is_sorted: break
        is_sorted = True
        n -= 1
    return arr


def cocktail_sort(itr):
    arr = itr[:]
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


def insertion_sort(itr):
    arr = itr[:]
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


def rec_merge_sort(itr):
    arr = itr[:]
    if len(arr) <=1: 
        return arr
    
    half = len(arr)//2
    return merge(merge_sort(arr[:half]), merge_sort(arr[half:]))


def merge_sort(itr, rec=False):
    if rec:
        return rec_merge_sort(itr)
    arr = itr[:]

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


def pigeon_hole_sort(itr):
    """
    Worst-case: O(N+n) where N = max(itr)-min(itr) and n  = len(itr)
    Best case: Number of key values = number of elements.
    Memory intensive.
    """

    arr = itr[:]
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


def quick_sort(itr):
    arr = itr[:]
    if len(arr) <= 1: return arr
    less_ls, equal_ls, greater_ls = [], [], []
    pivot = arr[-1]
    for val in arr:
        if val < pivot: less_ls.append(val)
        elif val == pivot: equal_ls.append(val)
        else: greater_ls.append(val)
    return quick_sort(less_ls) + equal_ls + quick_sort(greater_ls)


def cycle_sort(itr):
    arr = itr[:]
    pos = 0
    i = arr[pos]
    while pos < len(arr) - 1:
        changed = False
        counter = 0
        for val in arr[pos:]:
            if val < i:
                counter += 1
                changed = True
        if changed:
            while arr[pos + counter] == i:  # for duplicates
                counter += 1
            i, arr[pos + counter] = arr[pos + counter], i
            arr[pos] = float('inf')
        else:
            if arr[pos + counter] == float('inf'):
                arr[pos + counter] = i
            pos += 1
            i = arr[pos]
    return arr


def pancake_sort(itr):
    arr = itr.copy()
    cur = 0
    length = len(arr)
    while cur < length:
        min_idx = arr[cur:].index(min(arr[cur:])) + cur
        if cur != min_idx:  # or remove +cur and check min_idx != 0
            if min_idx != length - 1:
                arr[min_idx:] = reversed(arr[min_idx:])
            arr[cur:] = reversed(arr[cur:])
        cur += 1
    
    return arr


l = [2, 4, 3, 1, 6, 2, 9]
print(insertion_sort(l))
print(l)