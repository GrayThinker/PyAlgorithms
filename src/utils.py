from sort import *
# from graph import Graph
from timeit import timeit
import random
import math
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]

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

def random_graph(alphabet=alphabet, min_degree=0, max_degree=round(len(alphabet)*0.75)):
    d = {}
    for i in alphabet:
        d.update({i : [random.choice(exclude(alphabet, i)) for _ in range(random.randint(min_degree, max_degree))]})
    g = Graph(d)
    return g

def is_power_of_2(num):
    if num == 0:
        return False
    if math.ceil(math.log2(num)) == math.floor(math.log2(num)):
        return True
    return False
