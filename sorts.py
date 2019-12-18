# TODO: Radix sort, gravity sort, merge sort, cocktail sort sedge sort
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


def time_sort(sort, numbers, reps=10):
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

    if (sorted_numbers == test_numbers):
        return True
    else: return False


if __name__ == "__main__":
    low = 10  # smallest number of elements
    high = 1000  # highest number of elements
    step = 5  # size difference
    reps = 10  # number of repetitions for timeit (must > 0)

    number_of_elements = list(range(low, high, step))
    bubble_times = []
    selection_times = []
    insertion_times = []
    pigeon_times = []

    for num in number_of_elements:
        numbers = list(range(num))
        random.shuffle(numbers)
        bubble_times.append(time_sort('bubble_sort', 'numbers', reps))
        selection_times.append(time_sort('selection_sort', 'numbers', reps))
        insertion_times.append(time_sort('insertion_sort', 'numbers', reps))
        pigeon_times.append(time_sort('pigeon_hole_sort', 'numbers', reps))
        print(f'Progress ({low} to {high}): {num}')
    print('done\n')
    
    plt.plot(number_of_elements, bubble_times, color='#444444', label='Bubble sort')
    plt.plot(number_of_elements, selection_times, color='#adad3b', label='Selection sort')
    plt.plot(number_of_elements, insertion_times, color='#76FA12', label='Insertion sort')
    plt.plot(number_of_elements, pigeon_times, color='#b237a9', label='Pigeon hole sort')
    plt.xlabel('Number of elements')
    plt.ylabel('Time taken (ms)')
    plt.legend()
    plt.show()
