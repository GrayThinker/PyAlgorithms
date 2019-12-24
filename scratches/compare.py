from timeit import timeit
import random

# print(f'{timeit("list(range(10))")}')
# VS
# print(f'{timeit("[n for n in range(10)]")}')


sorted_list = list(range(10))

# print(timeit("broken_list = [sorted_list[i:i + 2] for i in range(0, len(sorted_list), 2)]", "from __main__ import sorted_list"))
# broken_list = []
# main_code = """
# for i in range(0, len(sorted_list), 2): broken_list.append(sorted_list[i:i+2])
# """
# print(timeit(main_code, "from __main__ import broken_list, sorted_list"))
# VS
# print(timeit("broken_list = [sorted_list[i:i + 2] for i in range(0, len(sorted_list), 2)]", "from __main__ import sorted_list"))
