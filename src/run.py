from src.sort import *
from src.utils import *
import random
from matplotlib import pyplot as plt


def main(low=10, high=100, step=10, reps=1, min_num=0, max_num=10000, test=False):
    """
    Plot each sorting function time over a range of list sizes.
    :param low: smallest list size.
    :param high: largest list size.
    :param step: size difference between subsequent lists.
    :param reps: number of repetitions for timing.
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
    cycle_times = []
    pancake_times = []
    counting_times = []

    number_of_elements = list(range(low, high, step))

    for num in number_of_elements:
        numbers = [random.randint(min_num, max_num) for _ in range(num)]
        
        if test:
            if not test_sort(bubble_sort, numbers): raise ValueError("Bubble sort error")
            if not test_sort(merge_sort, numbers): raise ValueError("Merge sort error")
            if not test_sort(cocktail_sort, numbers): raise ValueError("Cocktail sort error")
            if not test_sort(pigeon_hole_sort, numbers): raise ValueError("Pigeonhole sort error")
            if not test_sort(insertion_sort, numbers): raise ValueError("Insertion sort error")
            if not test_sort(quick_sort, numbers): raise ValueError("Quick sort error")
            if not test_sort(cycle_sort, numbers): raise ValueError("Cycle sort error")
            if not test_sort(selection_sort, numbers): raise ValueError("Selection sort error")
            if not test_sort(pancake_sort, numbers): raise ValueError("Pancake sort error")
            if not test_sort(bogo_sort, numbers): raise ValueError("Bogo sort error")
            if not test_sort(counting_sort, numbers): raise ValueError("Counting sort error")
        
        # cycle_times.append(time_sort('cycle_sort', numbers, reps))
        # bogo_times.append(time_sort('bogo_sort', numbers, reps))
        # bubble_times.append(time_sort('bubble_sort', numbers, reps))
        # cocktail_times.append(time_sort('cocktail_sort', numbers, reps))
        insertion_times.append(time_sort('insertion_sort', numbers, reps))
        selection_times.append(time_sort('selection_sort', numbers, reps))
        # merge_times.append(time_sort('merge_sort', numbers, reps))
        # pigeon_times.append(time_sort('pigeon_hole_sort', numbers, reps))
        # quick_times.append(time_sort('quick_sort', numbers, reps))
        # pancake_times.append(time_sort('pancake_sort', numbers, reps))
        counting_times.append(time_sort('counting_sort', numbers, reps))

        print(f'Progress ({low} to {high}): {num}')

    print('done\n')
    
    # plt.plot(number_of_elements, cycle_times, color='#FF43c2', label='Cycle sort')
    # plt.plot(number_of_elements, bogo_times, color='#59B272', label='Bogo sort')
    # plt.plot(number_of_elements, bubble_times, color='#444444', label='Bubble sort')
    # plt.plot(number_of_elements, cocktail_times, color='#C7D98E', label='Cocktail sort')
    plt.plot(number_of_elements, insertion_times, color='#76FA12', label='Insertion sort')
    plt.plot(number_of_elements, selection_times, color='#adad3b', label='Selection sort')
    # plt.plot(number_of_elements, pigeon_times, color='#b237a9', label='Pigeon hole sort')
    # plt.plot(number_of_elements, merge_times, color='#41F2c4', label='Merge sort')
    # plt.plot(number_of_elements, quick_times, color='#7464F2', label='Quick sort')
    # plt.plot(number_of_elements, pancake_times, color='#110893', label='Pancake sort')
    plt.plot(number_of_elements, counting_times, color='#910054', label='Counting sort')
    plt.xlabel('Number of elements')
    plt.ylabel('Time taken (ms)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main(high=2000)
