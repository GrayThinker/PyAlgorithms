from src.graph import Graph
from src.utils import random_graph
from src.utils import test_sort
import random
def counting_sort(l_arr):
    l_arr = l_arr[:]
    count_ls = []
    for i in l_arr:
        position_found = False
        for index in range(len(count_ls)):
            if i == count_ls[index][0]:
                count_ls[index][1] += 1
                position_found = True
                break
            if i < count_ls[index][0]:
                count_ls.insert(index, [i, 1])
                position_found = True
                break
        if position_found == False:
            count_ls.append([i, 1])

    return_ls = []
    for pair_index in range(len(count_ls)):
        while count_ls[pair_index][1] > 0:
            return_ls.append(count_ls[pair_index][0])
            count_ls[pair_index][1] -= 1
    
    return return_ls

# print(counting_sort([1, 4, 1, 2, 7, 5, 2]))
test_sort([random.randint(0, 2000) for i in range(10_000)], counting_sort, show=True)