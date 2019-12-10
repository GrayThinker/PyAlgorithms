from matplotlib import pyplot as plt
import time_sorts
import random

low = 10  # smallest number of elements
high = 200  # highest number of elements
step = 10  # size difference

number_of_elements = list(range(low, high, step))
reps = 100  # number of repetitions for timeit
bubble_times = []
tim_times = []
insertion_sort_times = []
sel_times = []
pigeon_times = []


for no in number_of_elements:
    numbers = list(range(no))
    random.shuffle(numbers)
    bubble_times.append(time_sorts.time_bubble_sort(reps))
    tim_times.append(time_sorts.time_tim_sort(reps))
    insertion_sort_times.append(time_sorts.time_insertion_sort(reps))
    sel_times.append(time_sorts.time_selection_sort(reps))
    pigeon_times.append(time_sorts.time_pigeon_sort(reps))
    print(f'Progress ({low} to {high}): {no}')
print('done\n')

plt.plot(number_of_elements, bubble_times, color='#444444', label='Bubble sort')
plt.plot(number_of_elements, tim_times, color='#5a7d9a', label='Tim sort')
plt.plot(number_of_elements, insertion_sort_times, color='#adad3b', label='Insertion sort')
plt.plot(number_of_elements, sel_times, color='#76FA12', label='Selection sort')
plt.plot(number_of_elements, pigeon_times, color='#b237a9', label='Pigeon hole sort')

# use plt.style.use('style name') for custom built in plot styles e.g 'fivethirtyeight'
# use plt.savefig('C:\path\filename') to save plot as filename.png at 'C:\path\'

plt.xlabel('Number of elements')
plt.ylabel('Time taken (ms)')
plt.legend()
plt.show()
