from timeit import timeit
from matplotlib import pyplot as plt

def time_sort(sort, numbers, reps=10):
    main_code = f"{sort}({numbers})"
    time_taken = timeit(stmt=main_code,
                        number=reps,
                        globals=globals()) / reps
    
    return time_taken * 1000


def test_sort(sort, numbers, show=False):
    sorted_numbers = sorted(numbers)
    test_numbers = sort(numbers)
    if(show): print(f'result: {test_numbers}')

    if (sorted_numbers == test_numbers): return True
    
    return False

def quick_sort(l_arr):
    arr = l_arr[:]
    if len(arr) <= 1: return arr
    pivot = -1
    i = 0
    for j in range(len(arr) - 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]        
            i += 1
        j += 1
    arr[pivot], arr[i] = arr[i], arr[pivot]
    if(i == len(arr)-1): return quick_sort(arr[:i]) + quick_sort(arr[i:])
    return quick_sort(arr[:i]) + arr[i:i+1] + quick_sort(arr[i+1:])

def opt_quick_sort(l_arr):
    arr = l_arr[:]
    if len(arr) <= 1: return arr
    less_ls, equal_ls, greater_ls = [], [], []
    pivot = arr[-1]
    for val in arr:
        if val < pivot: less_ls.append(val)
        elif val == pivot: equal_ls.append(val)
        else: greater_ls.append(val)
    return opt_quick_sort(less_ls) + equal_ls + opt_quick_sort(greater_ls)


import random
low = 10
high = 1000
step = 20
reps = 10
quick_times = []
q_times = []
number_of_elements = list(range(low, high, step))
ii = 0
for num in number_of_elements:
    numbers = list(range(num))
    # numbers += list(range(num//5))
    # numbers += list(range(num//3, num))
    # numbers += list(range(num//2))
    random.shuffle(numbers)
    if(not test_sort(opt_quick_sort, numbers)):
        print("ERROR")
        print("numbers")
        break
    q_times.append(time_sort('opt_quick_sort', 'numbers', reps))
    quick_times.append(time_sort('quick_sort', 'numbers', reps))
    print(ii)
    ii += 1
    

plt.plot(number_of_elements, quick_times, color='#4444F2', label='my Original qsort')
plt.plot(number_of_elements, q_times, color='#FF413B', label='My Optimized qsort')
plt.xlabel('Number of elements')
plt.ylabel('Time taken (ms)')
plt.legend()
plt.show()
# ls = list(range(100))
# random.shuffle(ls)
# print(test_sort(quick_sort, ls))