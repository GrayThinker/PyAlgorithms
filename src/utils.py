from src.graph import Graph
from timeit import timeit
from src.sort import *
import random
import math

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

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


def name_gen(alphabet=alphabet):
    length = random.randint(3, 8)
    name = ""
    for i in range(length):
        name += random.choice(alphabet)
    return name


def random_graph(n=5, max_degree = 5, alphabet=alphabet):
    try:
        assert max_degree >= n
        assert len(alphabet) >= n
    except AssertionError as e:
        print("The maximum degree must be >= number of nodes")
        print("The alphabet must be >= number of nodes")
        raise e

    g = Graph()
    new_alpha = [[letter, max_degree] for letter in alphabet]
    for i in range(n+1):
        a = random.choice(new_alpha)
        b = random.choice(new_alpha)
        g.add_ede(a, b)
        a[1] -= 1
        b[1] -= 1
        if a[1] < 1:
            new_alpha.remove(a)
        if b[1] < 1:
            new_alpha.remove(b)    

def random_int_graph(n=5, max_degree=5):
    g = Graph()
    alphabet = [i for i in range(n+1)]
    r = random.choice(alphabet)
    g.add_node(r)
    alphabet.remove(r)

    while n > 0:
        a = random.choice(alphabet)
        alphabet.remove(a)
        b = random.choice(list(g.graph.keys()))
        g.add_edge(a, b)
        n -= 1
        continue
    return g

def is_power_of_2(num):
    if num == 0:
        return False
    if math.ceil(math.log2(num)) == math.floor(math.log2(num)):
        return True
    return False
