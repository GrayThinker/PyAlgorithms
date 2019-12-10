# TODO: Radix sort, gravity sort, merge sort, cocktail sort


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
    # a prev. If it is then let the prev take the current position
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
