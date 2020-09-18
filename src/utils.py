from src.sort import *
from timeit import timeit

def time_sort(sort, numbers, reps=10):
    main_code = f"{sort}({numbers})"
    # setup_code = f"from __main__ import {sort}, {numbers}"
    
    time_taken = timeit(stmt=main_code,
                        number=reps,
                        globals=globals()) / reps
    
    return time_taken * 1000  # milliseconds


def test_sort(numbers, *args, show=False):
    sorted_numbers = sorted(numbers)

    for sort in args:
        test_numbers = sort(numbers)
        
        if(show):
            print(f'{sort} result: {test_numbers}')

        if (sorted_numbers != test_numbers):
            print(f'{sort} error')
            return False
    
    return True

def exclude(l_arr, val):
    arr = [*l_arr]
    if val in arr:
        arr.remove(val)
    return arr

