from src.sort import *
from src.utils import *
import random
from matplotlib import pyplot as plt

def main(low=1000, high=10000, step=10, reps=1, min_num=0, max_num=10000):
    """
    Plot each sorting function time over a range of list sizes.
    :param low: smallest list size.
    :param high: largest list size.
    :param step: size difference between subsequent lists.
    :param reps: number of repetitions for timeit.
    :param min_num: smallest number in list to be sorted.
    :param max_num: largest number in list to be sorted.
    """

    # bogo_times = []
    # bubble_times = []
    rec_merge_times = []
    cocktail_times = []
    insertion_times = []
    merge_times = []
    pigeon_times = []
    selection_times = []
    quick_times = []
    number_of_elements = list(range(low, high, step))

    for num in number_of_elements:
        numbers = [random.randint(min_num, max_num) for _ in range(num)]

        # if(not test_sort(insertion_sort, numbers)):  # for testing current sort
        #     print("Error")
        #     continue

        # bogo_times.append(time_sort('bogo_sort', numbers, reps))
        # bubble_times.append(time_sort('bubble_sort', numbers, reps))
        cocktail_times.append(time_sort('cocktail_sort', numbers, reps))
        # insertion_times.append(time_sort('insertion_sort', numbers, reps))
        # selection_times.append(time_sort('selection_sort', numbers, reps))
        rec_merge_times.append(time_sort('rec_merge_sort', numbers, reps))
        merge_times.append(time_sort('merge_sort', numbers, reps))
        pigeon_times.append(time_sort('pigeon_hole_sort', numbers, reps))
        quick_times.append(time_sort('quick_sort', numbers, reps))
        print(f'Progress ({low} to {high}): {num}')

    print('done\n')
    
    # plt.plot(number_of_elements, bogo_times, color='#444232', label='Bogo sort')
    # plt.plot(number_of_elements, bubble_times, color='#444444', label='Bubble sort')
    # plt.plot(number_of_elements, cocktail_times, color='#C7D98E', label='Cocktail sort')
    # plt.plot(number_of_elements, insertion_times, color='#76FA12', label='Insertion sort')
    # plt.plot(number_of_elements, selection_times, color='#adad3b', label='Selection sort')
    plt.plot(number_of_elements, rec_merge_times, color='#987221', label='rec Merge sort')
    plt.plot(number_of_elements, pigeon_times, color='#b237a9', label='Pigeon hole sort')
    plt.plot(number_of_elements, merge_times, color='#41F2c4', label='Merge sort')
    plt.plot(number_of_elements, quick_times, color='#4444F2', label='Quick sort')
    plt.xlabel('Number of elements')
    plt.ylabel('Time taken (ms)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
