# from timeit import timeit
# from functools import lru_cache
# import random
# from matplotlib import pyplot as plt

# def time_sort(sort, numbers, reps=10):
#     # FIXME: What if numbers was *number i.e. *args so this works
#     # on any function, not just sorts. Then main_code would be
#     # main_code = f"{sort}({[n for n in numbers[0]]})"
#     main_code = f"{sort}({numbers})"
#     # TODO: adding setup_code="" parameter. 
#     # setup_code = f"from __main__ import {sort}, {numbers}"

#     time_taken = timeit(stmt=main_code,
#                         number=reps,
#                         globals=globals()) / reps
    
#     return time_taken * 1000  # milliseconds

# @lru_cache(maxsize=None)
# def merge1(list_a, list_b):
#     # lists must already be sorted.
#     new_list = []
#     i = 0
#     j = 0
#     while (i < len(list_a) and j < len(list_b)):
#         if(list_a[i] < list_b[j]):
#             new_list.append(list_a[i])
#             i += 1
#         else:
#             new_list.append(list_b[j])
#             j += 1
#     new_list += list_a[i:]
#     new_list += list_b[j:]

#     return new_list

# @lru_cache(maxsize=None)
# def merge_sort1(l_arr):
#     arr = l_arr[:]

#     if len(arr) <= 1: return arr  # empty/sinlge value list

#     # break list into groups of 2
#     broken_list = [arr[i:i + 2] for i in range(0, len(arr), 2)]

#     # sort each group
#     for n in broken_list:
#         if (len(n) == 2 and n[0] > n[1]):
#             n[0], n[1] = n[1], n[0]

#     # while there exists multiple groups
#     while len(broken_list) != 1:
#         arr = []
#         for i in range(0, len(broken_list), 2):
#             if i == len(broken_list)-1:  # last group
#                 arr.append(broken_list[i])
#                 break
#             arr.append(merge1(broken_list[i], broken_list[i+1]))
            
#         broken_list = arr
#     return broken_list[0]

# def merge2(list_a, list_b):
#     # lists must already be sorted.
#     new_list = []
#     i = 0
#     j = 0
#     while (i < len(list_a) and j < len(list_b)):
#         if(list_a[i] < list_b[j]):
#             new_list.append(list_a[i])
#             i += 1
#         else:
#             new_list.append(list_b[j])
#             j += 1
#     new_list += list_a[i:]
#     new_list += list_b[j:]

#     return new_list


# def merge_sort2(l_arr):
#     arr = l_arr[:]

#     if len(arr) <= 1: return arr  # empty/sinlge value list

#     # break list into groups of 2
#     broken_list = [arr[i:i + 2] for i in range(0, len(arr), 2)]

#     # sort each group
#     for n in broken_list:
#         if (len(n) == 2 and n[0] > n[1]):
#             n[0], n[1] = n[1], n[0]

#     # while there exists multiple groups
#     while len(broken_list) != 1:
#         arr = []
#         for i in range(0, len(broken_list), 2):
#             if i == len(broken_list)-1:  # last group
#                 arr.append(broken_list[i])
#                 break
#             arr.append(merge2(broken_list[i], broken_list[i+1]))
            
#         broken_list = arr
#     return broken_list[0]


# merge1_times = []
# merge2_times = []
# number_of_elements = list(range(0, 10, 1))
# for num in number_of_elements:
#     numbers = [random.randint(0, 500) for _ in range(num)]
#     merge2_times.append(timeit('merge_sort2(numbers)', number=10, globals=globals())/100)
#     # merge1_times.append(timeit('merge_sort1(numbers)', number=100, globals=globals())/100)
#     print(merge_sort1(numbers))
#     print(f'Progress ({0} to {1000}): {num}')
# print('done\n')


# # plt.plot(number_of_elements, merge1_times, color='#41F2c4', label='Merge sort with memo')
# plt.plot(number_of_elements, merge2_times, color='#777777', label='Merge sort no memo')
# plt.xlabel('Number of elements')
# plt.ylabel('Time taken (ms)')
# plt.legend()
# plt.show()





# My first merge sort implementation
# TIL: len(arr) // 2 is much faster than list(len(arr)/2)
# but has more use case limitations
# 
# Code looks very sloppy but it is one of the faster 
# implementations from my testings. Code cleanup can
# be done another day
# 
# 
# def merge(list_a, list_b):
#     # lists must already be sorted.
#     new_list = []
#     i = 0
#     j = 0
#     while (i < len(list_a) and j < len(list_b)):
#         if(list_a[i] < list_b[j]):
#             new_list.append(list_a[i])
#             i += 1
#             # what if both values are the same
#         else:
#             new_list.append(list_b[j])
#             j += 1
#     while (i < len(list_a)): 
#         new_list.append(list_a[i])
#         i += 1
#     while (j < len(list_b)):
#         new_list.append(list_b[j])
#         j += 1

#     return new_list


# def merge_sort(original_list):
#     sorted_list = original_list[:]
#     broken_list = [sorted_list[i:i + 2] for i in range(0, len(sorted_list), 2)]
#     #FIXME: list comprehensions are more computationally taxing
#     for n in broken_list:
#         if (len(n) == 2 and n[0] > n[1]):
#             n[0], n[1] = n[1], n[0]  # could be added to broken_list list comprehension

#     depth = int(math.log(len(sorted_list), 2)) + 1
#     while(depth): # condition yet to be set
#             temp_list = []
#             for i in range(0, len(broken_list), 2):
#                 if (i != len(broken_list) - 1):
#                     temp_list.append(merge(broken_list[i], broken_list[i+1]))
#                 else: broken_list = temp_list.append(broken_list[i])
#             broken_list = temp_list
#             depth -= 1
#     return broken_list[0]





# Code snippets from trying to implement merge sort
# 
# break list into smaller list
# using modulo or list comprehension
# looping through list two values a time
# Using iterator:
# it = iter(lis)
# for x in it:
#     print (x, next(it))

# broken_list.append([x, next(it)] if x < next(it) else [next(it), x])

# Using zip:
# for x, y in zip(*[iter(nums)]*2):
#     print(x, y)
# recursion
# k = 2  # automate with self implemented split function
# for i in range(0,len([1, 2, 3, 4, 5]), 2):
#     print(i)
# i = 0
# j = 0
# while (i < len(list_a) - 1 or j < len(list_b) - 1):
#     if(list_a[i] < list_b[j]):
#         new_list.append(list_a[i])
#         i += 1
#         # what about if both values are the same
#     else:
#         new_list.append(list_b[j])
#         j += 1



# Someone elses Implementation of merge sort:
# My implementation is quicker msort2 and msort3.
# msort4 is faster than my sort due to use of sorted(x)
# 
# 
# def msort2(xx):
#     x = xx[:]
#     if len(x) < 2:
#         return x
#     result = []          # moved!
#     mid = int(len(x) / 2)
#     y = msort2(x[:mid])
#     z = msort2(x[mid:])
#     while (len(y) > 0) and (len(z) > 0):
#         if y[0] > z[0]:
#             result.append(z[0])
#             z.pop(0)
#         else:
#             result.append(y[0])
#             y.pop(0)
#     result += y
#     result += z
#     return result

# def msort3(xx):
#     x = xx[:]
#     if len(x) < 2:
#         return x
#     result = []
#     mid = int(len(x) / 2)
#     y = msort3(x[:mid])
#     z = msort3(x[mid:])
#     i = 0
#     j = 0
#     while i < len(y) and j < len(z):
#         if y[i] > z[j]:
#             result.append(z[j])
#             j += 1
#         else:
#             result.append(y[i])
#             i += 1
#     result += y[i:]
#     result += z[j:]
#     return result

# def msort4(xx):
#     x = xx[:]
#     if len(x) < 20:
#         return sorted(x)
#     result = []
#     mid = int(len(x) / 2)
#     y = msort4(x[:mid])
#     z = msort4(x[mid:])
#     i = 0
#     j = 0
#     while i < len(y) and j < len(z):
#         if y[i] > z[j]:
#             result.append(z[j])
#             j += 1
#         else:
#             result.append(y[i])
#             i += 1
#     result += y[i:]
#     result += z[j:]
#     return result


# Another merge sort under an MIT license. The merge functions are 
# almost identical but the merge_sort functions couldn't have
#  been more different.
# On average my implementation is faster which I did not
# expect.
# 
# 
# def merge(left, right, compare):
#     result = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if compare(left[i], right[j]):
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result

# def mergeSort(L, compare=operator.lt):
#     if len(L) < 2:
#         return L[:]
#     else:
#         middle = int(len(L) / 2)
#         left = mergeSort(L[:middle], compare)
#         right = mergeSort(L[middle:], compare)
#         return merge(left, right, compare)
