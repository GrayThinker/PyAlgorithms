from sorts import *
from timeit import timeit

def time_sort(sort, numbers, reps=10):
    # TODO: What if numbers was *number i.e. *args so this works
    # on any function, not just sorts.
    
    main_code = f"{sort}({numbers})"
    
    # setup_code = f"from __main__ import {sort}, {numbers}"

    time_taken = timeit(stmt=main_code,
                        number=reps,
                        globals=globals()) / reps
    
    return time_taken * 1000  # milliseconds


def test_sort(sort, numbers, show=False):
    sorted_numbers = sorted(numbers)
    test_numbers = sort(numbers)
    
    if(show):
        print(f'result: {test_numbers}')

    if (sorted_numbers == test_numbers): 
        return True
    
    return False
